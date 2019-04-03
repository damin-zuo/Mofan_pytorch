#activation function
import torch        # relu, sigmoid, tanh激励函数在这
import torch.nn.functional as F     # softplus激励函数在这
import matplotlib.pyplot as plt
from torch.autograd import Variable

a = torch.linspace(-5,5,200)
x = Variable(a)
x_np = x.data.numpy()  #from Variable to tensor to numpy for matplot drawing

#activation function
y_relu = torch.relu(x).data.numpy()
y_sigmoid= torch.sigmoid(x).data.numpy()
y_tanh = torch.tanh(x).data.numpy()
y_softplus = F.softplus(x).data.numpy()  #from torch.nn.functional

plt.figure(1, figsize=(8, 6))
plt.subplot(221)
plt.plot(x_np, y_relu, c='red', label='relu')
plt.ylim((-1, 5))
plt.legend(loc='best')

plt.subplot(222)
plt.plot(x_np, y_sigmoid, c='red', label='sigmoid')
plt.ylim((-0.2, 1.2))
plt.legend(loc='best')

plt.subplot(223)
plt.plot(x_np, y_tanh, c='red', label='tanh')
plt.ylim((-1.2, 1.2))
plt.legend(loc='best')

plt.subplot(224)
plt.plot(x_np, y_softplus, c='red', label='softplus')
plt.ylim((-0.2, 6))
plt.legend(loc='best')

plt.show()
