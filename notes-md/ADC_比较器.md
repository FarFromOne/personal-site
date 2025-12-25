# 比较器

## 基础架构与指标

低于阈值电压输出0，高于阈值电压输出1，对于一些比较器会存在时钟控制信号

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_1.png" style="zoom:50%;" />

应用场景：

- 电压电流比较（A/D转换）
- 数字通信接收：用于对于接口和使能信号的比较处理，分为CMOS和TTL，前者和电源电压有关，后者为固定阈值
- 存储读出电路的传感器
- 数字控制电源(DCDC，位于control回路中使用连续时间comparator)

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_2.png" style="zoom:40%;" />

### 指标

- 精度：失调，噪声，分辨率类似于放大器
- 建立时间：由于比较器工作在大信号，所以相比运放对于小信号速度的BW，比较器的速度用建立时间表示，同时包括SR和BW
- 敏感度：增益
- 亚稳态：对于clock控制比较器存在的，有限的时间内不能输出翻转准确电平，对于async异步电路使用比较器输出作为时钟而言更加致命
- 过驱动恢复：完全关断会导致再次翻转输出很慢
- CMRR
- 输入电容和输入电容线性度：影响Gain Error，非线性度影响更加严重
- Kickback Noise：输出耦合回输入使输出再次翻转进而产生噪声
- 功耗



<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_3.png" style="zoom:45%;" />

增益与速度权衡

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_4.png" style="zoom:60%;" />

对于一个14-bit的ADC，假设电源电压1.8V，满量程1.2V，LSB为73.2uV，比较器至少需要把二分之一的LSB转换为轨到轨的输出，那么增益为$1.8V/73.2uV/2=49180=93.8dB$，对于一个需要二分之一的采样周期的时间用于建立，对于采样速度为10MHz，那么一半的周期时间为50ns，则需要的3dB带宽为$200MHz$。

对于单级的运放，极大的3dB带宽则要求输出电阻小，高增益则要求输入管跨导极大，则需要过高的功耗，显然是不适合的设计

可以通过多级结构实现高带宽和高增益，部分电路负责高带宽、部分负责高增益。如下图所示，使用预放大器和latch结构复合实现比较器。

### 架构分析

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_5.png" style="zoom:60%;" />

使用pre-amp+latch结构（同时也是一个1-bitADC）自身在reg过程中就存在采样功能

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_6.png" style="zoom:50%;" />

多级级联的放大器，比较器工作在开环且不需要补偿，越多级数则增益越大，但同时3dB带宽也在下降

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_7.png" style="zoom:50%;" />

根据阶跃响应，在响应时间较小时可以认为是一阶关系，多级则表现为N阶乘分之一和N次方乘积关系，关键在于如何取合适的N使得转移关系$V_N/V_{in}$最大。

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_8.png" style="zoom:50%;" />

根据下图可知，在固定的增益下，级数在2~4之间有着最小的传输延时，关于N的选择为：

1. N固定在2~4
2. 根据设计需求得到LSB，根据Latch得到其输入噪声和失调
3. 根据$Latch/LSB=A$得到增益需求来选择级数

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_9.png" style="zoom:45%;" />

下图展示的是不同级数下增益和所需时间的关系，同时加入了latch的曲线，可以看到latch的速度是明显快于pre-amp的，需要注意的是横坐标增益是对数，如果换为线性坐标类似右下角，在输入信号较小时pre-amp较快，在信号已经放大较大时latch更快，这也是为什么要两者级联的原因。

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_10.png" style="zoom:40%;" />

主体结构如下。预放大器的用处，加快小信号的响应，减小输入失调（latch的失调较大），减小回踢噪声，减弱亚稳态。

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_11.png" style="zoom:45%;" />

## 亚稳态

