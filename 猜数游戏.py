#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[3]:


def guess():
    #生成随机数
    a=random.randint(0,100)
    #count计数 一共采了多少次
    count=1
    while True:
        c=input("请输入一个整数")
        c=int(c)
        if c<a:
            print("输入数比随机数小")
            count+=1           
        if c>a:
            print("输入数比随机数大")
            count+=1
        if c==a:
            print("正确，共猜测%d次"%(count))
            break
            #若猜中，则退出循环


# In[4]:


guess()


# In[ ]:




