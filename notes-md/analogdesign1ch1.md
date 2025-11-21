# Models for Intergrated-Circuit Active Devices
##  MOSFET
###  MOSFET的传输性质
下图为NMOS的结构剖面图

 <img src="./pic/analog_ic_gray/Typicalenhancement-modeNMOSstructure.png" width = "300" height = "200" alt="增强型NMOS截面图" align=center>

 称为增强型是因为在没有在Gate端施加电压时（即$V_{GS}=0$）沟道不导通，沟道需要被*增强*才能导通。

 接下来在衬底（body），源极（source），漏极（drain）都接地时，在栅极（Gate）施加电压，此时栅极（通常由金属或多晶硅）、衬底（p型硅）、介质层（$SiO_2$或high-k材料）形成电容，在栅极施加正压时，衬底的沟道会聚集电子，形成*耗尽层*，如下图所示：

 <img src="./pic/analog_ic_gray/NMOS栅极正压沟道耗尽层形成.png" width="300" alt="NMOS栅极正压沟道耗尽层形成" align=center>

 这个沟道的厚度可以由二极管的耗尽层即空间电荷区公式得到：

$$
X=(\frac{2\epsilon \phi}{qN_A})^{\frac{1}{2}}
$$


 其中$\epsilon$为硅的介电常数，$N_A$为p型衬底的掺杂浓度（假设均匀掺杂），$\phi$为耗尽层中交界处的电势。

 耗尽层的单位面积电荷为：


$$
Q=qN_AX=\sqrt{2qN_A\epsilon \phi}
$$


 当硅界面处的电势达到两倍的费米电势$\phi _f$时，*反型层*出现。
 费米电势（费米能级）被定义为：


$$
\phi _f=\frac{kT}{q}ln[\frac{N_A}{n_i}]
$$


 其中k为玻尔兹曼常数，$n_i$是本征载流子浓度：


$$
n_i=\sqrt{N_cN_v}exp(-\frac{E_g}{2kT})
$$


 其中$E_g$为硅在T=0K时的带隙，$N_c$为导带有效态密度，$N_v$为价带有效态密度。

 费米电势通常为0.3V，在硅表面的电势达到两倍费米电势之后，会在耗尽层的表面积累电子，形成一个电子组成的沟道。这个沟道中的电荷浓度可以用上面的单位面积电荷表示，不过由于耗尽层不再变厚，这个值固定在$Q_b=\sqrt{2qN_A\epsilon 2\phi _f}$。倘若有电压施加在源极和衬底之间，即$V_{SB}>0$，此时衬底的电势小于源极的，需要更大的栅极电压形成反型层，耗尽层的电荷此时为$Q_b=\sqrt{2qN_A\epsilon (2\phi _f+V_{SB})}$。

对于衬偏效应，它是影响晶体管小信号模型的一个重要因素，甚至有时候不正确的偏置会导致严重的漏电问题，以NMOS为例，其源漏级是N型，衬底为P型，假如$V_{SB}>0$，则导致阈值电压上升进而影响晶体管导通和关闭，在小信号上，引入$g_{mb}$作为$v_{bs}$对于阈值电压的影响表现，注意与$g_{mb}$相关的$v_{bs}$，$v_{bs}$的上升导致阈值电压下降，进而认为是漏电流的增加，与$g_m$并联，故也有称衬底为第二栅极的说法；与$V_t$相关的是$V_{SB}$，$V_{SB}$的上升导致阈值电压上升。为了减少体效应对于阈值电压的影响，有时候会用衬底连接源极，使得$V_{SB}=0$，这种情况是衬源二极管零偏，没有电压差和电流产生，在现代工艺中一般芯片都是以P型为衬底，而PMOS的N衬底则需要另外的N-well以形成PMOS，也就是说NMOS的衬底其实都连在一起，如果再连接各个NMOS的源极，会导致每个NMOS的体效应混乱，所以一般NMOS的衬底都连接在地电位，而PMOS由于处于阱中，能够保证衬底之间的隔离，则可以用这种源衬连接的方法。

不过话说回来，并不是所有的源和漏连在一起都是好事，源衬相连的目的是为了减弱体效应的影响，但实际电路还需要具体分析，假如在PMOS中源级和衬底都连在$V_{DD}$，但漏级上升到$V_{DD}\sim2V_{DD}$时（自举效应，可以参考自举开关），会导致漏源颠倒，漏级和衬底正偏产生漏电流，这是所不期望的，所有一般衬底和有源区都是处于零偏和反偏状态。

 将栅源电压形成反型层时的电压称为**阈值电压**，它由三部分组成，第一部分是维持反型层的电荷量$Q_b$；第二部分是栅极金属与硅之间的功函数差$\phi _{ms}$；第三部分是硅和介质层界面处的表面电荷$Q_{ss}$。故阈值电压公式为：


$$
V_t=\phi_{ms}+2\phi_f+\frac{Q_b}{C_{ox}}-\frac{Q_{ss}}{C_{ss}} \\
 =V_{t0}+\gamma(\sqrt{2\phi_f+V_{SB}}-\sqrt{2\phi_f})
$$

 其中$V_{t0}$为无衬偏时的阈值电压，$\gamma$定义为$\frac{1}{C_{ox}}\sqrt{2q\epsilon N_A}$.

 通过调整p型衬底的掺杂可以调整$V_{t0}$的大小，可以调整p型材料的注入使$V_{t0}$控制在0.3~ 1.5V，甚至可以注入n型材料使$V_{t0}$控制在-1~-4V。

 在$V_{GS}$大于$V_{t}$时，在漏源之间施加电压$V_{DS}$，在沟道形成了垂直和水平电场，这就是被称为场效应晶体管的原因。可以根据沟道的电子以及电压电场关系得到漏极电流的公式，推导过程非常简单，不再赘述。其中需要提到的是：从源到漏的电位逐渐升高，这是从漏指向源的电场导致的结果，当漏源电压越大，这个电场越强，电流也就越大。在漏极的电压增大但不超过$V_{GS}-V_{t}$时，始终存在受漏源电压差控制的电场，在这个电压区间，称晶体管工作在三极管区（或者线性区），其电流电压公式如下所示：


