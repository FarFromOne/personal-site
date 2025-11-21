# Output Stages

##  CMOS Class AB Output Stages
###  Common Drain Configuration

<div align="middle"><img src="./pic/analog_ic_gray/pic_5.31.png " width=450 alt="图5.31"></div>

###  Common-Source Configuration With Error Amplifiers
接下来介绍的*误差放大器辅助的共源结构*其核心思想其实是*super-source-follower*或者说*gm-boosting*，通过误差放大器对比输入与输出，进而调整输出管来控制输入与输出一致

<div align="middle"><img src="./pic/analog_ic_gray/pic_5.32.png " width=450 alt="图5.32"></div>

根据反馈或者直接分析可以得到该结构的输出阻抗为

$$
R_o=\frac{1}{(g_{m1}+g_{m2})A}\parallel r_{o1} \parallel r_{o2}
$$
在分析计入运放的失调之前，先进行一些约定：$k_p'(W/L)_1=k_n'(W/L)_2$以及$-V_{t1}=V_{t2}=V_t$，并且在输入电压，两个运放的失调电压为0时，$-I_{D1}=I_{D2}=I_Q$

进而有：
$$
V_{gs1}=-V_t-V_{ov} \\
v_{gs2}=V_t+V_{ov} \\
其中V_{ov}=\sqrt{\frac{2I_Q}{k'(W/L)}}
$$
<div align="middle"><img src="./pic/analog_ic_gray/pic_5.34.png " width=450 alt="图5.34"></div>

接下来加入失调电压，那么对于上面的误差放大器，其差分输入从0变为$V_o-V_i+V_{OSP}$，同理，下面的放大器，其差分输入从0变为$V_o-V_i-V_{OSN}$。那么两个输出管的栅源电压也因为失调电压产生了一定的偏差：
$$
V_{gs1}=-V_t-V_{ov}+A[V_o-(V_i-V_{OSP})] \\
V_{gs2}=V_t+V_{ov}+A[V_o-(V_i+V_{OSN})]
$$
进而结合MOS管在饱和区的转移方程，输出电流$I_o=V_o/R_L$，以及KCL，得到：
$$
V_o=\frac{V_i-\frac{V_{OSP}V_{OSN}}{2}}{1+\frac{1}{k'\frac{W}{L}A[2V_{ov}-A(V_{OSP}-V_{OSN})]R_L}}
$$
观察这个结果可以得到两个重要的结论：

在失调电压$V_{OSP}=V_{OSN}=0$时
$$
V_o\simeq V_i\left(1-\frac{1}{2Ag_mR_L}\right)
$$
在这个结论中可以看到，$2Ag_mR_L$为环路增益，$A,g_m,R_L$增大都会使增益误差变小，跟随效果更好。

在考虑失调电压时，$A(V_{OSP}-V_{OSN})\ll 2V_{ov}$以及$2Ag_mR_L\gg 1$时
$$
V_o\simeq V_i-\frac{V_{OSP}+V_{OSN}}{2}
$$
于大信号分析而言，上述关系于两个输出管工作在饱和区有效，而当输入变大或减小到一定数值时，输出也跟随变大或减小，但由于跟随的增益小于1，导致误差放大器的差分输入减少或减小，即当$V_i$上升到一定程度时，误差放大器输入减小，使得放大器输出减小，进而上方的MOS管的$I_d$变大，而下方的MOS管$I_d$变小，再进一步使得下方MOS管关断，对于$V_i$下降则相反。

这种输出级的优势相比上一种在于其进一步增大了输出摆幅，也就是多了一个阈值电压的摆幅。但这个结果也有两个问题，**第一个就是由于为了强化高频速度，增加带宽时必须的，但与此同时会影响结构的稳定性，第二个就是误差放大器的失调电压对静态电流的影响，大的静态电流可以减小交越失真，但同时会增大功耗，以及减小输出摆幅。**

控制静态电流的方法，可以通过反馈进行稳定，还可以通过减小误差放大器的增益控制，这里介绍后面的方法。这种方法也就是通过减少误差放大器的增益，减少失调对于输出管的栅压影响。

定义无失调时$V_i=0$的静态电流$I_Q=\frac{I_{D2}-I_{D1}}{2}$，注意漏电流是从漏级流入，源流出。考虑失调电压和误差放大器增益的静态电流为：
$$
I_Q=\frac{k'}{4}\frac{K}{L}\left((V_{ov}+A[V_o+V_{OSN}])^2+(-V_{ov}+A[V_o+V_{OSP}])^2\right)
$$
在不考虑失调电压时，此时输出电压为0($V_i$=0)，静态电流为：
$$
I_Q=\frac{k'}{2}\frac{K}{L}\left(V_{ov}\right)^2
$$
代入前面得到的考虑失调电压下输入输出电压关系到考虑失调电压的静态电流关系式中,并且取$V_i=0$，得到：
$$
I_Q=\frac{k'}{2}\frac{W}{L}\left(V_{ov}-A\left[\frac{V_{OSP}-V_{OSN}}{2}\right]\right)^2
$$
定义由于失调导致的静态电流差为$\Delta I_Q$:
$$
\Delta I_Q=I_Q|_{\substack{V_{OSP}=0 \\V_{OSN}=0}}-I_Q=\frac{k'}{2}\frac{K}{L}A(V_{OSP}-V_{OSN})\left[V_{ov}-A\left(\frac{V_{OSP}-V_{OSN}}{4}\right) \right]
$$
再定义误差静态电流与理论静态电流的比值用以衡量偏差比：
$$
\frac{\Delta I_Q}{I_Q|_{\substack{V_{OSP}=0 \\V_{OSN}=0}}}=A\left(\frac{V_{OSP}-V_{OSN}}{V_{ov}} \right)\left[1-\left(\frac{V_{OSP}-V_{OSN}}{4V_{ov}}\right) \right] \\
\simeq A\left(\frac{V_{OSP}-V_{OSN}}{V_{ov}}\right)  当A(V_{OSP}-V_{OSN})\ll 4V_{ov}时
$$
根据如上的关系式，我们可以看出，如果已知失调电压大小，以及需要设计的静态电流的误差量，就可以反推出误差放大器的最大增益：
$$
A<\left(\frac{V_{ov}}{V_{OSP}-V_{OSN}} \right)\left(\frac{\Delta I_Q}{I_Q|_{\substack{{V_{OSP}=0} \\V_{OSN}=0}}} \right)
$$
下图展示了一个利用误差放大器的输出级电路，包括了其中的误差放大器：
<div align="middle"><img src="./pic/analog_ic_gray/pic_5.35.png " width=450 alt="图5.35"></div>
该图仅展示了上半部分，即输入到上方误差放大器到上半部分输出管，对称的下半部分结构没有展示。

这一部分的gary的电路分析有些难以苟同，原论文(H. Khorramabadi. “A CMOS Line Driver with 80 dB Linearity for ISDN Applications,” IEEE Journal of Solid-State Circuits, Vol. 27, pp. 539–544, April 1992.)则是直接给出了放大器主体管的作用进而直接得到放大增益，这里给出个人分析思路：

该电路左边部分，即$I_{BIAS}$，M17M13M15构成了Wilson电流镜，用以构成偏置电流，为了控制整体增益，负载是M15和M16（原论文中依靠这两个$1/g_m$的负载把整体增益控制在7），其中M13和M14负责电流镜结构，使得M13和M15的小信号电流复制到M14，使得M12的跨导不被浪费，即整体跨导为$G_m=g_{m11}=g_{m12}$，而输出阻抗则为$R_{OUT}=1/g_{m15}=1/g_{m16}$（未考虑体效应），则最后放大器的增益为：$A=G_mR_{OUT}=\frac{g_{m11,12}}{g_{m15.16}}$。

此外有一些小细节需要注意，M13和M14对M17进行复制，故有：
$$
I_{D13}=I_{D14}=-I_{BIAS}\frac{(W/L)_{13}}{(W/L)_{17}}
$$
此外，根据KCL，有：$I_{D16}=-I_{BIAS}\frac{(W/L)_{13}}{(W/L)_{17}}+\frac{I_{TAIL}}{2}$，那么可以知道$|I_{D14}|=I_{BIAS}\frac{(W/L)_{13}}{(W/L)_{17}}>I_{TAIL}$。

对于M1，其也是M17的复制，$I_{D1}=-I_{BIAS}\frac{(W/L)_{1}}{(W/L)_{17}}$，当然实际上输出的静态电流会受到失调电压的影响，以及沟道长度调制效应（即输出电压）的影响，此处均不考虑，也就是$V_{OSP}=0,V_i=0,V_o=0$，在实际设计中，会取$(W/L)_1\gg (W/L)_{17}$，以减小偏置电流的功耗。