# 采样保持 Sample and Hold

## 采样定理

为了防止混叠，采样频率：
$$
f_s>2\cdot f_{signal}
$$
采样频率$f_s=2\cdot f_{signal}$被称为奈奎斯特频率，这种ADC也称为奈奎斯特ADC

> 还有一种过采样ADC，其采样频率远大于两倍信号频率

两中可行的方法：

- 让采样频率经可能宽
- 增加抗混叠滤波器，即滤除两倍期望信号频率以上的信号

## 混叠

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_1.png" style="zoom:60%;" />

如图，采样频率为1000kHz，其奈奎斯特频率为500kHz，远大于信号频率101kHz，在其周期内大概取10个点，对于输入的正弦波信号（蓝线），其采样结果为对时间t进行离散化得到的黑点。

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_2.png" style="zoom:60%;" />

保持采样频率不变，输入信号频率提升至899kHz，很明显不满足采样定理，如果将时间变量离散化取值，可以发现经过恒等变换，899kHz的采样和101kHz的采样时一样的，即上一张图的采样效果，这是时域上的混叠现象。

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_3.png" style="zoom:60%;" />

当输入信号频率再上升至1101kHz，而采样频率不变，可以发现采样后的信号仍然是和101kHz输入信号的采样一样。

综上，对于1000kHz的采样频率，输入频率101kHz，899kHz和1101kHz的采样结果一致，也就是高频成分和低频混叠，导致采样的信号无法区分低频高频，这种采样虽然不直接对SNR和THD产生影响，但高频的信号混叠也会导致高频的噪声混叠，进而影响SNR等性能。

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_4.png" style="zoom:60%;" />

混叠导致$N\cdot f_s \pm f_{sig}$在离散时间域上无法区分，除了将高频成分混叠回低频，也会将高频附近的噪声信号混叠至低频。

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_5.png" style="zoom:60%;" />

抗混叠滤波器：将$f_s/2$以外的信号全部滤除，使得高频的信号和噪声无法混叠。

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_6.png" style="zoom:60%;" />

实际滤波器不可能极其陡峭的进行滤波，过高阶的滤波器其会包含更多的运放，导致噪声的增加。实际的抗混叠滤波器在频率上提前衰减，假设期望采样输入信号频率为$B$，可以使得滤波器在$B$开始衰减，在$f_s-B$的部分已经进行了一定程度的削弱，其采样混叠回到频带内的影响也就有一定减弱，而在$f_s/2-B$范围内的信号则可以在数字域使用数字滤波器完全滤除。

之前在计算SNR中使用的理想公式为$SNR=6.02\cdot N+1.76dB$，其噪声信号的积分区间位于$[0,f_s/2]$之间，而数字滤波去除了$(B,f_s/2)$之间的噪声信号（包括量化噪声），这种过采样操作使得SNR有一定的提升：
$$
SNR=6.02\cdot N+1.76dB+10log\frac{f_s}{2\cdot BW}
$$
这一部分增益需要两部分才能存在：

1. 过采样操作
2. 数字滤波器

> 过采样指以明显高于奈奎斯特速率的采样频率对信号进行采样。过采样率：$OSR=\frac{f_s}{2\cdot BW}$

## 欠采样

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_7.png" style="zoom:60%;" />

在目标频率附近加入带通滤波器，经过采样之后将带通内的信号搬回奈奎斯特频率内。

## 采样保持电路

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_8.png" style="zoom:40%;" />

理想的采样保持电路：零建立时间，无限大带宽。实际的采样保持电路：一半周期用于建立（跟随），另一半用于ADC处理，带宽有限。

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_9.png" style="zoom:40%;" />

使用MOS管作为开关，以NMOS为例，时钟信号为1进行采样，为0断开，有以下问题：

1. MOS管导通电阻与输入信号有关，使得带宽与输入信号有关(signal-dependent)
2. 电荷注入：沟道电荷注入(channel charge)，时钟馈通(clock feedthrough)
3. 孔径误差：时钟变化行为与实际开关关断存在误差(aperture)

采样带宽：

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_10.png" style="zoom:60%;" />

由RC电路可得$v_o=v_i(1-e^{-\frac{t}{\tau}})$，其中$\tau=R_{on}C_s$，如果$R_{on}$趋于0，则带宽无限大，使得电路理想采样。

实际上$R_{on}$随着输入信号发生变化，导致采样出现扰动。

