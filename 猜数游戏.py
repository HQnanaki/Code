#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random


# In[5]:


def guess():
    #生成随机数
    a=random.randint(0,100)
    #count计数 一共采了多少次
    count=1
    while True:
        c=input("请输入一个0到100的整数")
        c=int(c)
        if c>100 or c<0 :    # 还可以进一步判断，用户如果输入的不是数字，而是字符串，应该如何处理？
            print("不在范围内，请重新输入一个数字，本次猜测不计数")
            continue
        if c<a:
            print("输入数比随机数小")
            count+=1           
        if c>a:
            print("输入数比随机数大")
            count+=1
        if c==a:
            print("正确，共猜测%d次"%(count))   # 这种用 % 的字符串格式化输出，逐渐抛弃，建议熟悉 f字符串的输出方法
            break
            #若猜中，则退出循环


# In[6]:


guess()


# In[ ]:




