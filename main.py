# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import numpy as np
import matplotlib.pyplot as plt

#linear model
x_data=[1.0,2.0,3.0]
y_data=[2.0,4.0,6.0]

def forward(x):
    return x*w+b

def loss(x,y):
    y_pred=forward(x)
    return (y_pred-y)*(y_pred-y)

w_list=[]
b_list=[]
mse_list=[]

for w,b in zip(np.arange(0.0,4.1,0.1),np.arange(0.0,4.1,0.1)):
    print('w=',w,'b=',b)
    l_sum=0

    for x_val,y_val in zip(x_data,y_data):
        y_pred_val=forward(x_val)
        loss_val=loss(x_val,y_val)
        l_sum+=loss_val
        print('\t',x_val,y_val,y_pred_val,loss_val)
    print('MSE=',l_sum/3)
    w_list.append(w)
    b_list.append(b)
    mse_list.append(l_sum/3)

ax=plt.figure().add_subplot(projection='3d')


xx,yy=np.meshgrid(w_list,b_list)
mse_list=loss(xx,yy)
ax.plot_surface(xx,yy,mse_list,linewidth=0.2,antialiased=True)









# plt.plot(w_list,mse_list)

plt.show()




