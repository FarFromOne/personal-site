# build_notes.py
# 从 notes-md/*.md 生成 notes/*.html
# 使用 notes/template.html 作为页面模板
import sys
from pathlib import Path
import re

import markdown  # pip install markdown


# ====== 路径配置（按你现在的目录结构写死） ======

# 当前脚本所在目录：personal-site/scripts
SCRIPT_DIR = Path(__file__).resolve().parent
# 项目根目录：personal-site
BASE_DIR = SCRIPT_DIR.parent

# markdown 源文件目录：personal-site/notes-md
MD_DIR = BASE_DIR / "notes-md"
# 输出 html 目录：personal-site/notes
OUT_DIR = BASE_DIR / "notes"
# 模板文件：personal-site/notes/template.html
TEMPLATE_FILE = OUT_DIR / "template.html"

# markdown 中图片所在的“源路径前缀”
# 比如：E:\personal-site\notes-md\pic\ADC\adc1_4.png
# 或   ...notes-md/pic/ADC/adc1_4.png
#MD_IMG_ROOT_PATTERN = r"notes-md[\\/]+pic[\\/]+"
MD_IMG_ROOT_PATTERN = r"pic[\\/]+"
# 在生成的 html 里，图片应指向的相对目录前缀
# notes/*.html -> ../assets/pic/xxx.png
SITE_IMG_PREFIX = "../assets/pic/"

# 是否给 img 包一层居中 div
WRAP_IMG_CENTER = True

# 是否统一给 img 加宽高 / alt
ADD_IMG_ATTR = True
IMG_WIDTH = 600
IMG_HEIGHT = 400
DEFAULT_ALT = "图片"

# 每篇文章的“副标题”手动写在这里（可选）
# key 用 markdown 文件名（不含 .md），value 是你想显示的副标题
SUBTITLE_MAP = {
    # "test": "这是 test 这篇笔记的副标题",
    # "analogch1": "模拟电路第一章",
}


# ====== 工具函数 ======

def load_template() -> str:
    if not TEMPLATE_FILE.exists():
        raise FileNotFoundError(f"找不到模板文件: {TEMPLATE_FILE}")
    return TEMPLATE_FILE.read_text(encoding="utf-8")


def extract_title_subtitle_and_body(md_text: str, fallback_name: str):
    """
    从 markdown 中提取：
    - 第一个一级标题 # ... 作为 article_title
    - 紧跟的一行 <!-- subtitle: ... --> 作为 subtitle （可选）
    并且把这两行（以及中间的空行）从正文里删掉。
    返回: article_title, subtitle, md_body
    """
    import re

    lines = md_text.splitlines()
    title = None
    subtitle = ""
    body_lines = []
    state = "search_h1"   # search_h1 -> after_h1 -> normal

    for line in lines:
        stripped = line.strip()

        if state == "search_h1":
            m = re.match(r"#\s+(.+)", stripped)
            if m:
                title = m.group(1).strip()
                state = "after_h1"
                # 不把这一行放进 body
                continue
            else:
                body_lines.append(line)

        elif state == "after_h1":
            # 1. 看看是不是副标题注释
            m_sub = re.match(r"<!--\s*subtitle\s*:\s*(.+?)\s*-->", stripped, re.I)
            if m_sub:
                subtitle = m_sub.group(1).strip()
                state = "normal"
                # 这一行也不放进 body
                continue

            # 2. 如果是空行，就跳过这一行，继续找正文
            if stripped == "":
                # 不放进 body
                continue

            # 3. 既不是注释也不是空行，说明正文开始了
            state = "normal"
            body_lines.append(line)

        else:  # normal
            body_lines.append(line)

    if title is None:
        title = fallback_name
        body = md_text
    else:
        body = "\n".join(body_lines).lstrip("\n")

    return title, subtitle, body


def md_to_html_fragment(md_text: str) -> str:
    """
    把 Markdown 转成 HTML 片段（不包含 <html> 外壳）
    """
    return markdown.markdown(
        md_text,
        extensions=[
            "fenced_code",
            "tables",
            "codehilite",
            "toc",
        ],
        output_format="html5",
    )


def fix_image_paths(html: str) -> str:
    r"""
    把 markdown 中的图片路径：
    - E:\personal-site\notes-md\pic\ADC\xxx.png
    - ...notes-md/pic/ADC/xxx.png
    统一换成：
    - ../assets/pic/ADC/xxx.png
    """

    # 1）匹配任何包含 pic/ 的绝对/相对路径
    html = re.sub(
        rf'src="[^"]*{MD_IMG_ROOT_PATTERN}([^"]+)"',
        rf'src="{SITE_IMG_PREFIX}\1"',
        html,
        flags=re.IGNORECASE,
    )

    # 2）如果写成 src="pic/ADC/xxx.png"，也一并处理
    html = re.sub(
        r'src="pic[\\/]+([^"]+)"',
        rf'src="{SITE_IMG_PREFIX}\1"',
        html,
        flags=re.IGNORECASE,
    )

    # 3）把 src 里的反斜杠 \ 换成 /
    def normalize_src(m):
        url = m.group(1).replace("\\", "/")
        return f'src="{url}"'

    html = re.sub(r'src="([^"]+)"', normalize_src, html)

    return html