量化亚稳态：亚稳态即不能在规定时间输出到规定值。根据latch的转移关系;$v_o=v_{in}e^{t/\tau}$，可以得到在输出电源电压，转移时间最大时的最小输入电压，进而得到预放大器的最小输入电压，将这个最小输入电压与输入的满摆幅相比可以得到一个概率$P_{error}$，而在整体的ADC中，这个比较器输入则是一个LSB，即在一个LSB的电压输入中，小于这个最小预输入电压$V_{pre\_min}$则会出现亚稳态。

图中右下角给出例子对于一个6bit，采样频率500MHz的ADC，比较器带宽5GHz，预放大器增益为3，满摆幅为0.5倍电源电压，最后得到出错概率$P_{error}=10^{-12}$，如果一直工作则预计会在33分钟出错。

避免亚稳态可以通过

1. 添加预放大器，或使预放大器增益变大
2. 后续增加反相器以消除亚稳态

一般而言出现在async异步ADC中。

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_12.png" style="zoom:45%;" />

## 失调

多级的pre-amp的失调如下图所示，

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_13.png" style="zoom:45%;" />

为了进一步减小失调电压，有Input offset cancellation :IOS和Output offset cancellation :OOS

### 输入失调消除

下图展示的是IOS：输入通过电容耦合到比较器，

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_14.png" style="zoom:45%;" />

在$\Phi_2$时采样失调电压到电容上

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_15.png" style="zoom:50%;" />

在$\Phi_1$时采样输入，同时存储的失调与实际失调相减，得到等效后的失调电压$\frac{V_{os}}{1+A}$。如果增益足够大则失调越小，但不能完全消除失调，且输入是AC耦合

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_16.png" style="zoom:50%;" />

由于采样失调也会引入CI和CF，所以可以采用底极板采用，dummy管等技术来减小采样的误差。

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_17.png" style="zoom:45%;" />

### 输出失调消除

输出失调矫正 OOS：输出信号AC耦合

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_18.png" style="zoom:45%;" />

在$\Phi_2$阶段存储失调电压在输出端电容上，这样由于采样的CI，CF误差折算到输入时会除以增益系数，此外不需要闭环稳定性问题。但由于失调也被放大A倍，可能会出现饱和问题所以增益不能太大。

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_21.png" style="zoom:45%;" />

在$\Phi_1$阶段输入的失调会与存储的相消，使得失调消去。

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_20.png" style="zoom:40%;" />

优点：能够真正的消除输入失调；能够将CI、CF减小A倍。

缺点：增益不能太大，会导致输出饱和

下图展示的是OOS同时消除pre-amp和latch的offset的电路图

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_22.png" style="zoom:50%;" />

失调采样：S5/S6闭合，Latch的正反馈回路切断，输入失调$V_{os2}$被采样到C1/C2上；S3/S4闭合，使$V_{os1}$被采样到C1/C2上；此外S5/S6相比S3/S4稍微早些断开，使C1/C2实现底极板采样，以及S5/S6由于在输出侧，使得CI/CF等效到输入时变小。

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_23.png" style="zoom:45%;" />

比较阶段，S3/S4/S5/S6断开，latch正反馈工作，S1/S2闭合，输入进入电路正常工作。

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_24.png" style="zoom:45%;" />

存在的问题：

1. 正反馈回路存在电容，使得转换速率变慢，同时也作为输出端的负载，使得速度变慢
2. S5/S6闭合时阻抗不够低导致正反馈回路切断不完全使得输出饱和
3. S5/S6的不对称使得CF/CI不对称导致regenerate过程使得latch受不对称信号控制被overwrite输出

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_25.png" style="zoom:60%;" />

改进电路：在正反馈回路添加一个运放（可以用跟随器代替），使得信号只能单向流通，输出端看辅助放大器的输入端阻抗大不会影响负载，进而消去C1/C2的负载效应，同时CF/CI由于辅助运放的隔离也被抑制到输出的贡献。

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_26.png" style="zoom:60%;" />

## 过驱动恢复 overdrive recovery

前一次的输入输出应不影响后一次的输入输出——memoryless，假设前一次是满幅输入，下一次是一个小跳变（$\pm 1/2LSB$），那输出从满输出回到共模的过程应不影响下一次的检测（如过冲等效应），需要通过reset来重置比较器状态。

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_27.png" style="zoom:60%;" />

无源钳位：使用两个二极管连接的MOS使一端的输出仅会比另一端高/低一个$V_{diode}$，使得输出摆幅不会特别大，但钳位二极管会使得寄生电容添加在输出端，同时由于是两个二极管相反并联，输出阻抗会受两端输出电压影响

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_28.png" style="zoom:60%;" />

有源重置：M5受时钟信号控制，为高时导通短接输出起到重置，但会随着时间使两端输出靠近时，导致电阻逐渐变大，使得导通变慢，此外也存在寄生电容影响输出负载

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_29.png" style="zoom:60%;" />

重置+autozero：在$\Phi_2'=1$时，输出输入短接， 两端输出相差极小（约为$V_{os}$），同时以IOS消除offset

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_30.png" style="zoom:60%;" />

综上三种的消除记忆效应：

1. clamp钳位二极管
2. reset管
3. Autozero开关连接$V_{cm}$

## CMOS pre-amp

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_31.png" style="zoom:60%;" />

使用NMOS作为Pull-Up负载，会受到体效应影响，可以使用Deep-Nwell

使用PMOS不受体效应影响，但受工艺角影响较大

使用电阻速度较快（寄生电容小），但会导致增益受工艺、温度等条件影响较大

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_32.png" style="zoom:60%;" />



通过抽取一部分电流以提供更高的增益：恒流源在小信号时视为开路，M3/M4偏置电流较小，gm也较小，作为负载提供更大增益

在相同电流下提供更高增益，且不需要共模反馈，需要额外的偏置对$I_p$；在使用output offset cancel时可以通过这种方法控制负载实现增益的调控

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_33.png" style="zoom:60%;" />

使用正反馈（交叉耦合）提高增益，速度较快，较高的差模增益，较低的共模增益，无需共模反馈，同时需要保证M3M4尺寸大于M5M6以确保负反馈大于正反馈控制电路稳定放大能力，电路同时存在迟滞现象

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_34.png" style="zoom:40%;" />

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_35.png" style="zoom:40%;" />

> 实际上考虑mismatch的CMRR会比计算CMRR的情况恶化很多

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_36.png" style="zoom:60%;" />

引入电阻作为M3M4的偏置以及负载，不需要共模反馈，CMRR较好，但电阻作为负载受条件影响较大，使得增益不稳定

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_37.png" style="zoom:60%;" />

## Latch

### 静态latch

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_38.png" style="zoom:60%;" />

中间两个交叉耦合形成两个反相器首尾相连，在regenerate形成之前电流很大，所以工作速度很快，同时regenerate输出轨到轨，此时没有DC电流，但会产生较大噪声；reset中电流很大，且没有明确的reset电平

关于offset：输入管的尺寸失调（Vth失调），输出负载寄生电容影响，反相器尺寸失调。关于输出负载寄生电容不匹配：在regenerate过程中，电流导通向两个反相器，由于电容失配导致充电速度不同，当一边达到反相器启动阈值时，由反相器开始代替充电进行正反馈输出。

### 半动态latch

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_39.png" style="zoom:60%;" />

上一个电路由于重置时电流导通，输出节点电压位于中间值，使得reset电流过大，但同时regenerate速度也够快，该半动态latch在reset时断开M8使得电流关断，几乎没有静态电流，同时reset输出电压为0，但因电压拉低导致regenerate速度慢

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_40.png" style="zoom:60%;" />

上一个电路由于reset时没有电流导致regenerate时较慢，这个电路中添加一个恒定电流，保证一直有DC电流存在，使速度较快，左边的pre-amp能提供一定增益，同时由于流经电源的电流恒定可以避免噪声，但输出不能达到轨到轨，需要再加一级latch（直接连接反相器会增加静态电流）