实际上哪怕电阻恒定也会有误差：dispersion

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_11.png" style="zoom:60%;" />

RC网络会带来相移，对于不同频率的信号增加的相移也不同，使得信号出现失真：

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_12.png" style="zoom:60%;" />

使用CMOS减小对于输入信号的依赖，虽然也有小的失真，但只要带宽够大，相移失真的影响就减小了。

> 虽然电路简单，但在高频中简单的电路引入的失调和噪声等误差更小。

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_13.png" style="zoom:60%;" />

理想采样保持：

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_14.png" style="zoom:60%;" />

无跟随误差，无孔径误差，无跟随、保持失调误差。

### 采样保持误差分析

实际采样保持电路：

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_15.png" style="zoom:60%;" />

$\delta_1$：跟随误差：有限带宽导致跟随信号无法完全贴合输入信号

$\delta_2$：保持误差，由于电流泄露等原因导致保持阶段的误差

$\delta_3$：转换误差，由于aperture孔径误差，如MOS管中在$V_{GS}$下降到$V_{in}-V_{th}$才关断的误差，以及时钟抖动，clock jitter引入的误差，此外还有电荷注入和时钟馈通

#### 采样跟随误差$\delta_1$分析：

捕获时间(Acquisition time $t_{acq}$)

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_16.png" style="zoom:60%;" />

在不同的精度要求下，所需要的捕获时间$t_{acq}$可以根据RC延时得到与$\tau$的关系，越高的精度需要的捕获时间越长，假设捕获时间固定为$T_s/2$，那么所要求的$\tau$也就越小，要求采样电路的带宽越大。其与$\delta_1$有关。

导通电阻与沟道长度和沟道电荷有关，小的导通电阻需要短的沟道长度，薄的介质层，大的沟道宽度和大的过驱动电压以及小的$V_i$。

#### 保持误差$\delta_2$分析：

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_24.png" style="zoom:60%;" />

由于漏电导致保持阶段的电压下降，使得电压不稳定，在先进工艺中漏电明显，可以使用IO端口，其沟道长度较大。

#### T/H转换误差$\delta_3$分析：

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_17.png" style="zoom:60%;" />

在转换过程中存在误差：

1. pedestal error:与输入信号有关，包含电荷注入和时钟馈通
2. aperture delay:关断信号指令与实际关断完成的误差
3. aperture jitter:时钟抖动

##### pedestal error

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_18.png" style="zoom:60%;" />

1. 时钟馈通，时钟关断通过寄生电容将额外电荷进行注入
2. 电荷注入，MOS管的强反型沟道在关断后的电荷注入

电荷注入(Charge injection,CI):在快速关断时，认为注入到输出的电压为$\Delta V=\frac{Q_{ch}}{2C_s}$，这个关系假设沟道电荷均分向两边注入，软件仿真也是按照这个关系，但实际情况是按照两边阻抗决定注入量。在慢关断时，由于注入速度慢，同时管子一直打开，使得输出仍然跟随输入，故而减小了注入的影响。

时钟馈通(Clock feedthrough):在快速断开时，是关于$V_{DD}$在管子的寄生电容和输出电容的分压，由于开关管尺寸一般较大，所以误差会存在，但由于与输入无关，可以认为是一个offset。在慢关断时，当$\Phi$降到$V_{in}+V_{th}$时管子才会关断，此时的电压再经过两个电容分压，虽然这个值比快关断时的误差小，但它和输入信号有关。

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_19.png" style="zoom:60%;" />

同时考虑两种误差时，可以发现无论快速关断还是满速关断都有和输入有关的误差项。

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_20.png" style="zoom:60%;" />

考虑快速关断的沟道电荷注入误差作为平台误差，将其与带宽TBW相比得到一个FoM值，可以发现其与工艺有关，越先进的工艺尺寸越小，误差和速度比值也就越小。

##### 孔径抖动 Aperture jitter

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_21.png" style="zoom:60%;" />

时钟抖动导致模式转换的抖动，导致保持的信号也有抖动$\Delta V$，进而影响SNR。SNR在其中收到两部分影响，一部分是$\delta t$，一部分是输入信号的频率$f_s$，频率速度越快，造成的$\Delta V$越大，进而SNR越差。推导如下：

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_22.png" style="zoom:60%;" />

可以绘制有关的图线：

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_23.png" style="zoom:60%;" />

例如对于一个输入信号频率为10MHz，要求其SNR65dB，也就是相当于11bit位数，那么就需要时钟抖动在10ps之内。

