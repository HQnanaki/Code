# List综述
## 列表(List)的基本知识和应用特点：
序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。序列都可以进行的操作包括索引，切片，加，乘，检查成员。  
Python有包括 str 、tuple 、list 在内的多个内置序列。列表（List）是一种常见的序列类型，Python中的列表除了可以保存多个数据内容之外，也可以动态地实现对数据的修改。


```python
#列表的定义
list=['apple','banana',23,-6,'dog','tiger','giraffe']
#列表的访问和切片
print(list[0])
print(list[1:4])
```

    apple
    ['banana', 23, -6]
    


```python
#计算列表长度
print(len(list))
#反向访问列表中的数据
for i in range(-1,-len(list)-1,-1):
    print(list[i],end='、')
```

    7
    giraffe、tiger、dog、-6、23、banana、apple、


```python
#列表的乘法和连接
list_1=list*3
print(list_1)
list_2=['cat','mike',3]
list_3=list_2+list
print(list_3)
```

    ['apple', 'banana', 23, -6, 'dog', 'tiger', 'giraffe', 'apple', 'banana', 23, -6, 'dog', 'tiger', 'giraffe', 'apple', 'banana', 23, -6, 'dog', 'tiger', 'giraffe']
    ['cat', 'mike', 3, 'apple', 'banana', 23, -6, 'dog', 'tiger', 'giraffe']
    


```python
#按步长截取数据
print(list_1[0:12:2])
#按步长替换数据
list_1[0:12:2]=['wow']*6
list_1[1:7:2]=['change_1','change_2','change_3']
print(list_1)
```

    ['wow', 'wow', 'wow', 'wow', 'wow', 'wow']
    ['wow', 'change_1', 'wow', 'change_2', 'wow', 'change_3', 'wow', 'apple', 'wow', 23, 'wow', 'dog', 'tiger', 'giraffe', 'apple', 'banana', 23, -6, 'dog', 'tiger', 'giraffe']
    


```python
#在最后追加数据
list.append('z')
print(list)
#在列表指定位置插入数据
list.insert(1,'z')
print(list)
#列表最后扩充列表
list.extend(['e1','e2'])
print(list)
```

    ['apple', 'banana', 23, -6, 'dog', 'tiger', 'giraffe', 'z']
    ['apple', 'z', 'banana', 23, -6, 'dog', 'tiger', 'giraffe', 'z']
    ['apple', 'z', 'banana', 23, -6, 'dog', 'tiger', 'giraffe', 'z', 'e1', 'e2']
    


```python
#删除列表中第一个值为z的数据
print(list)
list.remove('z')
print(list)
#根据索引删除数据
del list[3]
print(list)
```

    ['apple', 'z', 'banana', 23, -6, 'dog', 'tiger', 'giraffe', 'z', 'e1', 'e2']
    ['apple', 'banana', 23, -6, 'dog', 'tiger', 'giraffe', 'z', 'e1', 'e2']
    ['apple', 'banana', 23, 'dog', 'tiger', 'giraffe', 'z', 'e1', 'e2']
    


```python
a=['cat','dog','tiger']*2
print(a.count('cat'))
```

    2
    


```python
#列表数据查找，默认从第一个数据开始查找，输出第一次碰到这个数时的索引
print(a.index('cat'))
#从第三个数开始查找
print(a.index('cat',2))
#找不到，报错
print(a.index('cat',5))
```

    0
    3
    


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-11-1d39fd443de3> in <module>
          1 print(a.index('cat'))
          2 print(a.index('cat',2))
    ----> 3 print(a.index('cat',5))
    

    ValueError: 'cat' is not in list


## 列表与数组之间的异同
1、列表和数组都是序列的一种类型，可以相互转换
2、列表中可以含有不同类型的数据，但数组中的数据必须是相同的
3、一个numpy array 是内存中一个连续块，并且array里的元素都是同一类（例如整数）。所以一旦确定了一个array，它的内存就确定了，那么每个元素（整数）的内存大小都确定了（4 bytes）。  
list中的每个元素其实是一个地址的引用，这个地址又指向了另一个元素，这些元素的在内存里不一定是连续的。所以list其实是只能塞进地址的“数组”，而且由于地址不用连续，每当我想加入新元素，我只用把这个元素的地址添加进list。


```python
import numpy as np
```


```python
#列表和数组可以相互转换
a1=[1,2,3,4,5]
b1=np.array([1,3,7,9])
print(type(a1),type(b1))
a1_array=np.array(a1)
b1_list=b1.tolist()
print(type(a1_array),type(b1_list))
```

    <class 'list'> <class 'numpy.ndarray'>
    <class 'numpy.ndarray'> <class 'list'>
    


```python
#列表对象中可以包含不同的类型的数据
a=[1,'a',[2,3]]
b=np.array([1,2,3])
```


```python
#列表和数组
```
