# Current Mirros,Active Loads,and References
##  Current Mirrors
电流镜的理念就不赘述了，这里简单介绍以下理想电流镜的特征：
 - 输出电流是输入电流精确乘电流增益，这个增益不受输入频率影响
 - 输出电流不受输出电压的影响
 - 输入端与公共端（电源端或地端）之间电压差为0
 - 能负载多个输出而不影响输出效果

但实际上满足上述理想条件不现实，以下是几个偏差：
 - 最重要的偏差是输出电流会受输出端电压的影响，这个特征可以用小信号输出阻抗$R_o$表示，正如前一章所述，这个输出电阻会直接影响差分放大器的CMRR，一般来说，减小电流可以增大输出电阻，但减小电流往往意味着诸多性能的损耗
 - 另一个偏差是增益偏差，指代的是输出比输入的增益，这个增益偏差来自两个部分，一个是系统偏差，一个是随机偏差，前者是指即使器件完美匹配也会产生的误差$\epsilon$，是设计本身导致的误差，后者是由于器件失配导致的误差
 - 对于输入电压最小值，我们希望它越小越好，这可以让他满足各种各样的电路设计以及电源电压条件，不过既然是有电流流入，就必然产生了压差，如何让它更小是一个偏差
 - 输出电压裕度，将输出电压的最小值尽可能减小，可以使得其输出电压有更大的工作范围，以便于其作为有源负载工作，当然前提是其工作在饱和区
###  Simple Bipolar Current Mirrors
<div align="middle"><img src="./pic/analog_ic_gray/图4.2.png" width=450 alt="图4.2"></div>

上图是简单的bipolar电流镜电路图，首先假设两个bipolar的$V_{CE}$不影响集电极电流：
$$
V_{BE2}=V_Tln\frac{I_{C2}}{I_{S2}}=V_{BE1}=V_Tln\frac{I_{C1}}{I_{S1}}
$$
可得
$$
I_{C2}=\frac{I_{S2}}{I_{S1}}I_{C1}
$$
再根据Q1的集电极列KCL得到：
$$
I_{IN}-I_{C1}-\frac{I_{C1}}{\beta _F}-\frac{I_{C2}}{\beta _F}=0
$$
对于相同的晶体管：
$$
I_{OUT}=I_{C2}=I_{C1}=\frac{I_{IN}}{1+\frac{2}{\beta _F}}
$$
对于大的$\beta _F$，基区电流很小，可以得到：
$$
I_{OUT}=I_{C1}\simeq I_{IN}
$$
这个结果在直流和低频是准确的，但在超过3-dB点之后，基区电流会因为基区-发射区电容的阻抗降低而显著变大，导致$\beta _F$下降，使得电流镜的增益下降。

当Q1和Q2不相同时，可以得到：
$$
I_{OUT}=\frac{I_{S2}}{I_{S1}}I_{C1}=\left(\frac{I_{S2}}{I_{S1}}I_{IN} \right)\left(\frac{1}{1+\frac{1+(I_{S2}/I_{S1})}{\beta _F}} \right)
$$
鉴于$I_{S}$正比于其发射区面积，那么第一项就说明可以通过控制两边bipolar发射极面积比例以实现电流增益，这个可以通过并联单元bipolar减小光刻误差。第二项是由于$\beta _F$的有限性导致的系统偏差，当然，过大的$I_{S2}/I_{S1}$也会放大这个误差，也会导致过大的占用芯片面积。

接下来是考虑输出电阻影响的情况。
<div align="middle"><img src="./pic/analog_ic_gray/图4.3.png" width=450 alt="图4.3"></div>

图中所标点$V_{CE2}=V_{CE1}$且$V_{BE2}=V_{BE1}$


$$
I_{OUT}=\frac{I_{S2}}{I_{S1}}I_{C1}\left(1+\frac{V_{CE2}-V_{CE1}}{V_A}\right) \\
=\frac{\frac{I_{S2}}{I_{S1}}I_{IN}\left(1+\frac{V_{CE2}-V_{CE1}}{V_A}\right)}{1+\frac{1+(I_{S2}/I_{S1})}{\beta _F}}
$$

那么系统偏差为：
$$
\epsilon =\left(\frac{1+\frac{V_{CE2}-V_{CE1}}{V_A}}{1+\frac{1+(I_{S2}/I_{S1})}{\beta _F}} \right)-1\simeq \frac{V_{CE2}-V_{CE1}}{V_A}-\frac{1+(I_{S2}/I_{S1})}{\beta _F}
$$

可以看出bipolar电流镜的系统偏差来自于两部分：第一部分是有限的输出阻抗，虽说是取决于输出阻抗，但其实并非取决于$r_{o2}$而是厄利电压$V_A$，后者与偏置电流无关，而偏置电流在变化时，$V_{IN}$也会以电流的自然对数关系变化，$V_{IN}=V_{CE1}=V_{BE1}=V_{BE(on)}$，进而影响系统偏差，第二部分就是前面说过的有限的$\beta _F$导致的。

最后，最小的输出电压以保证Q2工作在正向有源区的条件为$V_{OUT(min)}=V_{CE2(sat)}\simeq 0.7V$

###  Simple MOS Current Mirrors

<div align="middle"><img src="./pic/analog_ic_gray/图4.4.png" width=450 alt="图4.4"></div>

MOS的电流镜过于熟悉，这里就简单带过了；

首先是不考虑沟道长度调制效应：


$$
V_{GS2} = V_t+\sqrt{\frac{2I_{D2}}{k'(W/L)_2}}=V_{GS1}=V_t+\sqrt{\frac{2I_{D1}}{k'(W/L)_1}} \\
I_{OUT}=\frac{(W/L)_2}{(W/L)_1}I_{D1}=\frac{(W/L)_2}{(W/L)_1}I_{IN}
$$


在考虑沟道长度调制效应后：

$$
I_{OUT}=\frac{(W/L)_2}{(W/L)_1}I_{IN}\left(1+\frac{V_{DS2}-V_{DS1}}{V_A} \right) 
$$

可以看到系统偏差为：

$$
\epsilon =\frac{V_{DS2}-V_{DS1}}{V_A}
$$

同样的，虽然是由于输出阻抗的有限导致的系统偏差，但实际上这个偏差取决于厄利电压$V_A$和漏源电压而非输出电阻 $r_{o2}=\frac{1}{\lambda I_{D2}}$

最后，关于最小的输出电压，$V_{OUT(min)}=V_{ov2}=\sqrt{\frac{2I_{OUT}}{k'(W/L)_2}}$，可以根据设计参数进行减小，这和bipolar不同。但当过驱动电压小于$2nV_T$，$n$在弱反型区有定义为$(1+\chi)$,$V_T$定义为热电压，那么这个结果就失效了，比如说在n=1.5的室温下，$2nV_T$为78mV，若晶体管工作在弱反型区，则$V_{OUT(min)}\simeq 3V_T$

###  Simple Current Mirror with Beta Helper
如前面分析bipolar电流镜偏差，其中有一部分就是由于有限的$\beta _F$导致的，当bipolar电流镜有多个输出时，基区电流的增加会导致$\beta _F$的减小，进而导致偏差的变大，故而引入*Beta Helper*如下图所示，（在有些电路中会在Q2的发射极即Q1Q3的基极加入一个电阻连接至地，用以控制Beta Helper的电流，以确保稳定的瞬态响应，这个电阻在MOS中并不需要，因为MOS管的栅极阻抗无穷大，其电流仅为pA级别）

<div align="middle"><img src="./pic/analog_ic_gray/图4.6.png" width=450 alt="图4.6"></div>

在Q2的发射极，还是取流入器件为正，流出器件为负：
$$
I_{E2}=-\frac{I_{C1}}{\beta _F}-\frac{I_{C3}}{\beta _F}=-\frac{2}{\beta _F}I_{C1} 
$$
忽略有限的输出阻抗导致的效应，Q2的基区电流为：
$$
I_{B2}=-\frac{I_{E2}}{\beta _F+1}=\frac{2}{\beta _F(\beta _F+1)}I_{C1} 
$$
在Q1集电极有：
$$
I_{IN}-I_{C1}-\frac{2}{\beta _F(\beta _F+1)}I_{C1}=0 
$$
最后得到：
$$
I_{OUT}=\frac{I_{IN}}{1+\frac{2}{\beta _F(\beta _F+1)}}\simeq I_{IN}\left(1-\frac{2}{\beta _F(\beta _F+1)} \right) 
$$
可以看到这个系统偏差被缩小了$[\beta _F+1]$倍，虽然beta helper对输出阻抗没有变化，但其改变了输入的最小电压$V_{IN}=V_{BE1}+V_{BE2}$，输入电压的裕度变小了，对于固定的偏置电流，意味着输入阻抗变大了。

beta helper常用于pnp型bipolar电流镜，因为它们的$\beta _F$常常小于npn的，同时在多个输出时，也需要它来补偿$\beta _F$的变小。

对于$\beta _F\to \infty$的MOS管而言，不需要再使用beta helper来减小系统偏差，*不过，beta helper结构可以增加MOS以及bipolar电流镜的带宽。*

###  Simple Current Mirror with degeneration

<div align="middle"><img src="./pic/analog_ic_gray/图4.7.png" width=450 alt="图4.7"></div>

如上图所示就是使用了发射极退化的bipolar电流镜，其核心想法是通过退化增大输出电阻，进而减小由于输出电阻有限导致的系统偏差，在上图的退化技术中，假设$r_\pi >>R_E$，对于Q3则有：
$$
R_o\simeq r_{o3}\left(1+g_mR_E \right)=r_{o3}\left(1+\frac{I_{C3}R_3}{V_T}\right)
$$
这个增加的部分同时反应到了系统偏差上，就输出电阻部分的偏差而言：
$$
\epsilon =\frac{V_{CE3}-V_{CE1}}{V_A(1+\frac{I_{C3}R_3}{V_T})}
$$
当然这个技术导致了输入电压和输出电压的最小值上升，需要在原来的基础上额外加$I_CR_E$

假设Q4要输出两倍的$I_{IN}$，在Q1Q4回路列KVL可得(忽略基区电流)：
$$
I_{OUT}=I_{C4}=\frac{1}{R_4}(I_{IN}R_1+V_Tln(\frac{I_{IN}}{I_{C4}}\frac{I_{S4}}{I_{S1}})) 
$$
通过复制Q1形成Q4，有$I_{S4}=2I_{S1}$，同时我们可以让发射极的退化电阻压降变大，使得输出主要由第一项决定：$I_{OUT}=(R_1/R_4)I_{IN}=2I_{IN}$，其中$R_4=R_1/2$，这个电阻也可以通过复制$R_1$并联形成。

对于MOS电流镜而言，源极退化其实并不常用，因为MOS本质上就是一个受控电阻，那么直接对MOS本身参数调制即可，比如调制沟道长度L，为了保持电流和$V_{ov}$一定，W也要同步调整以保持$W/L$恒定。

###  Cascode Current Mirror

Cascode结构能提供可观的高输出电阻，如下图所示是bipolar cascode电流镜，Q1Q3是普通的电流镜，Q2用于形成Cascode结构提高输出阻抗，Q4用于偏置Q2，由于流过电流相同，从Q2Q4的基极到Q1Q3的集电极有相同的电压差，保证了Q1工作在正向有源区，且Q3和Q1的$V_{CE}$一致
<div align="middle"><img src="./pic/analog_ic_gray/图4.8.png" width=450 alt="图4.8"></div>

根据射极退化可得到在$g_{m2}r_{o1}\simeq g_{m1}r_{o1}>>\beta _0$时：
$$
R_o=r_{o2}\left(1+\frac{g_{m2}r_{o1}}{1+\frac{g_{m2}r_{o1}}{\beta _0}} \right)\simeq \beta _0r_{o2}
$$
这个结果乍一看确实没问题，但有一个深层的问题，我们假设了$g_{m2}r_{o1}>>\beta _0$即$r_{o1}>>r_{\pi 2}$，这个关系本身是没问题的，它意味着流入Q2的集电极电流会更多的从Q2的基区流出，但这个电流镜结构导致这个电流关系出现了偏差，即$i_{b2}$的变化必然通过镜像回路导致$i_{e2}$产生相同的变化，那么Q2集电极电流必然是平等的分流去Q2的基极和发射极，那么输出阻抗就会减半：
$$
R_o\simeq \frac{\beta _0r_{o2}}{2}
$$
cascode电流镜的一个问题是电压裕度：

$$
V_{IN(min)}=V_{BE3}+V_{BE4}=2V_{BE(on)} \\
V_{OUT(min)}=V_{CE1}+V_{CE2}\simeq V_{BE(on)}+V_{CE2}
$$

这个问题在低电源电压尤为重要。

另一个问题是由于$\beta _F$导致的系统偏差，虽然输出阻抗变大使得一部分系统偏差变小，但$\beta _F$导致的偏差变大了，本质上是由于Q1Q3的基极电流叠加进入Q4，再加上自身基区的电流，这些电流叠加之后与$I_{IN}$相差再被复制到输出，计算过程省略，直接给出结果(电流增益为1)：

$$
I_{OUT}=I_{C2}\left(\frac{\beta _F}{\beta _F+1} \right)\left(\frac{I_{IN}}{1+\frac{2}{\beta _F}+\frac{1}{\beta _F+1}} \right) \\
=I_{IN}(1+\epsilon) \\
其中\epsilon =-\frac{4\beta _F+2}{\beta _F^2+4\beta _F+2} \\
若\beta _F>>1，\epsilon\simeq -\frac{4}{\beta _F+4}
$$

而相同情况下，simple current mirror的$\beta _F$部分的系统误差为$-2/\beta _F$

接下来是MOS cascode current mirror，
<div align="middle"><img src="./pic/analog_ic_gray/图4.9.png" width=450 alt="图4.9"></div>

其输出阻抗为：
$$
R_o=r_{o2}[1+(g_{m2}+g_{mb2})r_{o2}]+r_{o1}
$$
与bipolar不同的是，MOS管的cascode电流镜由于$\beta _F\to \infty$，那么也就没有被减弱的$\beta _F$系统偏差以及$\beta _Fr_{o}/2$的修正输出电阻，但，MOS衬底的漏电流会从输出节点向地产生电阻分流，当$V_{OUT}>V_{OUT(min)}$时，输出电阻会受到影响。

在$V_{GS4}=V_{GS2}$时，$V_{DS1}=V_{DS3}$，那么可以认为$\epsilon \simeq 0$

这种连接方式的缺点是浪费了输出电压裕度，使M2和M1工作在饱和区的最小输出电压$V_{OUT(min)}=V_{DS1}+V_{DS2}$，由于M1复制了M3的漏源电压，导致$V_{OUT(min)}$从$2V_{ov}$变为了$V_{t}+2V_{ov}$，也就是浪费了一个阈值电压的裕度。

第一个修改方案是加入一个源极跟随器作为电平移动：
<div align="middle"><img src="./pic/analog_ic_gray/图4.11.png" width=450 alt="图4.11"></div>

上图非常清晰的展示了这种方法的思路和实现，M5实现电平移动，使M4的电位下降一个$V_t+V_{ov}$之后再给M2栅极，进而使M1漏极下降至$V_{ov}$，M5由M6和M3进行偏置。

需要注意的是，为了使M1的漏源电压在两次的$V_{GS}$移动之后仍为$V_{ov}$，需要使M4的栅极再上升一个$V_{ov}$，再结合M3的栅漏电压，以及保持偏置电流不变下，M4的(W/L)需要变为原来的1/4。

实际设计中，$(W/L)_4$其实要比1/4来的更小，有两个原因，一，实际的MOS管的饱和区和线性区并不泾渭分明，所以$V_{ov}$需要来的更大一些以保证足够大的输出阻抗；二，根据KVL环路：
$V_{DS1}=V_{GS3}+V_{GS4}-V_{GS5}-V_{GS2}$，在固定的偏置电流下，这些$V_{GS}$中的$V_{ov}$部分固定，而$V_{t}$会受衬偏效应影响，其中的$V_{t2}>V_{t3}，V_{t5}>V_{t4}$，故$V_{ov4}$要更大一些以保证$V_{DS1}$的值，从而$(W/L)_4$需要更小。

然后是这个电路的缺点，
 - 第一，系统偏差

   为了降低输出最小电压，$V_{DS1}$从$V_{t}+V_{ov}$降为了$V_{ov}$，这就再次引回了系统偏差：
   
$$
\epsilon =\frac{V_{DS1}-V_{DS3}}{V_A}\simeq -\frac{V_t}{V_A}
$$
   不过这个值相较无cascode结果变小，并且不随$V_{OUT}$变化
 - 第二，功耗

   M5作为源极跟随器的存在导致了新的支路的产生，这也就增加了功耗。

抛开功率的问题先不谈，如何解决系统偏差，问题在于如何使M3的漏源电压也等于$V_{ov}$，
<div align="middle"><img src="./pic/analog_ic_gray/图4.12.png" width=450 alt="图4.12"></div>

如上图的(a)所示，由于M6是二极管连接方式，那么说明其一定工作在饱和区，而其栅源压差$V_{GS6}>V_t$也是M5的栅漏压差$V_{GD5}>V_t$，说明M5工作在线性区。

为了使M1的$V_{DS1(min)}=V_{ov}$，M2的$V_{DS2(min)}=V_{ov}$，那么它们两个的栅极压差为$V_{ov}$，正如上图和上上图中所示，那么问题就是如何产生一个$V_{ov}$，二极管连接的肯定不行，那么正是使用M5产生这个$V_{ov}$，根据M6的饱和区和M5的线性区可有：
$$
\frac{k'}{2}\left(\frac{W}{L}\right)_6(V_{GS6}-V_t)^2=\frac{k'}{2}\left(\frac{W}{L}\right)_5(2(V_{GS5}-V_t)V_{DS5}-(V_{DS5})^2)
$$
代入条件：

$$
V_{GS6}=V_t+V_{ov} \\
V_{DS5}=V_{ov} \\
以及推得的:V_{GS5}=V_t+2V_{ov}
$$

解得：
$$
\left(\frac{W}{L}\right)_5=\frac{1}{3}\left(\frac{W}{L}\right)_6
$$
现在回到(b)图的电路中，该cascode电流镜电路被称为*Sooch* cascode current mirror，先不管M4的存在，那么M5提供$V_{ov}$，二极管连接的M3提供$V_{ov}+V_t$，那么M1和M2的栅极电压和预期的一样分别为$V_t+V_{ov}$和$V_t+2V_{ov}$。

现在加入M4进行分析，M4的目的是为了将M3的漏极电压降低到$V_{ov}$，有：

$$
V_{DS3}=V_{G2}-V_{GS4} \\
V_{G2}=V_t+2V_{ov} \\
V_{GS4}=V_{ov}+V_t \\
=>V_{DS3}=V_{ov}
$$

那么系统偏差$\epsilon =0$，在这些条件下，$V_{DS4}=V_{GS3}-V_{DS3}=V_t$，为了M4能工作在饱和区，要求$V_t>V_{ov}$，这个条件常常能够成立，但在一些情况下不成立，如低阈值或高过驱动，那么M4就会工作在线性区，导致在偏置电流下，栅源电压取决于漏源电压，进而增加系统偏差，此外，温度升高会导致阈值电压下降，而过驱动反而上升，所以要在设计时考虑各个温度下都是否满足该条件。

该高输出摆幅电流镜的一个问题是输入电压很高，会达到$3V_{ov}+2V_t$，这个值在低电源电压是个很高的值，会严重影响使用，可以在电流镜里用低阈值器件，在开关中用高阈值，但这会显著增加工艺复杂度和成本。

为了解决输入电压过高的问题，可以将偏置的电路单独作为一条输入支路：
<div align="middle"><img src="./pic/analog_ic_gray/图4.13.png" width=450 alt="图4.13"></div>

通过M5M6生成$V_t+2V_{ov}$送往M4和M2的栅极，使支路自己生成M3和M1的漏源电压$V_{ov}$，这样一来，虽然额外增加了一条支路，但输入电压裕度变大了，$V_{IN1(min)}=2V_{ov}+V_t，V_{IN2(min)}=V_{ov}+V_t$，明显比Sooch电流镜的输入电压裕度变大了。

在这个电路中M5并不直接提供$V_{ov}$给另两个支路，其作用只是用来偏置M6，那么可以用一个二极管连接的MOS管M7替代M5和M6，只要其$V_{GS7}=V_t+2V_{ov}$即可，这可以通过调整宽长比轻松实现，通常而言，M7的宽长比(W/L)为M1~M4宽长比的$1/4$甚至更小以提供足够的$V_{GS7}$，这种方法在电流镜以及偏置电路中更为常见。

除此之外还有一种名为*Staked MOS*的低压电流镜方法，它相较上面那种方法有更好的匹配。

###  Wilson Current Mirrror
在前面分析bipolar cascode电流镜时，最大的缺点是有限的$\beta _F$导致的系统偏差，接下来的威尔逊电流镜就是通过负反馈减小这一部分影响
<div align="middle"><img src="./pic/analog_ic_gray/图4.14.png" width=450 alt="图4.14"></div>

当$I_{IN}$与$I_{C3}$之间的偏差通过Q2的基极传出时，其被乘$(\beta _F+1)$后作为Q2的发射极电流，然后因Q1Q3电流镜复制到Q3的集电极，进而减小误差。

当输出电压变化时，比如变大时，Q2的集电极电流变大，进而Q1的集电极电流也变大，传回到Q3，使Q3的集电极电流也变大，进而减小了$I_{IN}$与$I_{C3}$之间电流差，使Q2的基极电流变小，进而使Q2的集电极电流变小，形成负反馈。

在上图的(b)中可以分析小信号的输出阻抗，这里不详述计算过程，有一点值得一提的是，其实这里的输出阻抗的特点和cascode电流镜一样，也会因为电流镜的复制原因导致Q2集电极进入的小信号电流因为复制原因平均的分到发射极和基极，不过只是这里是输出的支路将电流反馈回去。

当$r_{o3}\to \infty$，Q1Q3相同（电流增益为）：
$$
R_o=\frac{1}{g_{m1}(2)}+r_{o2}+\frac{g_{m2}r_{\pi 2}r_{o2}}{2}\simeq \frac{\beta _0r_{o2}}{2} 
$$

对于直流特性，假设$V_A\to \infty$，且每个bipolar管一样。
$$
V_{IN(min)}=V_{CE3}=V_{BE1}+V_{BE2}=2V_{BE(on)} \\
V_{OUT(min)}=V_{CE1}+V_{CE(sat)}=V_{BE(on)}+V_{CE2(sat)}
$$
对于系统偏差的分析，也不再赘述计算过程了，结果为：
$$
I_{OUT}\simeq I_{IN}\left(1-\frac{2}{\beta _F^2+2\beta _F+2} \right)\left(1-\frac{V_{BE2}}{V_A} \right) \\
\epsilon \simeq -\left(\frac{2}{\beta _F^2+2\beta _F+2}+\frac{V_{BE2}}{V_A} \right)
$$
可以得到的是，wilson电流镜的$\beta _F$系统偏差确实相比cascode变小了，但Q1和Q3的集电极-发射极电压不一样导致了输出阻抗系统偏差，这个可以通过在Q3的集电极和Q2的基极加上一个二极管连接的bipolar管来解决，所以不是很大的问题。

<div align="middle"><img src="./pic/analog_ic_gray/图4.15.png" width=450 alt="图4.15"></div>

上图是MOS的Wilson电流镜，相比bipolar型，其电气参数取$\beta _F\to \infty,r_{\pi 2}\to \infty$，输出电阻为：
$$
R_o \simeq (1+g_{m2}r_{o3})r_{o2}
$$
如果考虑入M2的衬底效应，
$$
R_o \simeq (2+g_{m2}r_{o3})r_{o2}
$$
可以看到其实差的不大，因为M2的源极经过M1的二极管连接到地，几乎不变。
对于直流特性：

$$
V_{OUT(min)}=V_{GS1}+V_{ov2}=V_t+2V_{ov} \\
V_{IN}=V_{GS1}+V_{GS2}=2V_t+V_{ov} \\
$$

在不加入M4时，系统偏差为：
$$
\epsilon =-\frac{V_{GS2}}{V_A}
$$
加入M4后
$$
\epsilon \simeq 0
$$

## Active Load
前文中提到的差分对结构，是以差分输入，差分输出为类型的电阻负载式放大器，这个结构有一些问题：
- 首先，电阻在集成电路中的实现较为困难，精度较低
- 其次，在放大器处于反馈回路中，往往越大的增益越好，但电阻作为负载的放大器往往很难提供大的增益
- 假如在电阻上施加的压降较大，则会影响输入摆幅以及输出摆幅

基于以上原因，引入有源负载，其具有大的输出阻抗$r_o$以及较大的输出阈值。

下图所示的便是经典的五管OTA，其相较之下有更为简便的避免了共模反馈的问题：
<div align="middle"><img src="./pic/analog_ic_gray/OTA.png" width=300 alt="OTA"></div>
该电路通过负载的电流镜使得两边的负载都流过$I_{TAIL}/2$，形成了自偏置，这相比外加偏置的有源负载解决了共模偏置问题，同时由于复制关系，两边的电流以及跨导都没有被浪费，相比普通的电阻负载，其共模抑制能力更强。

### 小信号分析
下图展示的是bipolar的五管OTA的小信号模型，其中$\beta _F \to \infty$，MOS的版本只需要将$r_{\pi}\to \infty$即可。其中的（b）图是简化后的小信号图，并且在负载的电流镜中加入了误差项
<div align="middle"><img src="./pic/analog_ic_gray/pic_4.26.png" width=450 alt="图4.26"></div>

定义输入的小信号分别为$v_{i1}$和$v_{i2}$，以及共模信号$v_{1}=v_{ic}=(v_{i1}+v_{i2})/2$,差模信号$v_{id}=(v_1-v_2)/2$，进一步简化模型，使$r_{tail}\to \infty ,r_{o(dp)}\to \infty$，那么有：
$$
i_1=g_{m(dp)}(v_{i1}-v_1)=\frac{g_{m(dp)}v_{id}}{2} \\
i_2=g_{m(dp)}(v_{i2}-v_1)=-\frac{g_{m(dp)}v_{id}}{2}
$$
可以看到，假如是非电流镜结构的负载，如电阻负载，只有$i_2$会传输到单输出节点，$i_1$被浪费了，那么总体的电路跨导为$G_{m}[dm]=\frac{i_{out}}{v_{id}}\bigg |_{v_{out}=0}=-\frac{i_2}{v_{id}}=\frac{g_{m(dp)}}{2}$

而对于电流镜负载的结构，$i_1$也能被复制到输出节点，进而提高了跨导，输出电流为：
$$
 i_{out}=-(1-\epsilon)i_3-i_2 
$$
假设$\epsilon_m =0$，有$i_{3}=-i_1$，那么根据$i_{out}=g_{d(dp)}v_{id}$:
$$
 G_{m}[dm]=\frac{i_{out}}{v_{id}}\bigg|_{v_{out}=0}=g_{m(dp)}  
$$

对于输出阻抗，可按下图的方式求得，在输出节点加一个电压源，然后测量输入的电流，其余的电压源接地
<div align="middle"><img src="./pic/analog_ic_gray/pic_4.27.png" width=450 alt="图4.27"></div>

首先$i_{t1}$由测试电压经过$r_{o4}$流向地，故：
$$
 i_{t1}=\frac{v_t}{r_{o4}} 
$$
从测试电压向输入管M2看去便是一个被退化的共源管，退化的电阻为$r_{tail}$和从源看进去的M1的阻抗，为$1/g_{m1}$，若$1/g_{m}\ll r_{tail}$，那么可得：
$$
 i_{t2}+i_{t4}\simeq \frac{v_{t}}{r_{o2}\left(1+g_{m2}(\frac{1}{g_{m1}}\parallel r_{tail})\right)}\simeq \frac{v_t}{2r_{o2}} 
$$
对于$i_{t3}$，其受$v_{3}$控制，在假设电路的复制是无偏差的情况下，那么这份电流等于M1漏极的小信号电流，假设$r_{tail}$很大，小信号电流不流经它，那么这份电流完全由M2提供，则有：
$$
 i_3\simeq i_{2}+i_{4}\simeq \frac{v_t}{2r_{o2}} 
$$
那么总的输出阻抗为：
$$
R_o=\frac{v_t}{i_t}\bigg|_{\substack{v_{i1}=0 \\ v_{i2}=0}}\simeq \frac{1}{\frac{1}{r_{o(dp)}}+\frac{1}{r_{o(mir)}}}=r_{o(dp)}\parallel r_{o(mir)}
$$
往往在记忆这个输出阻抗以及推导其他放大器的输出阻抗时，我们简单的记忆为输出点的两个MOS管的输出阻抗的并联，这种理解从上述的分析可以发现有很大的问题，本质上是认为M1 M2的源极可以认为接地导致的，这种理解导致忽略了$r_{o2}$受到退化的影响以及电流镜对小信号的复制作用，不过从结果上看，复制小信号的部分正好是一个$2r_{o2}$的并联，导致结果是正确的，这种直觉式的分析虽然漏洞百出，不过在分析时确实会带来巨大的便捷，这一点在后续的cascode以及folded cascode都有展现。

对于输入阻抗，MOS管的输入阻抗为无穷大，而bipolar的输入阻抗可以近似认为直接是$2r_{\pi (dp)}$，不过实际上，由于电路的不对称以及高增益反馈的输出阻抗从T2到节点1，导致会有微小的偏差于$2r_{\pi (dp)}$

最后，有源负载的差分放大器能够将差分的双输入转变为对地的单端输出，同时，高输出阻抗也要求下一级也有高的输入阻抗以保持高增益，该结构的双端口等效电路如下图所示：
<div align="middle"><img src="./pic/analog_ic_gray/pic_4.28.png" width=450 alt="图4.28"></div>

### CMRR
接下来我们把电阻负载的差分放大器和电流镜负载的差分放大器放在一起讨论它们的CMRR，并且它们都是差分输入，单端输出。
<div align="middle"><img src="./pic/analog_ic_gray/pic_4.29_a.png" width=450 alt="图4.29_a"></div>

之前在单独讨论电阻负载的差分放大器时，那时输出为差分输出，故CMRR的定义有所不同，详情见[完美对称的差分对的小信号分析](#完美对称的差分对的小信号分析)，这里分析的都是单端输出，故对于输出电压有，其中$A_{dm}>0,A_{cm}<0$：

$$
v_o=-\frac{v_{od}}{2}+v_{oc}=-\frac{A_{dm}v_{id}}{2}+A_{cm}v_{ic} \\
=-\frac{A_{dm}}{2}\left(v_{id}-\frac{2A_{cm}}{A_{dm}}v_{ic}\right) \\
=-\frac{A_{dm}}{2}\left(v_{id}+2\left|\frac{A_{cm}}{A_{dm}}\right|v_{ic}\right) \\
=-\frac{A_{dm}}{2}\left(v_{id}+\frac{2v_{ic}}{CMRR}\right)
$$

可以看到在这里CMRR的定义为，共模输入对输出的影响:
$$
 CMRR=\left|\frac{A_{dm}}{A_{cm}}\right|=\left|\frac{G_m[dm]R_o}{G_m[cm]R_o}\right|=\left|\frac{G_m[dm]}{G_m[cm]}\right| 
$$
其中对于$G_m[cm]$定义为共模跨导：
$$
 G_m[cm]=\frac{i_{out}}{v_{ic}}\bigg|_{v_{out}=0} 
$$
那么对于电阻负载的结构很容易根据退化级共源结构的公式得到：

$$
 G_m[cm](resistively\enspace loaded)=-\frac{i_2}{v_{ic}}\simeq -\frac{g_{m(dp)}}{1+g_{m(dp)}(2r_{tail})}  \\
CMRR=\frac{1+2g_{m(dp)}r_{tail}}{2}\simeq g_{m(dp)}r_{tail}=g_{m1}r_{o5}
$$

其中$g_{m(dp)}$为输入对管的跨导，$r_{tail}$为尾电流源的小信号输出阻抗。可以看出由于该结构的跨导为$g_{m(dp)}/2$故导致CMRR被减半了。当用bipolar实现该结构时，由于bipolar的本征增益更大，所以CMRR也会更好。

接下来分析电流镜负载的CMRR，我们先假设T1 T2 T3 T4都有无穷大的小信号输出阻抗，且T3 T4的复制关系完美，虽然这种假设不可能在现实中成立，但通过这个分析我们可以更好理解为什么该电路的CMRR较好，且更好理解该电路的小信号模型。
<div align="middle"><img src="./pic/analog_ic_gray/pic_4.29_b.png" width=450 alt="图4.29_b"></div>

对于上面所述的假设条件，对于T1 T2的小信号电流有：$i_1=i_2=i_{tail}/2$，且由于无小信号输出阻抗，T1的小信号电流全部被T3的受控源吸收，并且由于完美复制，即$\epsilon_m=0$，有关系：$i_1=-i_3=-i_4$，则在输出点有KCL：$i_{out}=-i_2-i_4=-i_2+i_1=0$，则$G_m[cm]=\frac{i_{out}}{v_{ic}}\bigg|_{v_{out}=0}=0$，则可知$CMRR\to \infty$。

先不谈这个结果在实际中的不成立点，可以看到由于复制的关系，这个电路的CMRR非常好。接下来分析为什么这个关系在现实中为什么不成立。

在纳入小信号输出阻抗考虑时，我们可以把原本$G_m[cm]$的输出电流变化转化为输出点的电压变化，假使$i_4$和$i_2$的变化量完全一致那么输出节点的变化必然为零，这是由MOS管的输出特性所决定的，如果两边对称，则T1 T3的漏端（集电极）也应该完全不变，但如果把T3的小信号输出阻抗考虑进去（甚至可以先不考虑T1本身的小信号阻抗），$i_1$不能完全被T3的受控源吸收，一部分会被T3的输出阻抗吸收造成漏级（集电极）的电压变化，这种偏移和前面的结论便冲突了，也可以用公式来表示上述内容，将T1 T3的漏极作为F点，有：

$$
 \Delta v_F=\Delta i_{1}\left(\frac{1}{g_{m3}}\parallel r_{o3}\right) \\
|\Delta i_{4}|=g_{m4}\Delta v_{F}=g_{m4}\Delta i_{1}\frac{r_{o3}}{1+g_{m3}r_{o3}} \\
\Delta v_{out}=(\Delta i_1g_{m4}\frac{r_{o3}}{1+g_{m3}r_{o3}}-\Delta i_2)r_{o4}=-\Delta i_{1}\frac{r_{o4}}{1+g_{m3}r_{o3}}
$$

把方向纳入考虑的话，可以发现$\Delta v_F$的变化与$\Delta v_{out}$一样。如果把T1 T2的输出阻抗纳入考虑结果可以预见是大差不差的。

那么接下来分析准确的CMRR，这里Gary和Razavi均有各自的方法，前者精确的用误差项$\epsilon _m$和$\epsilon _d$表示复制的误差与输入的跨导误差和小信号输出阻抗误差，最终经过详细的推导得到准确的答案，并给予适当简化，而Razavi先是考虑各个管的输出阻抗，使用完全对称的假设得到了近似的结果，再单独考虑输入管失调的问题（但忽略了输入管的输出阻抗），Razavi在他的书中讨论电阻负载的失配对CMRR的影响时也是先考虑尾电流源的输出阻抗再加上负载失配的情况，虽然后者可以较为灵巧的解释电路且方法非常简短，但当需要详细分析时，他的奇技淫巧反而令人难以理解，其对于各个情况，各个情况以及误差的分析十分跳跃，而且Razavi对于长式子的化简以及表达实在令人难以恭维，所以此处重点介绍Gary的方法。

首先对于输入管误差，取
$$
i_1=i_2(1-\epsilon_d)
$$
其次考虑复制误差，取
$$
 i_4=i_3(1-\epsilon_m) 
$$
故输出电流为：
$$
 i_{out}=-i_4-i_2=i_1(1-\epsilon_m)-i_2=i_2((1-\epsilon_d)(1-\epsilon_m)-1)=-i_2(\epsilon_d+\epsilon_m-\epsilon_d\epsilon_m) 
$$
由于$\epsilon_m,\epsilon_d\ll 1$，对于$\epsilon_d\epsilon_m$这个二阶小量可以忽略
$$
 i_{out}\simeq-i_2(\epsilon_d+\epsilon_m) 
$$
则共模跨导为：
$$
 G_m[cm]\simeq-\left(\frac{i_2}{v_{ic}}\right)(\epsilon_d+\epsilon_m) 
$$
括号的式子等于阻抗负载的差分放大器的共模跨导，则替代进去有：
$$
 G_m[cm]\simeq-\left(\frac{g_{m(dp)}}{1+g_{m(dp)}(2r_{tail})}\right)(\epsilon_d+\epsilon_m) 
$$
则该电路的CMRR为：
$$
 CMRR=\left|\frac{G_m[dm]}{G_m[cm]}\right|\simeq\frac{1+2g_{m(dp)}r_{tail}}{(\epsilon_d+\epsilon_m)} 
$$
对比电阻负载的差分对的CMRR可以看出有一个$2/(\epsilon_d+\epsilon_m)$的因子区别，分子的2源于该结构差分跨导的翻倍，分母的误差项源于共模跨导的变小。
<div align="middle"><img src="./pic/analog_ic_gray/pic_4.26b.png" width=450 alt="图4.26b"></div>

输入管的偏差来自于计算跨导时两者的负载不同，可以由上图小信号以及以下的计算得知：取输入的$v_{i1}=v_{i2}=v_{ic}$

$$
 i_1=g_{m(dp)}(v_{ic}-v_1)+\frac{v_3-v_1}{r_{o(dp)}} \\
i_2=g_{m(dp)}(v_{ic}-v_1)-\frac{v_1}{r_o(dp)}
$$

取$i_3=-i_1$，且近似负载$\frac{1}{g_{m(mir)}}\parallel r_{o(mir)}\simeq \frac{1}{g_{m(mir)}}$则有：

$$
 i_1\simeq g_{m(dp)}(v_{ic}-v_1)-\frac{v_1}{r_{o(dp)}}-\frac{i_1}{g_{m(mir)}r_{o(dp)}} \\
<=>\left(\frac{1+g_{m(mir)}r_{o(dp)}}{g_{m(mir)}r_{o(dp)}}\right)i_1\simeq g_{m(dp)}(v_{ic}-v_1)-\frac{v_1}{r_{o(dp)}} \\
i_1\simeq i_2\left(\frac{g_{m(mir)}r_{o(dp)}}{1+g_{m(mir)}r_{o(dp)}}\right) 
$$

由$i_1=(1-\epsilon_d)i_2$可以得到误差项$\epsilon_d$的表达式：
$$
 \epsilon_d=\frac{1}{1+g_{m(mir)}r_{o(dp)}}
$$
接下来讨论$\epsilon_m$的表达式，在先前的讨论中，我们假设T3的漏极看进去的阻抗$r_3\simeq 1/g_{m(mir)}$，这个假设被运用在了求差分跨导以及输入管误差中，但在讨论负载复制误差时，这个假设不能成立，故该节点看进去的误差完善为$r_3=\frac{1}{g_{m(mir)}}\parallel r_{o3}\parallel r_{\pi 3} \parallel r_{\pi 4}$，假设两个管子完美匹配，即不考虑随机失调误差，有：
$$
 r_3=\frac{r_{\pi (mir)}r_{o(mir)}}{r_{\pi (mir)}+2r_{o(mir)}+g_{m(mir)}r_{\pi (mir)}r_{o(mir)}} 
$$
根据电路小信号模型可知
$$
g_{m4}v_3=g_{m4}i_3r_3=\frac{g_{m4}r_{\pi (mir)}r_{o(mir)}i_3}{r_{\pi (mir)}+2r_{o(mir)}+g_{m(mir)}r_{\pi (mir)}r_{o(mir)}} \\
i_4=\frac{g_{m4}r_{\pi (mir)}r_{o(mir)}}{r_{\pi (mir)}+2r_{o(mir)}+g_{m(mir)}r_{\pi (mir)}r_{o(mir)}}i_3
$$
由$i_4=(1-\epsilon_m)i_3$可以得到复制误差项$\epsilon_m$的表达式：
$$
 \epsilon_m=\frac{r_{\pi (mir)}+2r_{o(mir)}}{r_{\pi (mir)}+2r_{o(mir)}+g_{m(mir)}r_{\pi (mir)}r_{o(mir)}} 
$$
对于bipolar，$r_\pi$通常远小于$r_o$，那么可以化简得到：
$$
 \epsilon_m[bip]=\frac{2+\frac{r_{\pi (mir)}}{r_{o(mir)}}}{2+\frac{r_{\pi (mir)}}{r_{o(mir)}}+g_{m(mir)}r_{\pi (mir)}}\simeq \frac{1}{1+\frac{g_{m(mir)}r_{\pi (mir)}}{2}}=\frac{1}{1+\frac{\beta _0}{2}} 
$$
对于MOS，取$r_{\pi}\to \infty$:
$$
 \epsilon_m[MOS]=\frac{1}{1+g_{m(mir)}r_{o(mir)}} 
$$
那么代回到CMRR的公式$CMRR\simeq \frac{1+g_{m(dp)}r_{tail}}{\epsilon_d+\epsilon_m}$有：
$$
 CMRR[bip]\simeq \frac{1+2g_{m(dp)}r_{tail}}{\frac{1}{1+g_{m(mir)}r_{o(dp)}}+\frac{1}{1+\frac{g_{m(mir)}r_{\pi (mir)}}{2}}} 
$$
取$g_{m(mir)r_{o(dp)}}\gg 1,g_{m(mir)}r_{\pi (mir)}/2\gg 1$，得到简化结果：

$$
 CMRR[bip]\simeq (1+2g_{m(dp)}r_{tail})g_{m(mir)}\left(r_{o(dp)}\parallel \frac{r_{\pi (mir)}}{2}\right) \\
\simeq (2g_{m(dp)}r_{tail})g_{m(mir)}\left(r_{o(dp)}\parallel \frac{r_{\pi (mir)}}{2}\right) 
$$

对比电阻负载的单端输出的CMRR:$g_{m(dp)}r_{tail}$，有源负载的CMRR提高了$2g_{m(mir)}\left(r_{o(dp)}\parallel \frac{r_{\pi (mir)}}{2}\right)$倍
对于MOS情况：
$$
 CMRR[MOS]\simeq\frac{1+2g_{m(dp)}r_{o(tail)}}{\frac{1}{1+g_{m(mir)}r_{o(dp)}}+\frac{1}{1+g_{m(mir)}r_{o(mir)}}} 
$$
取$g_{m(mir)}r_{o(dp)}\gg 1,g_{m(mir)}r_{o(mir)}\gg 1$，可得到化简式子：

$$
 CMRR[MOS]\simeq (1+2g_{m(dp)}r_{o(tail)})g_{m(mir)}(r_{o(dp)}\parallel r_{o(mir)}) \\
\simeq (2g_{m(dp)}r_{o(tail)})g_{m(mir)}(r_{o(dp)}\parallel r_{o(mir)})
$$

对比电阻负载的单端输出的CMRR:$g_{m(dp)}r_{tail}$，有源负载的CMRR提高了$2g_{m(mir)}\left(r_{o(dp)}\parallel r_{o(mir)}\right)$倍

接下来考虑随机失配的影响，其中不进行推导，只给出结果以及结果分析。

对于差模输出跨导，在考虑输入管，负载管跨导失调的情况下：
$$
 G_m[dm]\simeq g_{m(1-2)}\left[\frac{1-\left(\frac{\Delta g_{m(1-2)}}{2g_{m(1-2)}}\right)^2}{1+\left(\frac{\Delta g_{m(3-4)}}{2g_{m(3-4)}}\right)}\right] 
$$
其中$\Delta g_{m(1-2)}=g_{m1}-g_{m2},g_{m(1-2)}=(g_{m1}+g_{m2})/2,\Delta g_{m(3-4)}=g_{m3}-g_{m4},g_{m(3-4)}=(g_{m3}+g_{m4})/2$，该结果的近似成立于每个晶体管的$g_mr_o\gg 1$，尾电流管$(g_{m1}+g_{m2})r_{tail}\gg 1$的情况。

可以看出来其实输入管的跨导偏差对整体的跨导影响并不大，这是由于在两边的输入管跨导一致时，尾电流管的漏源小信号电压为零，而当一边的跨导大于另一边时（栅级小信号电压不修改，同时忽略输入管的小信号输出阻抗），比如$g_{m1}>g_{m2}$时，保持$v_{g1}=v_{id}+v_{ic}$，但由于跨导较大，导致从尾电流源的输出阻抗吸收一部分小信号电流以满足跨导增加，但这部分电流又在尾电流输出阻抗上产生压降，导致尾电流源漏极也是M1的源极电压上升，导致$v_{gs1}=v_{g1}-v_{s1}$减小，抑制了电流的变化，这种效应导致了整体差模跨导受$g_{m1}-g_{m2}$影响变小，但与此同时，$g_{m3}$和$g_{m4}$却可以直接影响$i_1$到输出端的复制，故而影响更大一些。

对于共模输出跨导，考虑输入管的跨导误差、输出阻抗误差，负载电流镜管的跨导误差，有：
$$
 G_m[cm]\simeq -\frac{1}{2r_{tail}}(\epsilon_d+\epsilon_m) 
$$
其中$\epsilon_d$和$\epsilon_m$的定义仍然取
$$
i_1=i_2(1-\epsilon_d)
$$

$$
i_4=i_3(1-\epsilon_m) 
$$
在这里
$$
 \epsilon_d\simeq \frac{1}{g_{m3}r_{o(dp)}}-\frac{\Delta g_{m(1-2)}}{g_{m(1-2)}}\left(1+\frac{2r_{tail}}{r_{o(dp)}}\right)-\frac{2r_{tail}}{r_{o(dp)}}\frac{\Delta r_{o(dp)}}{r_{o(dp)}} 
$$
以上各项均为单个增益误差，不考虑高阶误差，即各个误差之间的相互作用。

首先第一项源于输入管的负载不同，T1负载为二极管，T2负载为小信号地，这一点在前面解释过。第二项源于$g_{m1}$和$g_{m2}$的失调，第三项源于$r_{o1}$和$r_{o2}$之间的失调，后者对$G_m[cm]$的影响相较于第二者对之的影响更大，因为电流镜会削弱跨导失调对于$G_m[cm]$的影响，相反，$G_m[dm]$受$r_{o1},r_{o2}$的影响相对而言并不大，因为电流镜以及差分输入导致$g_{m1},g_{m2}$并不在输出相互抵消（甚至相互增强）。

对于复制误差：
$$
 \epsilon_m=\frac{1}{1+g_{m3}r_{o3}}+\frac{(g_{m3}-g_{m4})r_{o3}}{1+g_{m3}r_{o3}}\simeq \frac{1}{g_{m3}r_{o3}}+\frac{\Delta g_{m(3-4)}}{g_{m(3-4)}} 
$$

同样，以上各项均为单个增益误差，不考虑高阶误差，即各个误差之间的相互作用。

第一项是前面提到的系统误差，源于电流镜本身的输出阻抗，导致T3的漏极看进去的阻抗不是$\frac{1}{g_{m3}}$而是$\frac{1}{g_{m3}}\parallel r_{o3}$，导致电流复制的偏差，这一点在前面解释过了。第二项源于$g_{m3},g_{m4}$的失调。

在没有失配的时候共模跨导非常小，这是由于电流镜结构所导致的，而失配则总是通过增大$|G_{m}[cm]|$进而减小CMRR。

##  Voltage and Current References
需要提前说明的是，“基准”和“偏置”两个概念在电路里几乎是息息相关的，产生了基准之后用以偏置电流（或电压），甚至有时候基准本身就是一种偏置，在接下来的部分将详细讲解这些基准电路。
###  Low-Current Biasing
所谓的Low-Current也就是指能产生几uA到几百nA的电流偏置，他和后面谈到的Supply-Insensitive Biasing 和 Temperature-Insensitive Biasing并不是互斥或对立关系，他们彼此相交甚至包含。故而我们先介绍一下***sensitivity***即***灵敏度***的定义：
####  Sensitivity
对于一个受$x$变量影响的变量$y$，变量$y$对参数$x$的灵敏度定义如下：

$$
S_x^y=\lim _{\Delta x\to 0}\frac{\Delta y/y}{\Delta x/x}=\frac{x}{y}\frac{\partial y}{\partial x}
$$

对于输出电流$I_{OUT}$对电源电压$V_{SUP}$的灵敏度有：
$$
S_{V_{SUP}}^{I_{OUT}}=\frac{V_{SUP}}{I_{OUT}}\frac{\partial I_{OUT}}{\partial V_{SUP}}
$$

<div align="middle"><img src="./pic/analog_ic_gray/图4.30.png" width=450 alt="图4.30"></div>

上图展示的是极为简单的电流偏置，仅用电源电压和电阻实现，这个*电流镜*电路的缺点很明显，如果需要小电流的话，那么电阻的值就要很大，比如对于（a）的电路，假设$V_{BE(on)}=0.7V$，电源电压为5V，设定输出电流为5uA，而Q1最大化取10倍Q2，则输入电流为50uA，解得$R=86k\Omega$，这个电阻的面积会影响很多面积，同时，当电源电压远大于$V_{BE(on)}$或者$V_{GS}$时，那么输入电流等于输出电流的情况下，输出电流约等于电源电压除以偏置电阻，那么输出电流对电源电压的灵敏度约为$S_{V_{SUP}}^{I_{OUT}}\approx 1$，可见其性能一般。

故接下来介绍***Wildar 电流源***，这个名字虽然较为陌生，但其使用程度可谓广泛。
####  Wildar Current Source

<div align="middle"><img src="./pic/analog_ic_gray/图4.31.png" width=450 alt="图4.31"></div>

Wildar电流源的思想是将两个管子的射-基电压（源-栅电压）不一致形成的电压来实现输出的小电流。需要注意的是因为这个输出的电流对于输入电流和电源电压的依赖性小于上面电流镜的对于两者的依赖性，故这个电路是*电流源*。
##### Bipolar Wildar Current Source
对于(a)电路，可以用KVL进行分析得到，当然其中Q1Q2的$V_{BE}$并不一致：
$$
V_Tln\left(\frac{I_{IN}}{I_{OUT}}\frac{I_{S2}}{I_{S1}}\right)=I_{OUT}R_2
$$
这是一个典型的超越方程，在实际设计电路中，$I_{IN}$和$I_{OUT}$通常已知，那么可以直接对电阻进行设计。不过我们也可以意识到，在$ln$项中的$I_{IN}$受到指数倍的抑制，这使得它的性能比上一个电路良好。

对于这个电路的定量灵敏度分析，可以通过全差分方程的形式进行，对刚刚的式子两边对$V_{OUT}$求导，其中$I_{OUT}$也是$V_{CC}$的函数：
$$
V_T\frac{\partial}{\partial V_{CC}}ln\frac{I_{IN}}{I_{OUT}}=R_2ln\frac{\partial I_{OUT}}{\partial V_{CC}}
$$
最后得到：
$$
S_{V_{CC}}^{I_{OUT}}=\left(\frac{1}{1+\frac{I_{OUT}R_2}{V_T}}\right)S_{V_{CC}}^{I_{IN}}
$$
当电源电压较大时，输入电流对电源电压的灵敏度为1，假设$I_{IN}=1mA,I_{OUT}=5\mu A,R_2=27.4k\Omega$，那么可以得到$S_{V_{CC}}^{I_{OUT}}\simeq 0.16$，可见其性能比上一个电路的优势。
##### MOS Wildar Current Source
对于图(b)的MOS管Wildar电路，分析方式类似，不过由于square-law 的特性，这个结果是闭式解，可以轻松得到结果，并不需要像bipolar的电路一样进行迭代才能得到答案，

$$
\sqrt{I_{OUT}}=\frac{-\sqrt{\frac{2}{k'(W/L)_2}}+\sqrt{\frac{2}{k'(W/L)_2}+4R_2V_{ov1}}}{2R_2}
$$

对于灵敏度分析，采取同样的方法，其中$V_{ov1}$是$V_{DD}$的函数，得到：
$$
S_{V_{DD}}^{I_{OUT}}=\frac{V_{ov1}}{\sqrt{V_{ov2}^2+4I_{OUT}R_2V_{ov1}}}S_{V_{DD}}^{I_{IN}}
$$
同样假设$V_{DD}>>V_{GS1},I_{IN}\simeq V_{DD}/R_1$，则$S_{V_{DD}}^{I_{IN}}$约为1，再假设输出电流远小于输入电流，而$V_{ov2}$通常很小，则$I_{OUT}R_2\simeq V_{ov1}$，那么则有：
$$
S_{V_{DD}}^{I_{OUT}}=0.5S_{V_{DD}}^{I_{IN}}=0.5
$$

####  Peaking Current Source
上述的Wildar电流镜能提供微安级别的电流输出，而接下来的Peaking Current Source能在能够接受范围的电阻下提供纳安的电流。
##### Bipolar Peaking Current Source
<div align="middle"><img src="./pic/analog_ic_gray/图4.32.png" width=450 alt="图4.32"></div>

鉴于输出的电流很小，所以忽略Q2的基极电流，再假设 $V_A\to \infty$，由KVL有：
$$
I_{OUT}=I_{IN}exp\left(-\frac{I_{IN}R}{V_T} \right)
$$
在已知$I_{IN}$和$I_{OUT}$设计R时可以有上式的变形：
$$
R=\frac{V_T}{I_{IN}}ln\frac{I_{IN}}{I_{OUT}}
$$
假如$I_{IN}=10uA,I_{OUT}=100nA$，那么$R\simeq 12k\Omega$

定性分析这个电路，当输入电流较小时，R上的压降可以忽略不计，那么输出电流跟随输入电流，随着输入电流增大，Q1的$V_{BE1}$随着$I_{IN}$增大呈对数增大，而R的压降随$I_{IN}$变大而线性变大，那么Q2的$V_{BE2}$随着输入电流增大而逐渐变小，总而言之输出电流会随着输入电流变大而先变大后变小。如下图所示，这个最大值根据R而定，这种尖峰的存在也就是这个电路的名称由来
<div align="middle"><img src="./pic/analog_ic_gray/图4.33.png" width=450 alt="图4.33"></div>

##### MOS Peaking Current Source
对于MOS管也有一样的电路：
<div align="middle"><img src="./pic/analog_ic_gray/图4.34.png" width=450 alt="图4.34"></div>

由于M1M2的源体都连在一起可以认为它们的阈值电压一致，可以由KVL得到：
$$
V_{ov2}=V_{ov1}-I_{IN}R
$$
假如两个MOS管都在强反型区，那么很自然有：
$$
I_{OUT}=\frac{k'(W/L)_2}{2}(V_{ov1}-I_{IN}R)^2 
$$
但由于输入和输出的电流都很小，所以两个管子其实都可能工作在弱反型区，也就是两个管子的过驱动电压都小于$2nV_T$，那么漏极电流就是栅源电压的指数函数，在$V_{DS}>3V_T$时，有：
$$
I_{OUT}=\frac{W}{L}I_texp\left(\frac{V_{GS2}-V_t}{nV_T} \right)\simeq I_{IN}exp\left(-\frac{I_{IN}R}{nV_T}\right) 
$$
其中，$I_t$为M2的栅源电压为$V_t$，宽长比为1，且漏源电压远大于$V_T$时的漏极电流，$V_t$为阈值电压，$V_T$为热电压，n通常取1.5

下图展示的是在使用强反型和弱反型模型时的输出电流-输入电流关系，可以明显看到强反型关系低估了输出电流的大小。
<div align="middle"><img src="./pic/analog_ic_gray/图4.35.png" width=450 alt="图4.35"></div>

定量而言，Peak Current Source的输入输出电流关系可以表达为：
$$
I_{OUT}=I_{IN}exp\left(-\frac{I_{IN}R}{nV_T}\right) 
$$
对于MOS情况，n取1.3~1.5，对于bipolar情况，n取1

定性而言，都是一开始电阻压降较小，输入输出呈跟随状态，随着输入电流变大，电阻压降变大速度大于晶体管基射（栅源）电压变大速度，导致输出管的基射（栅源）电压变小，输出电流变小，且输出电流最大值取决于电阻。

###  Supply-Insensitive Biasing
前面我们已经介绍了Sensitivity，以及普通的电流镜和Wildar电流镜的电源敏感度，虽说Wildar电流镜已经相比普通电流镜减小了将近一半，但依旧需要进一步在结构上进行优化以实现更好的性能。

如何使得输出的量不受电源电压影响，一个思路就是用一个常量（不受电源电压影响）来控制输出量，最方便的标准就是晶体管的基-射电压或者阈值电压、热电压以及反偏pn结（齐纳二极管）的击穿电压，这些量均可以降低电源电压的影响，但前三者的问题是会受温度的巨大影响。

基-射极电压以及阈值电压有着负温度系数，在1~2mV/°C；而热电压有着正温度系数，为$k/q\simeq 86uV/°C$。

而齐纳二极管的缺点则是其需要至少7~10V的电源电压，因为标准工艺下重掺杂的结点（通常为npn晶体管发射极-基极结点）上产生最低击穿电压约为6V，此外，在反向击穿条件时，pn结会引入大量噪声。

接下来介绍基于基-射极/栅-源极电压的参考电压电路
<div align="middle"><img src="./pic/analog_ic_gray/图4.36.png" width=450 alt="图4.36"></div>

其实这个电路与Wilson电流镜类似，只是用电阻替换了二极管连接的晶体管，也可以用另一个被偏置的MOS管实现这个电阻的效果(被Allen书中引用，称为校准共源共栅电流镜)，为了使得T1能有足够的基-射电压吸收输入电流，T2产生输出电流在R2上形成对应压降。有：
$$
I_{OUT}=\frac{V_{BE1}}{R_2}=\frac{V_T}{R_2}ln\frac{I_{IN}}{I_{S1}} 
$$
再根据灵敏度的定义有：
$$
S_{V_{CC}}^{I_{OUT}}=\frac{V_T}{V_{BE(on)}}S_{V_{CC}}^{I_{IN}} 
$$
在$V_{CC}>>V_{BE(ON)}$时，$I_{IN}\simeq V_{CC}/R_1$那么$S_{V_{CC}}^{I_{IN}}$约等于1，在取$V_{BE(on)}=0.7,V_T=0.026$时，$S_{V_{CC}}^{I_{OUT}}\simeq 0.037$，可见其受电源电压影响已经变小很多。

对于b图的MOS情况，
$$
I_{OUT}=\frac{V_{GS1}}{R_2}=\frac{V_t+\sqrt{\frac{2I_{IN}}{k'(W/L)_1}}}{R_2} 
$$
其输出阻抗为：
$$
R_{OUT}\simeq g_{m2}g_{m1}r_{o1}r_{o2}R_2 
$$
可以认为是反馈放大了其输出阻抗，是典型的Gain-Boosting

如果输入电流较小，且T1的宽长比较大，那么可以认为输出电流取决于阈值电压，因此这个电路被称为*阈值基准 threshold-referenced*，进行灵敏度的求解：
$$
S_{V_{DD}}^{I_{OUT}}=\frac{V_{ov1}}{2I_{OUT}R_2}S_{V_{DD}}^{I_{IN}}=\frac{V_{ov1}}{2V_{GS1}}S_{V_{DD}}^{I_{IN}} 
$$
假设阈值电压为1V，过驱动为0.1V，同时$S_{V_{DD}}^{I_{IN}}\simeq 1$，则$S_{V_{DD}}^{I_{OUT}}\simeq 0.045$

这个电路不是完全隔离于电源电压因为其集电极/漏极几乎正比于电源电压，这种灵敏度问题在输入电流来自于电源端到电阻产生的偏置电路中尤为明显，会导致电路中某些部分的电流随电源电压变化。

此外，这个结构在偏置中极为常见，但不同的书中对这个结构有不同的讲解，甚至连名字都不一样，
例如在Gary的书中，这种结构叫*阈值基准*，在Allen书中，这个结构叫*调制共源共栅电流镜*，马丁的书中则是并没有提及这个结构，且只是简单对比了Wilson电流镜和cascode电流镜，而在拉扎维的书中甚至没有介绍Wilson电流镜和这个结构，于本人而言，叫这个结构为电流镜有些不妥，因为它本身如果按照Gary的用法使用，其并不直接复制输入电流，而是一个基准源，此外，由于其中环路的存在，哪怕它具有和cascode结构类似的输出阻抗，其环路造成的不稳定仍然使其作为电流镜的功能有待商榷，不过这个结构终究是源自于Wilson电流镜，其发明是由于在三极管时代cascode结构受到$\beta$偏差影响较大，而Wilson电流镜能较好抑制这一误差，这一点在前面分析过，不过到了MOS管时代，这个优势也就无从说起了。

###  Self-Biasing
其实这一章在Gary书中是隶属于Supply-Insensitive Biasing下的，但其使用之广泛，就单独提出来了。

在上文的分析中，可以看到敏感度的一个很大因素是被输入电流和电源电压直接的关系所恶化，那么通过输出反过来再控制输入，就可以进一步减弱敏感度，这种手段就叫*自偏置self-biasing*或者*自举bootstrap*(自举的定义以及使用更加广泛，可以简单认为是输入和输出同时同步同向变化所引起的效果)

下图展示了这种自偏置的思路以及工作点定义，其中电流镜保持1：1复制。（实线的$I_{IN}-I_{OUT}$曲线取自于阈值基准的关系）
<div align="middle"><img src="./pic/analog_ic_gray/图4.37.png" width=450 alt="图4.37"></div>

Gary提到了自偏置的两个条件，一个是“转移”，在上图中即电流源的输入输出关系，一个是“跟随”，即上图中输入跟随输出，不过在一些结构中，只需要跟随就能达到*自举*的效果。

很明显这是一个正反馈电路，但只要其环路增益小于1，那么依然能保持稳定，可以注意到有两个稳定点，一个是期望的工作点，一个是不期望的0点，理论上设计0点的环路增益大于1，便可以自动收敛到期望的工作点。

但在实际中由于低电流工作点时极小的跨导，使得大于1的环路增益不能实现，便需要*启动电路start-up citcuit*注入电流使得电路向正常工作点收敛。

下图展示的是以$V_{BE}$基准和$V_t$基准为例的自偏置电流基准（在Allen的书中，这个结构才被称为$V_t$基准源，中文名为自举基准）

<div align="middle"><img src="./pic/analog_ic_gray/图4.39.png" width=300 alt="图4.39"></div>

其中T3T6是复制电流出去的管子，而在左侧加入了启动电路，这个电路的输出电流分析并不困难，但求解困难会遇到麻烦，比如bipolar的$V_{BE}$基准因为电流源是超越方程故而解出输出电流并不现实，不过我们可以简单取$I_{OUT}\simeq \frac{V_{BE(on)}}{R}$作为输出，就这个结果可以看出输出电流已经和电源电压关系不大了。

对于MOS的自举基准,忽略沟道长度调制效应：
$$
I_{OUT}R=V_t+\frac{2I_{IN}}{\mu _nC_{ox}(W/L)_1} \\
I_{IN}=I_{OUT} \\
I_{OUT}=\frac{V_t}{R}+\frac{1}{\mu _nC_{ox}(W/L)_1R^2}+\frac{1}{R}\sqrt{\frac{2V_t}{\mu _nC_{ox}(W/L)_1R}+\frac{1}{(\mu _nC_{ox}(W/L)_1)^2R^2}}
$$
那么其实输出电流近似为$I_{OUT}\simeq \frac{V_t}{R}$，也与电源电压近似无关

对于(a)中的启动电路，在电路位于0点时，T1的集电极处于低电位，而左侧存在4个导通二极管的$V_{BE(on)}$，使得D1导通向主体电路通电，使得Rx上的压降变大，可以调整Rx的阻值使得当电路处于正常工作点时D1处于关断状态，即T1的集-射压差为两个开启电压，而设置$I_{IN}R_X$为两个开启电压即可。

在(b)中不使用二极管方法，因为浮空二极管在MOS工艺中并不可行，在电路处于0点时，T1的栅极为低电平，在经过T7T8之后在T9形成高电平使得其导通（T7关断，T8三极管区），进而将T4T5的栅极拉低从而启动电路。

此外，启动电路除了能启动电路以外还需要做到：尽可能走小电流以减小功耗；在主电路开启之后不影响主电路或最好关闭以减小功耗。

接下来介绍一个参数：分式温度系数（fractional temperature coefficient），对于输出电流的结构，其计算公式为：
$$
TC_F=\frac{1}{I_{OUT}}\frac{\partial I_{OUT}}{\partial T}
$$
很明显，它表示了输出变化量受温度的影响，比如对于$V_{BE}$基准电路：
$$
I_{OUT}=\frac{V_{BE}}{R} \\
\frac{\partial I_{OUT}}{\partial T}=\frac{1}{R}\frac{\partial V_{BE}}{\partial T}-\frac{V_{BE}}{R^2}\frac{\partial R}{\partial T} \\
TC_F=\frac{1}{I_{OUT}}\frac{\partial I_{OUT}}{\partial T}=\frac{1}{V_{BE}}\frac{\partial V_{BE}}{\partial T}-\frac{1}{R}\frac{\partial R}{\partial T}
$$
同理，$V_t$基准电路的分式温度系数为：
$$
TC_F=\frac{1}{I_{OUT}}\frac{\partial I_{OUT}}{\partial T}\simeq \frac{1}{V_t}\frac{\partial V_t}{\partial T}-\frac{1}{R}\frac{\partial R}{\partial T}
$$
在这里我们可以看到一些情况：对于$V_{BE}$而言，它的温度系数是负数，如果电阻的温度系数是正数，那么$V_{BE}$基准电路的温度系数会很大，也就是说它的温度性能并不好，这或许也是它如今使用不多的原因之一。当然，如果温度系数中的温度函数并不是一个常数，那么求出这个电路的温度系数也许意义不大，所以现在评估一个电路的温度性能采用的是温漂系数，取其在温度测量范围中的最值差除以整个测量区间作为导数：
$$
TC=\frac{X_{max}-X_{min}}{X_{nominal}(T_{max}-T_{min})}
$$
其中X为测量的变量，可以是电流，也可以是电压。

在CMOS电路中也可以用$V_{BE}$基准电路，如下图所示，因为上面的电流镜，导致M2和M3的栅源电压一致，进而使得输出电流由Q1的$V_{BE}$和电阻$R$决定

<div align="middle"><img src="./pic/analog_ic_gray/图4.40.png" width=450 alt="图4.40"></div>

进而有
$$
I_{OUT}=\frac{V_{BE}}{R} 
$$

同时，在bipolar电路中也可以实现$V_T$基准（热电压基准），这会用到前面讲过的Wildar电流源：

<div align="middle"><img src="./pic/analog_ic_gray/图4.41.png" width=450 alt="图4.41"></div>

根据Wildar 电流源公式：
$$
V_Tln\left(\frac{I_{IN}}{I_{OUT}}\frac{I_{S2}}{I_{S1}}\right)=I_{OUT}R_2
$$
由于加入了Q3Q4的电流镜，导致$I_{IN}=I_{OUT}$，为了使得电路的0工作点的环路增益大于1进而促使电路趋向理想工作点，Q2的发射极面积为Q1的发射极面积的两倍，也就是$I_{S2}=2I_{S1}$，故有：
$$
I_{OUT}=\frac{V_T}{R_2}ln2
$$
对于这个电路的分式温度系数可以得到：
$$
TC_F=\frac{1}{V_T}\frac{\partial V_T}{\partial T}-\frac{1}{R_2}\frac{\partial R_2}{\partial T}
$$
对于正温度系数的热电压和正温度系数的扩散电阻，它们的互相抵消会使得电路的温度系数更小，表现为更好的温度效果。

在CMOS中也可以形成$V_T$基准，如下图所示
<div align="middle"><img src="./pic/analog_ic_gray/图4.42.png" width=450 alt="图4.42"></div>

其中M5和M6匹配，以实现复制的功能，M3与M4匹配，进而它们的源电位相同，得到：
$$
V_{BE1}=I_{OUT}R+V_{BE2}
$$
其中Q2的射极面积为Q1的n倍，故而有：
$$
I_{OUT}=\frac{V_Tln(n)}{R} 
$$
需要注意的是，由于MOS管M3M4的失配或者沟道长度调制效应，会导致它们有着不同的漏源电压，而电阻R上的压降通常很小，比如100mV，那么M3M4源极电位的小小偏差就可能导致巨大的误差，所以在实践中常常使用cascode或者wilson电流镜以减小偏差，当然在全工艺中，往往使用cascode结构，它除了能减弱沟道长度调制效应带来的误差，还能增强电路的PSRR，唯一的问题可能就是它要使用较高的电压裕度。

可以看到，在一些基准电路中我们会故意制造管子之间的不对称，这种不对称的原因是为了形成自举，就以CMOS中的$V_T$基准（图4.42）为例，假如两边的bipolar管一致，那么输出电流就为0，也就是转移和复制的关系被唯一收敛到0点，而只有假如不对称导致转移关系偏移形成另一个我们期望的解，才能保证电路能输出预期值，接下来看一个经典的电路
<div align="middle"><img src="./pic/analog_ic_gray/图4.42.s.png" width=450 alt="图4.42.s"></div>

这个电路被称为*constant-transconductance*，这个名字的由来接下来会解释，以其中的（a）图为例，可以看到M2和M1就有明显的不对称，根据电流关系有：
$$
V_{ov1}+V_{t1}=V_{ov2}+V_{t2}+I_{OUT}R_S \\
假设两个阈值电压一致： \\
I_{OUT}R_S=\sqrt{\frac{2I_{OUT}}{\mu _nC_{ox}(W/L)_N}}-\sqrt{\frac{2{I_{OUT}}}{\mu _nC_{ox}K(W/L)_N}} \\
I_{OUT}=\frac{2}{\mu _nC_{ox}(W/L)_N}\frac{1}{R_S^2}\left(1-\frac{1}{\sqrt{K}} \right)^2
$$
虽然这个结构类似于bipolar的$V_T$基准，但就结果而言，这个结果即不和$V_T$有关，也极不美观，难以看出它在电路结构上的理解方法，这是由于ln函数和sqrt函数以及bipolar管和MOS管对于热电压/阈值电压的区别，也就是由于晶体管本身的转移性质导致了结果的不同，但分析方法一致。

需要注意的是，我们在上述计算过程中忽略了体效应，也就是说实际上M1M2的阈值电压并不一致，由于M2的源极更高一些，会导致M2的阈值电压也相应较高，导致实际电流比理论值小一些，所以为了恢复到原来预期的电流，可以修改管子的比例K，或者调制电阻R，**一般设计而言取K为4**，因为这样根号4取2较为方便计算，而跨导也可以直接表示为$1/R_{S}$。当然，也可以采取（b）图的方法，使得偏差管的体和源相连，这一点可以在版图上进行隔离进而实现。此外，沟道长度调制效应会导致电路受到外部电压的影响，比如电源电压，虽然从公式上看输出电流不受电源电压的影响，但在小信号角度而言，电源波纹（ripple）会影响电路性能，故而可以增长管子的长度或者使用cascode结构。

接下来看一看这个电路的一些细节问题：
$$
g_{m1}=\sqrt{2\mu _nC_{ox}(W/L)_NI_{OUT}} \\
g_{m1}=\frac{2\left(1-\sqrt{1/K} \right)}{R_S} \\
g_{m2}=\frac{2\left(\sqrt{K}-1 \right)}{R_S}
$$
可以看到这个跨导仅由工艺参数和电阻决定，故而称为*constant-transconductance*。

接下来看这个典型的Wildar电流镜以及其错误电路的环路分析
<div align="middle"><img src="./pic/analog_ic_gray/图4.42.s1.png" width=450 alt="图4.42.s1"></div>

前面提到，管子的不对称和电阻的引入是为了转移关系和复制关系能在非零点有一个稳定解，从另一个说法来看，也可以认为是在预期工作条件下能够有稳定的环路关系。

对于上图图1进行环路分析，从M1和M2的栅极断开加入一个测试电压$v_t$：
$$
v_t\times \frac{g_{m2}}{1+g_{m2}R_S}\times \frac{1}{g_{m3}}\times g_{m4}\times \frac{1}{g_{m1}}=v_{out} \\
g_{m3}=g_{m4};g_{m2}=\sqrt{K}g_{m1} \\
Loop Gain=\frac{v_{out}}{v_t}=\frac{\sqrt{K}}{1+g_{m2}R_S}
$$
可以看到图1的环路反馈虽然大于0但是小于1，故而稳定

同理在图2加入相同的方法测试：
$$
v_t\times g_{m2}\times \frac{1}{g_{m3}}\times g_{m4}\times (r_{o4}\parallel (\frac{1}{g_{m1}}+R_S))=v_{out} \\
g_{m3}=g_{m4};g_{m1}=\sqrt{K}g_{m2} \\
Loop Gain=\frac{v_{out}}{v_{in}}=g_{m2}\times (r_{o4}\parallel (\frac{1}{g_{m1}}+R_S))
$$
可以看到图（b）中的反馈不仅大于零还大于1，所以其预期工作状态并不稳定，这是因为$R_S$在图一作为M2的退化电阻，而在图（b）中作为M1串联的电阻提高了增益。

不过其实如果理解自举基准的原理，也就不会有图（b）的错误产生，为了在电流源产生转移关系的偏移，必然是在输出的管下面加入电阻配合管子的宽长变化。