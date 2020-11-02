#!/usr/bin/env python
# coding: utf-8

# In[1]:


#循环算法
def Fibonacci_f(num):
    #如果num<2时，生成特定的数列
    if num == 0:
        print("0")   # 这几个可以省略
    elif num == 1:
        print ("1")
    elif num ==2:
        print ("1,1")
    else:
        #建立斐波那契数列
        Fib_list=[1,1]
        for i in range(2,num):
            Fib_list.append(Fib_list[i-1]+Fib_list[i-2])
        return (f'{Fib_list}') 


# In[2]:


#递归算法
def Fibonacci_d(num):
    if num == 1 or num == 2:
        return 1
    else:
        m=Fibonacci_d(num-1)+Fibonacci_d(num-2)
        return m


# In[3]:


#迭代器对象方法
class Fibonacci_i:   # //需要增加初始化方法
    #用前一个和前两个数字的值作为对象的属性
    def __iter__(self):
        self.before_1 = 1
        self.before_2 = 1
        return self
    #定义next方法
    def __next__(self):
        num = self.before_1 + self.before_2
        self.before_2 = self.before_1
        self.before_1 = num
        return num


# In[4]:


#生成器方法
def fibonacci_g(num):
    before_1,before_2,count=1,0,0
    while count<num:
        f_num=before_1+before_2
        yield f_num
        before_2=before_1  # //这句与yield前面、还有下面一句，合并。
        before_1=f_num
        count+=1


# In[5]:


import numpy as np


# In[6]:


#矩阵方法
def Fibonacci_m(num):
    base=np.mat([[1,1],[1,0]])
    n=base
    for i in range(num):
        if i == 0:
            print('1',end='、')
        else:
            print(n[0,0],end='、')
            n=n*base


# In[8]:


if __name__=='__main__':
    num=input('请输入斐波那契数列的项数')
    try:
        num = int(num)
    except ValueError:
        print("输入错误，请输入一个整数")
    print(f"循环方法生成的{num}项斐波那契数列")
    print(Fibonacci_f(num),end='、')
    print(f"\n由递归方法生成的{num}项斐波那契数列")
    for i in range(1,num+1):
        print(Fibonacci_d(i),end='、')
    print(f"\n由生成器方法生成的{num}项斐波那契数列")
    f=fibonacci_g(num)
    for i in range(num):
        if i==0:
            print(1,end='、')
        else:
            print(next(f),end='、') 
    print(f"\n由迭代器方法生成的{num}项斐波那契数列")
    out=Fibonacci_i()
    out_iter=iter(out)
    #输出斐波那契数列的前两个数字
    print(f'{out.before_1}、{out.before_2}',end='、')
    for i in range(num-2):
        print(next(out),end='、')
    print(f"\n由矩阵方法生成的{num}项斐波那契数列")
    Fibonacci_m(num)