def add_img_attributes(html: str) -> str:
    """
    给所有 <img ...> 加上 width / height / alt（如果原来没有）
    """

    def repl(m):
        attrs = m.group(1)

        # 检查是否已有这些属性
        if 'width=' not in attrs:
            attrs += f' width="{IMG_WIDTH}"'
        if 'height=' not in attrs:
            attrs += f' height="{IMG_HEIGHT}"'

        if 'alt=' not in attrs:
            # 尝试用文件名做 alt
            alt_text = DEFAULT_ALT
            m_src = re.search(r'src="([^"]+)"', attrs)
            if m_src:
                filename = m_src.group(1).split("/")[-1]
                alt_text = filename.rsplit(".", 1)[0]
            attrs += f' alt="{alt_text}"'

        return f"<img{attrs}>"

    html = re.sub(
        r"<img([\s\S]*?)\/?>",
        repl,
        html,
        flags=re.IGNORECASE,
    )
    return html


def wrap_img_center_div(html: str) -> str:
    """
    把图片包进 <div class="img-center"> ... </div>

    1）优先把 <p><img ...></p> -> <div class="img-center"><img ...></div>
    2）单独的 <img ...>（不在 div.img-center 里）也包一层
    """

    # 1) 处理 <p> 包裹的情况（跨行也能匹配）
    html = re.sub(
        r"<p>\s*(<img[\s\S]*?>)\s*</p>",
        r'<div class="img-center">\1</div>',
        html,
        flags=re.IGNORECASE,
    )

    # 2) 处理裸露的 <img>（简单的负向回溯，避免重复包裹）
    html = re.sub(
        r'(?<!<div class="img-center">)\s*<img([\s\S]*?)>',
        r'<div class="img-center"><img\1></div>',
        html,
        flags=re.IGNORECASE,
    )

    return html


def postprocess_html(html: str) -> str:
    """
    对从 markdown 转出来的 html 做后处理：
    - 修正 img 路径
    - 加 img 属性
    - 包 img-center div
    """
    html = fix_image_paths(html)
    if ADD_IMG_ATTR:
        html = add_img_attributes(html)
    if WRAP_IMG_CENTER:
        html = wrap_img_center_div(html)
    return html


def build_page_for_file(md_path: Path, template_html: str):
    """处理单个 .md -> .html"""
    md_text = md_path.read_text(encoding="utf-8")

    #  从 markdown 里拿到 H1 作为标题，并把这行从正文里删掉，拿到特定格式的作为副标题，其余作为正文
    article_title, subtitle, md_body = extract_title_subtitle_and_body(md_text, md_path.stem)
    title = article_title  # 用在<title>里

    #  md -> html 片段（注意现在用的是 md_body，而不是原始 md_text）
    content_html = md_to_html_fragment(md_body)
    content_html = postprocess_html(content_html)

    #  用模板替换占位符
    page_html = template_html
    page_html = page_html.replace("{{TITLE}}", title)
    page_html = page_html.replace("{{ARTICLE_TITLE}}", article_title)
    page_html = page_html.replace("{{SUBTITLE}}", subtitle)
    page_html = page_html.replace("{{CONTENT}}", content_html)

    # 输出同名 .html
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_file = OUT_DIR / (md_path.stem + ".html")
    out_file.write_text(page_html, encoding="utf-8")
    print(f"[OK] {md_path.relative_to(BASE_DIR)} -> {out_file.relative_to(BASE_DIR)}")


def main():
    template_html = load_template()

    args = sys.argv[1:]  # 命令行参数中去掉脚本名本身

    if args:
        # 指定了要处理的 md 文件
        md_files = []
        for name in args:
            p = MD_DIR / name
            # 如果没写 .md 后缀，自动补上
            if p.suffix != ".md":
                p = p.with_suffix(".md")
            if p.exists():
                md_files.append(p)
            else:
                print(f"[WARN] 找不到文件: {p}")
    else:
        # 没有给参数，就处理全部 .md（和之前行为一样）
        md_files = sorted(MD_DIR.glob("*.md"))

    if not md_files:
        print(f"没有需要处理的 markdown 文件")
        return

    for md_file in md_files:
        build_page_for_file(md_file, template_html)



if __name__ == "__main__":
    main()