#### kT/C噪声

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_25.png" style="zoom:60%;" />

#### 小结与SNDR

除了之前的误差，还有$kT/C_s$积分噪声误差，不过实际上这是一个相对比较小的误差，比如1.2V的参考电压，12bit的ADC，其LSB约为200uV，对于1pF的$C_s$绰绰有余了，但一旦需要噪声小十倍，则需要电容大100倍。实际上电容的数值选取一般取决于之前提及的种种误差。

综上有四种误差：

1. 跟随误差
2. 转换误差
3. 保持误差
4. 积分噪声

综合的SNDR如下式：
$$
SNDR=\frac{\overline{V_i^2}}{\overline{V_N^2}+\frac{A^2\omega ^2}{2}\overline{\delta^2}+\overline{V_{\epsilon}^2}}
$$
其中$\overline{V_i^2}$主要由$kT/C$决定，第二部分由时钟抖动决定，第三部分在track阶段主要是导通电阻和带宽的变化，转换时有电荷注入和时钟馈通以及时钟SR/输入BW限制，在保持阶段存在漏电和AC电源耦合，其中比较重要的误差项是$\overline{V_{\epsilon}^2}$。

### MOS S/H 技术

#### 顶极板采样

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_26.png" style="zoom:60%;" />

最简单的顶板采样，优势是结构简单，速度快。缺点是带宽与输入有关，存在CI和CF，以及输入依赖的平台延迟：

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_27.png" style="zoom:60%;" />

由下式推导可以看到信号和distortion的比SDR与时钟SR平方成正比，与输入信号幅值平方和频率平方成反比。

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_28.png" style="zoom:60%;" />

CMOS开关管

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_29.png" style="zoom:60%;" />

互补管减小了导通阻抗受输入信号的影响，进而优化BW，同时由于时钟互补，使得时钟馈通CF也有所改善，不过阻抗仍然受输入信号影响，且在先进工艺更明显。

#### Clock Bootstrapping

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_30.png" style="zoom:60%;" />

通过在栅源之间加入一个恒定的电压(如$V_{DD}$)，使得导通电阻保持不变，栅极电压被这个恒定电压自举到$V_{in}+V_{DD}$。可以不受一阶效应影响。

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_31.png" style="zoom:60%;" />

一个早期的自举开关电路，左边红框是一个电荷泵，关于其分析可以见[DRAM充电泵结构笔记]，它在这里的作用是在$\Phi=1$时提供$2V_{DD}$用于导通其驱动的NMOS，所以先忽略。输入从M1的一端加入，在另一端输出，输出点接一个输出负载电容，充电阶段给电容$C$充电$V_{DD}$，自举阶段通过传输门和M2对AB两个点产生一个$V_{DD}$的电压形成自举。中间的三个管子用于控制M2的开关。

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_32.png" style="zoom:60%;" />

上图为时钟信号为低时的情况$\Phi=0,\overline{\Phi}=1$，电源对电容$C$进行充电，M2栅端的PMOS导通，输入$V_{DD}$给M2栅极使其关断，M3导通使得M1栅极接地，导致M1关断，不进行采样。

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_33.png" style="zoom:60%;" />

上图是时钟信号为高时的情况$\Phi=1,\overline{\Phi}=0$，$V_{in}$经过传输门到$C$下面使得$C$上方抬升至$V_{in}+V_{DD}$，同时M2栅极也是$V_{in}$，其比$C$上端低$V_{DD}$，使$V_{in}+V_{DD}$传输至M1栅端产生自举。

现在来分析这个电路的一些细节和改进

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_34.png" style="zoom:60%;" />

对于M6使用PMOS，可以不用像NMOS一样需要一个自举的charge pump来驱动来传递$V_{DD}$，这个PMOS的作用是：1，使得电容充电到VDD，2，电容自举之后不会漏电。对于后者，当源极在VDD侧，体二极管使得C上方的电压上升时漏电至VDD，导致最大值钳位(clamp)为$V_{DD}+V_{diode}$。

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_35.png" style="zoom:60%;" />

关于图中下方使用的传输门，可以替换为一个栅极接到M1自举点的NMOS，进而也能实现自举开关使得$V_{in}$传给C，减少了管子数量，但这种方案电容C需要同时驱动M1和这个自举NMOS，而传输门方案是由时钟信号驱动传输门，受到寄生效果较小。

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_36.png" style="zoom:60%;" />

M4用于保护M3，M3在自举M1的过程中，其栅源为0，漏级最高可以达到$2V_{DD}$，存在击穿风险（哪怕不击穿也有TDDB和reliability问题），加入M4后，在M1自举阶段进行分压，使得M3漏极最高到$V_{DD}-V_{th}$，减小击穿风险，在充电C时，无损传输0至M1，不影响正常工作。

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_37.png" style="zoom:60%;" />

改进后的自举开关如上图，第一点采用了上文说的NMOS取代传输门，第二点用PMOS作为从$V_{DD}$向电容C充电的管子（注意衬底接法），第三点用NMOS替代M2的启动管，即图中的M5，其与M3互补对M6驱动，当Vin一开始较小时M3导通使Vin驱动M6栅极，当Vin趋近VDD，M3关断，同时M7栅端也自举到约为2VDD，使得M5打开继续传递Vin给M6栅极用于驱动。

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_38.png" style="zoom:60%;" />

图中蓝色部分表示寄生电容，由于这些电容存在导致Ms的栅极很难到$V_{DD}+V_{in}$，假设这些寄生电容的和为$C_{p}$，那么可以认为寄生电容产生了分压，输出的$V_x=\frac{C_b}{C_b+C_p}(V_{in}+V_{DD})$。

此外Ms的栅端从开启的$V_{in}+V_{DD}$跳变到0时会产生馈通效应，导致输出电压的变化。沟道电荷注入由于自举结构，其注入与输入无关，且可以通过dummy和差分减小。

第三个误差是Ms的衬偏效应。如下图所示，由于衬底接地，源极升高存在衬偏，使得阈值电压变化，进而导致导通电阻随着输入变化，故引入高阶的误差。

![](E:\personal-site\notes-md\pic\ADC\ADC2_39.png)

可以通过深N阱工艺实现这个管子的衬源相接消除衬偏效应。需要注意使用Back gate switch，在采样期间使$V_{BS}=0$，以消除衬偏效应，保持期间使$V_{B}=0$，以消除体二极管，此外还需要注意这种工艺的寄生电容，可以通过Deepwell的floating使得寄生电容串联实现减小。

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_40.png" style="zoom:60%;" />

#### Dummy Switch与全差分采样

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_41.png" style="zoom:60%;" />

在开关关断时，沟道电荷进行注入，假设向负载电容传输一半电荷，在输出与负载之间加一个dummy管其尺寸为一半且控制开关相反，其沟道电荷吸收电荷为$Q_{ch}/2$，此外也能减弱一定的时钟馈通。也可以配合差分结构进一步优化性能。实际上dummy管的反时钟信号会略晚于开关管的时钟信号。

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_42.png" style="zoom:60%;" />

通过全差分操作进行采样，抑制直流分量和偶数次谐波。

#### 底极板采样 Bottom-Plate Sampling

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_43.png" style="zoom:60%;" />

原本的顶极板采样由于开关动作和输入之间联系导致存在孔径误差等误差，底极板采样引入一个底板与地相连的MOS，该MOS提前于输入开关关断，使得Cs floating，进而使得CF和CI不对Cs在一阶上产生影响。

进一步可以引入全差分，以及自举开关可以进一步优化带宽和误差。可以在X节点加入dummy优化CI。

### 采样保持放大器 Sample-and-Hold Amplifier SHA

1. 单端转差分
2. 放大(幅值放大，MDAC余量放大)
3. 驱动(输入阻抗很大的情况H-Z，需要放大器进行阻抗匹配)

反相SHA

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_44.png" style="zoom:60%;" />

跟随阶段：

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_45.png" style="zoom:60%;" />

使用底极板采样技术，中间$\Phi_{1e}$控制的MOS管可以分为两个长度减半的MOS管串联，中间结点可以认为是ACground，采样在电容$C_s$上面，同时由于差分结构使得$\Phi_{1e}$的CF和CI被取消。

保持阶段

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_46.png" style="zoom:60%;" />

$\Phi_2=1$，使$C_s$左端接ACground，对保持电容$C_H$进行放电得到输出电压。

优点：可以单端转差分；共模电平转换

缺点：信号增益为1，放大反馈系数在$C_s=C_H$时为1/2，即增益为2，导致噪声恶化。

非反相SHA

<img src="E:\personal-site\notes-md\pic\ADC\ADC2_47.png" style="zoom:60%;" />

信号增益和放大增益都是1，噪声性能较好。