$$
I_D=\frac{k'}{2}\frac{W}{L}[2(V_{GS}-V_t)V_{DS}-{V_{DS}}^2]
$$

<div align="middle"><img src="./pic/analog_ic_gray/pic_2.11_razavi.png" width=300 alt="NMOS特性曲线"></div> 

其中$k'=\mu_nC_{ox}=\frac{\mu_n\epsilon _{ox}}{t_{ox}}$，这也就常说的工艺常数，因为这个值常常由工艺决定，当然不同的公式中会有$k$的存在，一般来说$k=k'/2$。

而当漏源电压较小时，上面的公式中$V_{DS}^2$可以忽略，公式退化为：
$$
I_{D}=k'\frac{W}{L}(V_{GS}-V_t)V_{DS}
$$
在这个部分，可以认为抛物线变成了一条直线，如下图所示，

<div align="middle"><img src="./pic/analog_ic_gray/pic_2.12_razavi.png" width=300 alt="NMOS特性曲线"></div>

那么也可以认为这是一个受$V_{GS}$控制的电阻，电流为$I_{D}$，两端的电压为$V_{DS}$，那么有导通电阻：
$$
R_{on}=\frac{1}{\mu_nC_{ox}\frac{W}{L}(V_{GS}-V_t)}
$$
需要注意的是，哪怕源漏没有压差/没有导通电流，也是可以处于导通状态的，这与bipolar不同。

当$V_{DS}$增长时，漏极的电压上升，直到$V_{DS}=V_{GS}-V_t$时，漏极的电压和栅极电压之间形成电势差正好不再形成沟道，这种现象称为**沟道夹断**。随着$V_{DS}$继续升高，这个夹断点从漏极向源极移动，以保证夹断点的电压为$V_{GS}-V_t$。故而用$V_{GS}-V_t$代替$V_{DS}$可以得到饱和区的漏极电流公式，同时如果考虑由于夹断点的移动，加上$V_{DS}$的影响，得到**沟道长度调制效应**调整后的漏极电流公式：


$$
I_D=\frac{k'}{2}\frac{W}{L}(V_{GS}-V_t)^2(1+\lambda V_{DS})
$$


 其中$\lambda=\frac{1}{V_A}$，被称为沟道长度调制系数，$V_A$为厄利电压，$V_A=L_{eff}(\frac{dX_d}{dV_{DS}})^{-1}$，需要提到的是在实际的MOS晶体管中，由于耗尽区的场不是一维的，因此$X_d和V_{DS}$的变化关系极为复杂，所以计算$\lambda$是十分困难的，需要根据实验值确定，它通常与有效沟道长度成反比，与掺杂浓度成反比。

下图给出了NMOS器件的输入转移特性以及输出特性曲线，PMOS中所有的电压和电流极性相反，Gray在他的书中为了防止bipolar晶体管中“饱和区”一词在MOS管中反复使用引起的误解，故他将MOS管的饱和区称为有源区（active region）

<div align="middle"><img src="./pic/analog_ic_gray/NMOS特性.png" width=300 alt="NMOS特性曲线"></div>

#### MOS管的栅源电压组成

$V_{GS}=V_{ov}+V_t$
我们把$V_{ov}$称为过驱动电压，根据square-law可以知道：$V_{ov}=\sqrt{\frac{2I_D}{k'(W/L)}}$，那么过驱动电压受到三个部分影响，一个是漏极电流、一个是工艺参数k'，其中包含了迁移率$\mu$，它随温度升高而降低、一个是设计参数即宽长比。

$V_t$前面已经介绍，这里介绍其受温度的影响：

$$
V_t=\phi_{ms}+2\phi_f+\frac{\sqrt{2qN_A\epsilon (2\phi _f)}}{C_{ox}}-\frac{Q_{ss}}{C_{ss}}
$$

 其中$\phi _{ms},Q_{ss},C_{ox}$与温度无关，而根据之前给出的$\phi _f$的公式，结合本征载流子的公式得到：

$$
\phi _f=\frac{kT}{q}ln\left[\frac{N_Aexp\left(\frac{E_g}{2kT} \right)}{\sqrt{N_cN_v}} \right]
$$

对$V_t$关于T求导，并代回$\phi _f$，得到：

$$
\frac{dV_t}{dT}=-\frac{1}{T}\left[\frac{E_g}{2q}-\phi _f \right]\left[2+\frac{\gamma}{\sqrt{2\phi _f}} \right]
$$

可以得知，当$\phi _f<E_g/(2q)$时，随温度升高，阈值电压降低。

###  MOSFET小信号模型
<div align="middle"><img src="./pic/analog_ic_gray/图1.34.png" width=500 alt="图1.34"></div>

对于这个处于饱和区的基本模型:
$$
g_m=k'\frac{W}{L}(V_{GS}-V_t)=\sqrt{2k'\frac{W}{L}I_D}=\frac{2I_D}{V_{GS}-V_t}=\frac{2I_D}{V_{ov}} \\
r_o=\frac{V_A}{I_D}=\frac{1}{\lambda I_D}\propto \frac{L_{eff}}{I_D} \\
C_{gs}=\frac{2}{3}WLC_{ox}
$$

<div align="middle"><img src="./pic/analog_ic_gray/图1.36.png" width=500 alt="图1.36"></div>

上图给出了更加细致的小信号模型，
$$
g_{mb}=\frac{\partial I_D}{\partial V_{BS}}=-k'\frac{W}{L}(V_{GS}-V_t)(1+\lambda V_{DS})\frac{\partial V_t}{\partial V_{BS}} \\
其中\frac{\partial V_t}{\partial V_{BS}}=-\frac{\gamma}{2\sqrt{2\phi _f+V_{SB}}}=-\chi=-\frac{C_{js}}{C_{ox}} \\
有g_{mb}=\frac{\gamma k'(W/L)(V_{GS}-V_t)}{2\sqrt{2\phi _f+V_{SB}}} \\
\frac{g_{mb}}{g_m}=\frac{\gamma}{2\sqrt{2\phi _f+V_{SB}}}=\chi
$$
$\chi$通常为0.1~0.3，不过也可看到$\chi$的值受到$V_{SB}$的影响
$$
C_{sb}=\frac{C_{sb0}}{\left(1+\frac{V_{SB}}{\psi _0} \right)^{1/2}} \\
C_{db}=\frac{C_{db0}}{\left(1+\frac{V_{DB}}{\psi _0} \right)^{1/2}} \\
当MOS处于三极管区：C_{gd}=C_{gs}=\frac{C_{ox}WL}{2} \\
当MOS处于饱和区：C_{gd}=0,C_{gs}=\frac{2WLC_{ox}}{3}
$$
$C_{gb}$代表着栅极与体极或衬底之间的电容，它模拟的时栅极接触材料与有源器件区域外的衬底之间的寄生氧化物电容，这个电容与栅极-衬底电压无关，这种类型的寄生电容是集成电路上所有多晶硅和金属走线的基础，在模拟和计算高频电路和器件性能时需要考虑在内，其值取决于氧化物厚度，在二氧化硅厚度为100$\AA$时，这个电容为3.45fF。

在源和漏端还有一些寄生电阻，它们源于接触以及扩散区，它们通常反比于沟道宽度W，对于1$\mu m$的W，阻值为50$\Omega$-100$\Omega$，但在手算时，为了简便通常忽略它们，在栅和衬底也有类似的寄生电阻，不过由于在这些端口的电流很小，故可以忽略这些电阻。
### 频率响应
<div align="middle"><img src="./pic/analog_ic_gray/pic_1.37.png" width=500 alt="图1.37"></div>

和bipola一样，定义特征频率(transition frequency)$f_T$，在此频率下，电流增益将为1，虽然MOS管的栅极在低频阻抗无穷大，输入电流为0，但在高频下由于栅漏电容，栅源电容的存在导致小信号电流可以进入，如上图所示的小信号模型所示，由于$v_{ds}=v_{bs}=0$，所以不考虑$g_{mb}.r_o,C_{sb},C_{db}$，故有KCL：
$$
i_i=s(C_{gs}+C_{gb}+C_{gd})v_{gs} \\
i_o\simeq g_mv_{gs}\quad \text{(忽略反馈}C_{gd}\text{的电流)} \\
\frac{i_o}{i_i}\simeq \frac{g_m}{s(C_{gs}+C_{gd}+C_{gb})}
$$
代入$s=j\omega$作为频率响应，同时使结果等于1，得到特征频率：
$$
\omega=\omega_T=\frac{g_m}{C_{gs}+C_{gd}+C_{gb}} \\
f_T=\frac{1}{2\pi}\omega_T=\frac{1}{2\pi}\frac{g_m}{C_{gs}+C_{gb}+C_{gd}}
$$
忽略相比$C_{gs}$较小的$C_{gd}$和$C_{gb}$，代入饱和区的$C_{gs}$和$g_m$关系式:
$$
f_T=\frac{1}{2\pi}\frac{\mu_nC_{ox}(W/L)V_{ov}}{2/3WLC_{ox}}=1.5\frac{\mu_n}{2\pi L^2}V_{ov}
$$
取bipolar特征频率的近似：$f_T=2\frac{\mu_n}{2\pi W_B^2}V_T$，这个结果和MOS是高度相似的，但是可以看出，由于热电压$V_T=26mV$远小于MOS的$V_{ov}$，同时$W_B$对于bipolar是纵向深度的物理量，相比MOS管$L$可以在工艺上可以做的更小，故而bipolar的特征频率是比MOS管大的，当然在短沟道下，平方律的退化会导致特征频率的结果也出现变化，即$f_T\propto L^{-2}$变化为$f_T\propto L^{-1}$，这一点在后面会详细介绍
###  亚阈值
亚阈值区又称弱反型区。阈值电压代表的是栅压达到阈值反型点所需的栅压，此时反型电荷密度等于掺杂浓度，表面势为两倍的费米能级与本征费米能级的势垒高度(以p衬底为例$\psi _s=2\psi _{fp}$)，大于该电压后反型层电荷密度便大于掺杂浓度，称为强反型，此时电压电流关系确实可以用平方律来模拟，但当栅压小于阈值电压时，也不是完全不能导电，此时虽然没有形成强反型层，但载流子仍然可以通过扩散越过势垒进入沟道，故**亚阈值电流为扩散电流**。
<div align="middle"><img src="./pic/analog_ic_gray/图1.1.3各模式势垒.png" width=500 alt="图1.36"></div>

关于亚阈值电流的推导并不重要，这里直接给出结果：
$$
I_D=\frac{W}{L}I_texp\left(\frac{V_{GS}-V_t}{nV_T}\right)\left[1-exp(-\frac{V_{DS}}{V_T})\right] \\
$$
其中$I_t=qXD_nn_{p0}exp\left(\frac{k_2}{V_T}\right)$

$I_t$代表的是当$V_{GS}=V_t$，$W/L=1$，且$V_{DS}\gg V_T$时的漏极电流。

$n=1+\chi=1+C_{js}/C_{ox}$它所代表的是在亚阈值区，栅压对表面势控制为氧化层电容与耗尽区电容的分压，即
$$
\frac{d \psi _s}{d V_{GS}}=\frac{C_{ox}}{C_{js}+C_{ox}}=\frac{1}{n}
$$
对该式子进行求解得到：
$$
\psi _s=\frac{V_{GS}}{n}+k_1
$$
其中$k_1$为常数，需要注意的是上式仅在弱反型区有效，即$V_{GS}>V_t$时这个关系不适用，那么我们可以再进行变形：
$$
\psi _s=\frac{V_{GS}-V_t}{n}+k_2
$$
其中$k_2=k_1+V_t/n$

可以通过式子看出，当$V_{DS}>3V_T$时，电流的最后一项趋于1，这与饱和区的MOS管不同，后者需要MOS管工作为电流源的漏源电压取决于过驱动电压，而前者则为固定的值，同时公式也表明当栅源电压小于阈值电压漏电流不为零，如下图所示：
<div align="middle"><img src="./pic/analog_ic_gray/图1.43.png" width=400 alt="图1.43"></div>