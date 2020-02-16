#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
a = np.array([1,3,4],int)
for x in a:
    print(x)
b = np.array([[1,2,3],[3,4,5]],float)
for y in b:
    print(y)
for X,Y,Z in b: #X,Y,X는 b행렬에서 각 행의 원소 수와 동일해야 연산 가능
    print(X*Y*Z)


# In[14]:


a = np.array([[1,2,3],[4,5,6]],int)
print(a.sum())


# In[15]:


print(a.prod()) #prod 전체 원소들의 곱


# In[17]:


a = np.array([range(4)],float)
print(a.mean()) #a의 평균
print(a.var())  #a의 분산
print(a.std())  #a의 표준편차
print(a.max()) #a배열의 최대값


# In[19]:


a = np.array([4,9,2,3,6,8,7,4], int)
print(sorted(a))


# In[21]:


b = np.array([2,3,4,5,6,6,7,8],int)
print(a > b) #a와 b 배열의 각 원소마다 비교해서 t/f 출력


# In[23]:


c = np.array([True, False,True, True],bool)
print(any(c)) #하나라도 참이면 True를 반환하는 함수
print(all(c)) #모두 참이여야 참을 반환하는 함수 


# In[26]:


print(np.logical_not(c)) #c의 모든 원소 반대로 바꾸기


# In[27]:


d = np.array([True,True,False,False],bool)
print(np.logical_or(c,d)) #같은 열에서 하나라도 True이면 True

