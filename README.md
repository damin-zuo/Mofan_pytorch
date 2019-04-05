# Mofan_pytorch
Mofan tutorial for pytorch
深度学习入门阶段
背景：生物医学工程博士生，德国亚琛工大医学院，做过C++的数据处理，用模型模拟仿真药物在体内的代谢过程；研究生主要使用MATLAB做图像处理。
基础：C++编程（2年，以前学过C）， MATLAB编程（六年，本科研究生一直使用MATLAB），上完了莫凡的Python课程（numpy,pandas和matplotlib），opencv基础，Andrew Ng的机器学习课程上了一半（MATLAB）。
目的：使用Python学会深度学习的框架pytorch，并应用在医学影像上。
学习材料：Mofan课程，周志华《机器学习》，Sentdex machine learning视频，百面机器学习
内容：记录pytorch学习过程中遇到的问题以及解决方案。
准备：anaconda，Python，pytorch，pycharm环境
目录：
1 20190403，pytorch神经网络基础
1.1 torch_numpy.py  torch和numpy运算类似，矩阵乘积（matrix multiplication）要注意（np.matmul, torch.mm）
1.2 Variable.py     Variable功能已经不在torch里使用，函数还可以用
1.3 AF.py
    Activation function: y=AF(Wx)，让神经网络可以描述非线性问题。
    relu=max(0,x)， rectifier Linear Unit，适用于卷积神经网络(Convolutional neural networks)，循环神经网络（recurrent neural networks）
    softplus=log(1+ex)   
    tanh=(e-x-ex)/(e-x+ex)，适用于循环神经网络（recurrent neural networks）
    sigmoid=1/(1+e-x) 
2 20190403，Neural Network(nn)基础
2.1 regression.py 基础神经网络，线性回归
    SGD, schomatic gradient descent
    



