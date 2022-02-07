import torch
import numpy as np

x = torch.empty(5,4)
print(x)

x1 = torch.ones(3,3)
print(x)

x2 = torch.zeros(2)
print(x)

x3 = torch.rand(5,6)
print(x)


######## list, numpy to tensor ############
l = [13,4]
r = np.array([4,56,7])
l2t = torch.tensor(l)
r2t = torch.tensor(r)

print(l2t)
print(r2t)

########### size, type, calc ##############
print(x.size())
print(x.size()[1])
print(type(x))

x = torch.rand(2,2)
y = torch.rand(2,2)
print(x+y)
print(torch.add(x,y))
print(y.add(x))
print(y)
print(y.add_(x))
print(y)

############## transform ################
x = torch.rand(8,8)
print(x.size())
a = x.view(64)
print(a.size())
b = x.view(-1,4,4)
print(b.size())

############## tensor to numpy ###############
x = torch.rand(8,8)
y = x.numpy()
print(type(y))

############## tensor to value ##############
x = torch.ones(1)
print(x.item())