### 动态latch

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_41.png" style="zoom:60%;" />

reset时所有节点重置为电源电压，regenerate时导通M9M10，由输入管M1M2进行抽电流，根据输入电压的大小决定输出节点PY的下降速度，先下降到反相器阈值（M5或M6导通）的进入正反馈回路进行输出电压生成，综上在reset阶段无电流，且在期间输出有明确的电压（VDD），同时能够做到轨到轨输出，但速度较慢，具体取决于输入电压差分的大小

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_42.png" style="zoom:40%;" />

上图所示的调整版动态latch调整了反相器输入端的位置，即两个MOS管栅极连接点跨过了M9M10，其和上一个电路一样在reset阶段没有DC电流，同时每个节点都有确定的电压（M9M10以上为VDD，以下为0），M1M2工作在线性区，根据输入电压大小控制M1M2的线性区电阻决定充电快慢，输出满足轨到轨，但同样由于从reset到regenerate的充电放电过程导致速度较慢

其中的offset来源于节点的寄生电容，以及M1M2的失配

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_43.png" style="zoom:60%;" />

添加的M1R和M2R作为比较器的阈值调整管，下面四个NMOS均工作在线性区，根据电流相等时的情况（或并联导纳）可以得到开启比较器的阈值电压。此外还可以通过这两个管子的电流来实现对于输入管M1M2的失调修正（另一种补正失调的方法是控制负载电容）。

### 双尾电流动态latch

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_44.png" style="zoom:60%;" />

分为了两级构成的latch，在reset阶段CLK=0，M3M4导通使Di+和Di-拉往VDD，M8M9导通使得输出拉地。CLK=1时，M5导通，M3M4关断，使得M1M2将Di+Di-节点从VDD往地拉低，根据输入差分值的大小拉低速度不同，M8M9关断出现先后，先关断的使对应输出级被上拉网络充电至VDD进入正反馈生成轨到轨输出。

由于分为了两级，所以可以工作在较低电源电压下，M1M2有一定的预放大能力加快速度，此外有较好抵抗kickback噪声能力：由于输出的轨到轨输出经过M8M1再到输入所以影响较小，且输入同向（都是降低至地），所以kickback影响也较小。

### Strong ARM latch

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_45.png" style="zoom:60%;" />

用S1S2在reset阶段将PQ进行重置至VDD，使M1M2在regenerate有一定预放大能力，S3S4对XY在reset进行重置至VDD，使输出有明确值，offset主要由M1M2控制，由于XYPQ的预充电，所以M3M4M5M6关断，它们的offset对输出影响变小

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_46.png" style="zoom:60%;" />

上图展示了一种比较器的噪声仿真方法，原先的噪声仿真方法基于PSS+Pnose，速度较慢；这种方法在不考虑offset时仿真trannose检查输出，可以看到各占一半正负值，加入一个$Vs$之后输出的高低有概率便偏移，通过高斯分布的$\delta$和输入电压值可以得到噪声的积分和P-P值

### 自校准

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_47.png" style="zoom:60%;" />

校准主要通过控制电容C和电流I来实现冲放电一致，上图的自校准引入一个Charge Pump，通过比较输出值和校准的值控制电荷泵对Mc2进行冲放电，使得电流平衡。

<img src="E:\personal-site\assets\pic\ADC\ADC_comparator\ADC3_48.png" style="zoom:60%;" />

和上一个电路的不同点使在输入管下方加入了offset采样电路，在reset阶段，使$\Phi_1=1$，输入共模信号，下方的两个电容对输入管的阈值失调进行采样：$V_{cm}-V_{th1,2}$，在$\Phi_2=1$时输入差模信号，之后$\Phi_L=1$，M5导通，M3M4关断，开始正常工作，由于之前电容对阈值进行了采样，此时就消除了阈值失调的误差量。