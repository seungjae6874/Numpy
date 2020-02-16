#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
print(np.ones((2,3),dtype = float)) #np의 메소드로 ones는 2,3행렬을 1로 채워 생성
print(np.zeros((2),dtype = float)) #zeros는 1행 2열 행렬을 0으로 채워 생성


# In[5]:


a = np.array([[1,2,3],[4,5,6]],float) #1,2,3 4,5,6을 원소로 갖는 행렬 생성
print(np.zeros_like(a)) #a 행렬의 기존 원소 값들을 모두 0으로 바꾼다
print(np.ones_like(a)) #a 행렬 원소들을 모두1로 바꿈


# In[6]:


print(np.identity(4, dtype = float))#단위행렬 사이즈=4


# In[12]:


print(np.eye(4,k =0, dtype = float)) 
# k는 첫행의 k번째 원소부터 차례로 다음 행에는 1씩 자리수 늘려 1을 삽입


# In[14]:


a = np.array([1,2,3],float)
b = np.array([2,4,5],float)
print(a+b)
print(a**b)


# In[15]:


a = np.array([1,2,3],float)
b = np.array([4,5],float)
print(a+b) #열이 맞지 않기에 연산 불가


# In[20]:


a = np.array([1.5,2.3,3],float)
print(np.sqrt(a)) #sqrt는 루트값
print(np.ceil(a)) #ceil는 천장으로 올림을 의미
print(np.rint(a)) #rint는 바닥으로써 내림을 의미
print(np.pi) #pi도 numpy로 호출 가능


# In[ ]:




