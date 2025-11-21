# Single-Transistor and Multiple-Transistor Amplifiers
## 多晶体管放大器

### MOS Cascode

所谓cascode即共源共栅（CS-CG）结构，如下图所示：

<img src="./pic/analog_ic_gray/pic_3.38_3.39.png" width=500 alt="pic_3.38_3.39">

由于输入在栅极，故$R_i\to \infty$，为了得到跨导，令输出短接到地，那么在输出有KCL：
$$
i_o+g_{m2}v_{ds1}+g_{mb2}v_{ds2}+\frac{v_{ds1}}{r_{o2}}=0
$$
在M2的源极有：
$$
g_{m1}v_i+\frac{v_{ds1}}{r_{o1}}+g_{m2}v_{ds1}+g_{mb2}v_{ds1}+\frac{v_{ds1}}{r_{o2}}=0
$$
那么得到跨导：
$$
G_m=\frac{i_o}{v_i}\bigg|_{v_o=0}=g_m\left(1-\frac{1}{1+(g_{m2}+g_{mb2})r_{o1}+\frac{r_{o1}}{r_{o2}}}\right)
$$
可以看到这个值是小于1的，但由于$(g_{m2}+g_{mb2})r_{o1}\gg1$，所以这个值可以近似认为是1，那么也就有$G_m\simeq g_{m1}$，也就是说cascode结构并不会怎么影响跨导，这是由于M2从源极看进去的阻抗导致的，我们把它记为$R_{i2}$，同时，将负载记为$R$，正如图中所示，在电路中它表现为M2漏极连接的电流源负载（或电阻偏置负载之类）和输出负载的并联，如$R=R_D\parallel R_L$，那么从M2的源极看进去的电阻为：
$$
R_{i2}=\frac{r_{o2}+R}{1+(g_{m2}+g_{mb2})r_{o2}}\simeq \frac{1}{g_{m2}+g_{mb2}}+\frac{R}{(g_{m2}+g_{mb2})r_{o2}}
$$
当然，在测试跨导时，由于输出短接，$R=0$，那么可以看到输入的共源级电流$i=g_{m1}v_i$，会流向$r_{o1}$和$R_{i2}$的并联，相较于前者，后者电阻更小，那么大部分电流流向共栅管，同时，由于共栅管的电流增益为1，所以大部分的电流流去输出，也就导致$G_m\simeq g_{m1}$，这里可以再进一步说一下，由于$R_{i2}$的值很小，导致M1单管的增益其实很小，即$A_{v1}=g_{m1}R_{o1}=g_{m1}(r_{o1}\parallel R_{i2})\simeq g_{m1}R_{i2}$，假设$R_{i2}$中的负载项$R$，与$r_{o2}$数量级一致，那么这个增益也就为$A_{v1}\simeq \frac{2g_{m1}}{g_{m2}+g_{mb2}}$，可以近似认为是2左右的数量级，这会带来一个好处，就是它削弱了M1的米勒效应，M1的$C_{gd}$电容受到米勒效应等效到输入的电容不会变大很大，进而不会产生很大的频率影响。

回到输出阻抗，根据共栅级的公式很容易得到输出阻抗为：
$$
R_o=r_{o1}+r_{o2}+(g_{m2}+g_{mb2})r_{o1}r_{o2}\simeq (g_{m2}+g_{mb2})r_{o1}r_{o2}
$$
那么最后，整个cascode结构的增益为$A_v=G_mR_o=\simeq g_{m1}(g_{m2}+g_{mb2})r_{o1}r_{o2}$，也就是两个MOS管本征增益的数量级，鉴于MOS管不受电流增益$\beta$的影响，故而可以继续堆叠共栅管以提高增益，会引发一系列问题，其中之一就是消耗过多电压裕度。在BiCMOS工艺中，可以用bipolar来替代共栅的MOS管，因为前者有着更高的跨导$g_m$，而MOS管有着输入电流为0的优点，也正如前面提到的，更小的M1负载也可以提供更好的频率响应，这一点后面会提到。

### Active Cascode

<img src="./pic/analog_ic_gray/pic_3.41.png" width=500 alt="pic_3.41">

如图所示，展示了一种不堆叠共栅管来提高共源共栅管的增益的方法，也就是通过增加一个辅助放大器形成负反馈来提高增益，定性而言，假如该辅助放大器的增益$a$为无穷大，那么M1的漏极电压被钳位在$V_{BIAS}$，导致流经M1输出阻抗的电流不发生变化，也就是输出电压的变化不会导致输出电流的响应，也就形成了无穷大的输出阻抗，当然由于辅助放大器的增益不可能无穷大，所以只是提高了输出阻抗而不是使其无穷大。当输出电压变大时，由于输出阻抗的存在，导致流入M2漏极的电流变大，进而导致M1的漏级电压变大，被辅助放大器的负端提取，然后放大$(-a)$倍输出到M2栅极，使得M2的漏电流变小，进而提到反馈调制的作用，相比普通的cascode有更大的输出阻抗。

<img src="./pic/analog_ic_gray/pic_3.42.png" width=400 alt="pic_3.42">

上图展示了这种结构的小信号等效模型，其中值得注意的是M2的等效模型的跨导$g_{m2}$被放大了$(a+1)$倍，这是由于源极电压也就是M1的漏极电压被放大再被输入到M2栅极导致的：
$$
v_{gs2}=v_{g2}-v_{s2}=v_{g2}-v_{ds1}=-(a)v_{ds1}-v_{ds1}=-(a+1)v_{ds1}
$$
我们可以认为是M2的跨导$g_{m2}$被放大了$(a+1)$倍，那么可以直接代入到上一节中对于cascode的结论中有：
$$
G_m=\frac{i_o}{v_i}\bigg|_{v_o=0}=g_m\left(1-\frac{1}{1+[(a+1)g_{m2}+g_{mb2}]r_{o1}+\frac{r_{o1}}{r_{o2}}}\right)\simeq g_{m1}
$$

$$
R_o=r_{o1}+r_{o2}+[(a+1)g_{m2}+g_{mb2}]r_{o1}r_{o2}\simeq [(a+1)g_{m2}+g_{mb2}]r_{o1}r_{o2}
$$

这个结构最大的问题是在频率上升之后导致的辅助放大器增益下降，会导致输出阻抗也受到影响，更坏的情况可能会导致电路不稳定。对于其更多的内容可以见[辅助放大器(Active-cascode Amp)](#辅助放大器(Active-cascode Amp))

##  Differential Pairs

差分对的实用性源于两个关键性要素：
- 差分对的级联可以直接级联，无需级间耦合电容以实现直流隔离，因为差分对的输出本身具有共模输出
- 差分输入对两个输入的差模敏感，并且可以高度抑制两个输入的共模信号
###  差分对的直流特性
####  bipolar差分对
<img src="./pic/analog_ic_gray/bipolar差分对结构.png" width=300 alt="bipolar差分对结构">

对于bipolar差分对，分析大信号时，假设其尾电流源的阻抗$R_{TAIL}->\infty$，晶体管的输出阻抗$r_o->\infty$，晶体管的基区阻抗$r_b=0$，这些假设对大信号分析的误差并不大，通过KVL在输入环路的分析，以及bipolar的基极-发射极电压和集电极电流关系，还有发射级的KCL：

$-(I_{e1}+I_{e2})=I_{TAIL}=\frac{I_{c1}+I_{c2}}{\alpha_F}$

得到差分输入电压与两个集电极电流的关系：

$$
I_{c1}=\frac{\alpha_FI_{TAIL}}{1+exp(-\frac{V_{id}}{V_T})}
$$

$$
I_{c2}=\frac{\alpha_FI_{TAIL}}{1+exp(\frac{V_{id}}{V_T})}
$$
其中$V_{id}=V_{i1}-V_{i2}$，两个电流与差分输入电压的关系如下图所示

<img src="./pic/analog_ic_gray/发射极耦合对集电极电流与差分输入电压的函数关系.png" width=300 alt="发射极耦合对集电极电流与差分输入电压的函数关系">

可以明显看出来，当$V_{id}>3V_T\approx78mV$时，一个管子关断，电流完全流向另一个管子

进一步定义$V_{o1}=V_{CC}-I_{c1}R_c$和$V_{o2}=V_{CC}-I_{c2}R_C$以及$V_{od}=V_{o1}-V_{o2}$，可得：
$$
V_{od}=\alpha_FI_{TAIL}R_Ctanh(\frac{-V_{id}}{2V_T})
$$
其图像如下图：

<div align=center><img src="./pic/analog_ic_gray/发射器耦合对差分输出电压与差分输入电压的函数关系.png" width=300 alt="发射器耦合对差分输出电压与差分输入电压的函数关系" ></div>

为了提高线性度以及输入范围，可以使用发射极退化手段：

<div align="middle"><img src="./pic/analog_ic_gray/带有发射极退化的发射极耦合对电路图.png" width=400 alt="带有发射极退化的发射极耦合对电路图"></div>

由于电阻上的压降，所以导致晶体管完全关断所需要的差分电压越大，进而导致截断点外推，同时由于尾电流大小不变，导致输出的最大差分电压也是不变的，所以进而导致了在线性工作区的斜率变小。

####  MOS差分对
<div align="middle"><img src="./pic/analog_ic_gray/n 沟道 MOSFET 源耦合对.png" width=400 alt="n 沟道 MOSFET 源耦合对"></div>

对于MOS差分对，大信号分析方法类似，目前同样假设$R_{TAIL}->\infty,r_o->\infty$，这些假设对小信号分析会有很大影响，但对大信号分析无伤大雅。同样在输入的环路列KVL，并且根据MOS的输入特性以及$I_{TAIL}=I_{d1}+I_{d2}$，和$V_{id}=V_{i1}-V_{i2}$，可以得到当时的两边电流与$V_{id}$的关系：
$$
I_{d}=\frac{I_{TAIL}}{2}\pm\frac{k'}{4}\frac{W}{L}V_{id}\sqrt{\frac{4I_{TAIL}}{k'(w/L)}-V_{id}^2}
$$

可以根据这个式子得到差分输入的工作范围，即一边电流为0一边电流为$I_{TAIL}$，有$V_{id}$与$I_{TAIL}$的关系：

$$
|V_{id}|\leq \sqrt{\frac{2I_{TAIL}}{k'(W/L)}}
$$
也可以由在$V_{id}=0$时$I_{d1}=I_{d2}=I_{TAIL}/2$，得到$V_{id}$与$I_{d1}$的关系：
$$
|V_{id}|\leq \sqrt{2}\left (\sqrt{\frac{2I_{d1}}{k'(W/L)}}\right )\bigg |_{V_{id}=0}=\sqrt{2}(V_{ov})|_{V_{id}=0}
$$

<div align="middle"><img src="./pic/analog_ic_gray/MOS差分对的直流转移特性.png" width=400 alt="MOS差分对的直流转移特性"></div>

MOS差分对的直流输出取决于电流，即两个电流的差值:$\Delta I_d$:
$$
\Delta I_d=I_{d1}-I_{d2}=\frac{k'}{2}\frac{W}{L}V_{id}\sqrt{\frac{4I_{TAIL}}{k'(W/L)-V_{id}^2}}
$$
那么也可以得到差分输出电压：
$$
V_{od}=V_{o1}-V_{o2}=V_{DD}-I_{o1}R_D-V_{DD}+I_{d2}R_D=-(\Delta I_d)R_D
$$
那么我们也可以理解差分输出的第一个特性：**差分对的级联可以直接级联**，这是因为当输入的差分电压为0时，在晶体管和电阻匹配的情况下，输出的差分电压也是零，保证了输出的电压平衡，能够以同一个共模输入到下一个差分对，假使一个输出1.2V，一个输出1.7V，那么就需要额外的电容隔离来控制偏置。

###  差分对的交流特性
Gray对差分对的小信号分析可谓细致且系统，具体的分析过程不加以赘述，只挑关键和结论记录，详情见Gray3.5.4-3.5.6

先确定几个增益以及系数便于后续讨论：
$$
差分输入：v_{id}=v_{i1}-v_{i2} \\
共模输入：v_{ic}=\frac{v_{i1}+v_{i2}}{2} \\
差模输出：v_{od}=v_{o1}-v_{o2} \\
共模输出：v_{oc}=\frac{v_{o1}+v_{o2}}{2}
$$
引入四个增益系数：
$$
差模增益：A_{dm}=\frac{v_{od}}{v_{id}}\bigg |_{v_{ic}=0}  表示了单位差模输入引起的差模输出变化 \\
共模增益：A_{cm}=\frac{v_{od}}{v_{ic}}\bigg |_{v_{id}=0}  表示了单位共模输入引起的共模输出变化 \\
差模到共模增益：A_{dm-cm}=\frac{v_{oc}}{v_{id}}\bigg |_{v_{ic}=0}  表示了单位差模输入引起的共模输出变化 \\
共模到差模增益：A_{cm-dm}=\frac{v_{od}}{v_{ic}}\bigg |_{v_{id}=0}  表示了单位共模输入引起的差模输出变化
$$
由上述系数的定义，进而得到两种输出的组合：
$$
v_{od}=A_{dm}v_{id}+A_{cm-dm}v_{ic} \\
v_{oc}=A_{cm}v_{ic}+A_{dm-cm}v_{dm}
$$
在正式讨论小信号前，先进行CMRR的讨论，对于完美对称的差分对，差分输入的影响和共模输入的影响完全隔离，即$A_{dm-cm}$和$A_{cm-dm}$都为0，但$A_{cm}$却不一定为0，故而定义**共模抑制比：CMRR**为：
$$
CMRR=\left |\frac{A_{dm}}{A_{cm}} \right |
$$
有意思的是，这个定义是与拉扎维书中的定义：$CMRR=\left | \frac{A_{dm}}{A_{cm-dm}}\right|$不同的，两位其实都在表达一个意思：期望信号的增益比上不期望信号的增益，只是两位对于不期望信号有所不同，Gray其实也对拉扎维定义的CMRR有所讨论：在并非完美对称的差分对中，$A_{dm-cm}\neq 0,A_{cm-dm}\neq 0$，那么产生了新的比值：$A_{dm}/A_{cm-dm},A_{dm}/A_{dm-cm}$，而前者尤为重要，因为它代表了不期望的共模输入信号产生了差分输出，在多级放大器中，这个比值会比前面定义的CMRR更为重要。

####  完美对称的差分对的小信号分析
作为对称的差分对，即使加上尾电流源的阻抗，也仍然满足半边电路的条件，因为对称，所以两边互补，同时互不影响，也就导致尾电流源上的节点作为虚拟地，下图给出的是bipolar差分对的小信号图，把$r_\pi \to \infty$就可以得到MOS差分对的电路了
<div align="middle"><img src="./pic/analog_ic_gray/图3.55 3.56.png" width=450 alt="图3.55 3.56"></div>
根据电路可以很轻松得到差分增益为：

$$
A_{dm}=\frac{v_{od}}{v_{id}}\bigg |_{v_{ic}=0}=-g_mR
$$
在考虑进管子的输出电阻时，将$R$改为$R||r_o$，同时，MOS的$g_{mb}$可以忽略，因为源极接虚拟地，而衬底接地。

对于共模增益，也可以依据半边电路得到简化，不过此时尾电流源阻抗不能忽略，因为此时尾电流源上的节点会因为共模输入变化同步变化，所以不是虚拟地。
<div align="middle"><img src="./pic/analog_ic_gray/图3.59 3.60.png" width=450 alt="图3.59 3.60"></div>
有：

$$
A_{cm}=\frac{v_{oc}}{v_{ic}}\bigg |_{v_{id}=0}=-G_mR
$$
其中$G_m$是共模输入时的跨导，可以根据电路得知这是一个射极/源极退化的跨导，故而比差分情况下更小，所以$|A_{dm}|>|A_{cm}|$，这也就是之前说的差分放大器的第二个特点：**差分对对差分输入比共模输入更敏感**

##### 对于bipolar差分对
$$
A_{cm}\simeq -\frac{g_mR}{1+g_m(2R_{TAIL})}
$$
如果考虑bipolar的输出阻抗，那么$R$换为$R||R_o$，$R_o$为射极退化的共射放大器的输出阻抗，退化的电阻为$R_E=2R_{TAIL}$

结合前面的差分增益可以得到CMRR：
$$
CMRR=1+2g_mR_{TAIL}
$$
同时可以得到差模和共模情况下的输入阻抗：
$$
R_{id}=\frac{v_{id}}{i_{b}}\bigg |_{v_{ic}=0}=2r_{\pi} \\
R_{ic}=\frac{v_{ic}}{i_b}\bigg |_{v_{id}=0}=r_{\pi}+(\beta _0+1)(2R_{TAIL})
$$
##### 对于MOS差分对
如果考虑衬偏效应，$g_{mb}\neq 0$
$$
A_{cm}\simeq -\frac{g_mR}{1+(g_m+g_{mb})(2R_{TAIL})}
$$
如果计入MOS管的输出阻抗，那么$R$就换为$R||R_o$，其中$R_o$为源极退化的共源放大器的输出阻抗，退化电阻为$R_S=2R_{TAIL}$

结合前面的差分增益可得CMRR：
$CMRR=1+2(g_m+g_{mb})R_{TAIL}$
###  差分对失调
前面提到对于非完美对称的差分对，有：$A_{dm-cm}\neq 0,A_{cm-dm}\neq 0$，而导致失调的因素很多，可以简单列一下以下几个：
1. 晶体管不匹配
   - 阈值电压不匹配：由掺杂浓度不同导致
   - 尺寸不匹配（W/L差异）：导致跨导和输出阻抗不同，以及电流差异
   - 迁移率不同：产生电流差异
2. 负载不匹配
   - 电阻不匹配
   - 有源负载不匹配
3. 工艺与制造偏差
   - 掺杂浓度或氧化层厚度差异：导致器件参数（如$V_{th},\mu,C_{ox}$）漂移，是失调的主要原因
   - 版图布局：不对称的版图会导致器件受到不同的应力，热流，工艺偏差影响
4. 温度因素
   - 热梯度：不同的区域温度会导致晶体管以及其他器件特性漂移
   - 温度系数不匹配：不同器件对温度响应曲线不同导致的失调
5. 噪声与时间漂移
   - 低频噪声（如1/f噪声、burst noise）：低频随机过程导致失调电压在短期内波动
   - 器件老化与电迁移：长时间工作后MOS管的参数变化

由于这些失调的存在，导致哪怕输入的差分信号为0，也会有非零的差分输出，所以引入失调输入信号，在这个信号的补偿下，差分输出回到0.

输入的失调信号如下图(b)所示，它即包含一个和输入串联的失调电压，也包含一个并联的失调电流。在MOS管中只有输入失调电压，而没有电流成分，因为MOS管本身输入电流为零，而bipolar既有输入电压也有输入电流，所以对于bipolar两者都要考虑。
<div align="middle"><img src="./pic/analog_ic_gray/图3.62.png" width=450 alt="图3.62"></div>

对于bipolar和MOS的失调电压电流书上有详细推导，这里直接给结论：

####  对于bipolar：

$$
V_{os}=V_Tln[(\frac{R_{c2}}{R_{c1}})(\frac{A_2}{A_1})(\frac{Q_{B1}(V_{CB})}{Q_{B2}(V_{CB})})]
$$
其中$(V_{CB})$代表基区的电荷是$V_{CB}$的函数，对$R_{c2}R_{c1},A_2A_1,Q_{B1}Q_{B2}$进行差模共模化，在进行ln的近似分析得到：

$$
V_{os}\simeq V_T(-\frac{\Delta R_C}{R_C}-\frac{\Delta A}{A}+\frac{\Delta Q_B}{Q_B})  \\
\simeq V_T(-\frac{\Delta R_C}{R_C}-\frac{\Delta I_s}{I_s})
$$

可以看到三个参数同时影响失调电压，当三个参数同时为一个相位（包含符号），失调情况最严重，不过也可以相互抵消。

对于温度导致的漂移，有经验公式：
$$
\frac{dV_{os}}{dT}=\frac{V_{os}}{T}
$$

对于bipolar的输入失调电流：
$$
I_{os}\simeq -\frac{I_C}{\beta _F}(\frac{\Delta R_C}{R_C}+\frac{\Delta \beta _F}{\beta _F})
$$

####  对于MOS：
$$
V_{os}=\Delta V_t +\frac{(V_{GS}-V_t)}{2}\left (-\frac{\Delta R_L}{R_L}-\frac{\Delta (W/L)}{(W/L)}\right )
$$

对比这个式子与bipolar的式子可以得到一些有用的结论：

MOS失调电压的第一项是有关阈值电压的，这一项在bipolar中是没有的，且其与偏置电流无关，仅受工艺影响，这也限制了MOS管失调的下限，可以导致失调电压比bipolar大一个数量级。

第二项在MOS和bipolar中的类似，但系数不同，bipolar中是$V_T$，MOS中是$V_{ov}/2$，很明显，前者会小于后者至少两倍以上，比如对于bipolar$V_T=26mV$，而MOS的$V_{ov}/2$会达到50mV至500mV。

对于温度漂移，MOS的失调电压的两个部分$\Delta V_t$和$V_{ov}$，前者根据费米能级变化，费米能级随温度上升而下降，故$V_t$具有负温度系数。后者受迁移率变化影响，当温度升高时，迁移率下降，而过驱动电压为了补偿这一部分降低，会随温度升高而上升，具有正温度系数。两者同时作用于$V_{os}$，使得失调电压受温度影响小，当然，如果$\Delta V_t$占比较大，则也会导致失调电压随温度漂移较严重的情况，不过由于是差分结构，只要两边的漂移一致，那么本身就具有一阶的抵消效应。

###  失调差分对的小信号分析
Gary对于这一部分的分析堪称“严酷”，十分系统且详细的介绍了如何分析失调时的小信号，在得到小信号等效电路情况下同时给出了直接的推导，也给出了简化的推导方法，这里不再细讲，直接介绍核心部分。

失调导致的最重要的后果就是$A_{dm-cm}\neq 0,A_{cm-dm}\neq 0$，也就是在分析差模和共模时，共模信号会影响差模输出，而差模信号也会影响共模输出。

对于电阻负载的失调：$\Delta R=R_1-R_2,R=(R_1+R_2)/2$，同时定义电流：$i_d=i_1-i_2,i_c=(i_1+i_2)/2$，得到：
$$
v_d=i_dR+i_c(\Delta R)  \\
v_c=i_cR+\frac{i_d(\Delta R)}{4}
$$
进而得到负载电阻在差模和共模中的等效模型：
<div align="middle"><img src="./pic/analog_ic_gray/图3.64.png" width=450 alt="图3.64"></div>

对于晶体管失调：$\Delta g_m=g_{m1}-g_{m2},g_m=(g_{m1}+g_{m2})/2$，得到电流：
$$
i_d=i_1-i_2=g_{m1}v_1-g_{m2}v_2=g_mv_d+\Delta g_mv_c \\
i_c=(i_1+i_2)/2=(g_{m1}v_1+g_{m2}v_2)/2=g_mv_c+\frac{\Delta g_mv_d}{4}
$$
进而得到受控电流源在差模和共模中的等效模型：
<div align="middle"><img src="./pic/analog_ic_gray/图3.66.png" width=450 alt="图3.66"></div>

结合以上两个等效模型，得到差模和共模的完整等效半边电路：
<div align="middle"><img src="./pic/analog_ic_gray/图3.68.png" width=450 alt="图3.68"></div>

可以根据这个等效电路直接解得小信号增益：
$$
v_{od}=A_{dm}v_{id}+A_{cm-dm}v_{ic} \\
A_{dm}=\frac{v_{od}}{v_{id}}\bigg |_{v_{ic}=0}
=-g_mR+\frac{\Delta g_mr_{TAIL}\frac{\Delta g_m}{2}R-\frac{\Delta g_m}{2}\frac{\Delta R}{2}}{1+2g_mr_{TAIL}} \\
A_{cm-dm}=\frac{v_{od}}{v_{ic}}\bigg |_{v_{id}=0}
=-\left( \frac{g_m\Delta R+\Delta g_mR}{1+2g_mr_{TAIL}}\right)
$$

$$
v_{oc}=A_{cm}v_{ic}+A_{dm-cm}v_{id} \\
A_{cm}=\frac{v_{oc}}{v_{ic}}\bigg |_{v_{id}=0}
=-\left( \frac{g_mR+\frac{\Delta g_m}{2}\frac{\Delta R}{2}}{1+2g_mr_{TAIL}}\right) \\
A_{dm-cm}=\frac{v_{oc}}{v_{id}}\bigg |_{v_{ic}=0}
=-\frac{1}{4}\left[g_m\Delta R+\frac{\Delta g_mR-g_m\Delta R\left(2g_mr_{TAIL}\left(\frac{\Delta g_m}{2g_m} \right)^2 \right)}{1+2g_mr_{TAIL}} \right]
$$
这个结果是精确的，与直接分析整个电路得到的结果一致，不过后者的分析更为复杂。

接下来用一种简化方法分析，这个分析是基于失配本身的性质决定的，因为失配只是平均值的一小部分，那么对于失配发生的部分可以进行简化：
- 共模半边电路中，差模信号控制的失调部分，我们认为其仅受差分信号控制
- 差模半边电路中，共模信号控制的失调部分，我们认为其仅受共模信号控制

听上去很混乱，但结合图就比较好理解了：
<div align="middle"><img src="./pic/analog_ic_gray/图3.69.png" width=450 alt="图3.68"></div>

上图是差模和共模不受失调影响的半边电路，他们分别形成了两份电流$\hat{i}_{Rd},\hat{i}_{Rc}$，将它们分别代入到共模电路中的$i_{Rd}$和差模电路中的$i_{Rc}$

最后得到：
$$
A_{dm}=\frac{v_{od}}{v_{id}}\bigg |_{v_{ic}=0} \simeq-g_mR \\
A_{cm-dm}=\frac{v_{od}}{v_{ic}}\bigg |_{v_{id}=0} \simeq-\left(\frac{g_m\Delta R+\Delta g_mR}{1+2g_mr_{TAIL}} \right)
$$
由上面的两个式子可以看出来$A_{dm}/A_{cm-dm}$几乎正比于$1+2g_mr_{tail}$，且$A_{cm-dm}$与精确计算得到的结果一致，这是因为图 3.68a 中的$g_m$发生器是由纯差分信号控制的。在其他例子中，用这种方法计算的共模-差模增益只能大致正确。
$$
A_{cm}=\frac{v_{oc}}{v_{ic}}\bigg |_{v_{id}=0}\simeq-\frac{g_mR}{1+2g_mr_{tail}} \\
A_{dm-cm}=\frac{v_{oc}}{v_{id}}\bigg |_{v_{ic}=0}\simeq-\frac{1}{4}\left(g_m\Delta R+\frac{\Delta g_mR}{1+2g_mr_{tail}} \right)
$$
通过上面的式子可以看得出来，经由尾电流源输出阻抗的退化，$A_{cm-dm},A_{dm-cm},A_{cm}$都在变小，而当$r_{tail}\to\infty$时，$A_{cm-dm}\to0,A_{cm}\to0$，但同时$A_{dm-cm}$并不会同步趋向0，而是
$$
\lim_{r_{tail}\to\infty}A_{dm-cm}\simeq-\frac{g_m\Delta R}{4}
$$

需要额外说明的一点是，在考虑到两边晶体管的失配以及体效应的失配时，即使$r_{tail}\to\infty$，$A_{cm-dm}$也$\neq0$，这是由于尾电流源上的点被视为源跟随器变化，而体效应的失配导致$g_{mb}\Delta v_{bs}$不同导致$A_{cm-dm}\neq0$。不过$r_{tail}$仍然是重要的参数，它影响了电路对共模信号的敏感性。