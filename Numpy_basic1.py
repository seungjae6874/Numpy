#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
a = np.array([1,2,3],float)
print(a) #그냥 배열 a를 출력
print(a.tolist()) #a를 list로 변환하여 출력
print(list(a)) # a를 list로 변환하여 출력2


# In[16]:


import numpy as np
a = np.array([1,2,3],int)
b = np.array(['string','char'])
print(b)
c = b.tostring()#문자열을 갖는 배열 b를 tostring해서 출력해봄
print(c)
s = a.tostring()
print(s) #1,2,3을 원소로 갖는 배열을 tostring해서 뽑아보니 이상한 값나옴


# In[17]:


a = np.array([1,2,3],float)
print(a)
a.fill(0) #a 배열을 0으로 모든 원소를 채운다
print(a)


# In[22]:


a = np.array(range(6),float) #range(6)은 배열에 0~5까지의 수를 차례로 넣는다
print(a) 
b = a.reshape(2,3) #a배열이 1*6인데 이걸 2행 3열로 바꾼다는 뜻
print(b) #즉 reshape 메소드를 쓰려면 기존 배열의 행열곱과 동일한 값으로 변환해야함
c = np.array(range(4),int).reshape(2,2)
print(c) #배열을 생성과 동시에 reshape도 가능하다


# In[25]:


print(c.transpose()) # c행렬을 전치해서 바꿀 수 있다


# In[32]:


a = np.array([[1,2,3],[4,5,6]],float)#행렬 만들때는 각 행의 들어있는 원소갯수 동일!
print(a)


# In[33]:


print(a.flatten())#위에 있는 2행3열 행렬을 1행6열로 평평하게 피는 flatten메소드


# In[41]:


a = np.array([[range(3)],[range(3)]],float)
b = np.array([[range(3)],[range(3)]],float)
print(np.concatenate((a,b))) #두개의 배열을 한꺼번에 이어서 출력 가능

c = np.array([[1,2,3],[4,5,6]],float)
d = np.array([[7,8,9],[0,1,2]],float)
e = np.concatenate((c,d), axis = 1)
f = np.concatenate((c,d), axis = 0)
#axis 인자를 주어 축 기준을 바꿀 수 있다. axis가 1이면 
print(e) #1행을 먼저 출력
print(f)


# In[44]:


a = np.array([1,2,3],float)
b = np.array([4,5,6],float)
print(a[:,np.newaxis])
print(b[np.newaxis,:].shape)


# In[48]:


print(np.arange(5, dtype=float))
print(np.arange(1,6,2,dtype=int))#1부터 5까지 맨마지막 2는 2씩 커짐을 의미
print(np.arange(2,8,3,dtype=int))


# In[ ]:




