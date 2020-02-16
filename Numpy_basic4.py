#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
a = np.array([1,3,2],float)
print(np.where(a != 0, 1/a, a))#각원소마다  where조건을 통과시켜 출력
#ex 2의 경우 0이 아니고, 1/2 = 0.5 이고 그대로니까 결국 0.5
print(np.where(a >0, 3, 1))


# In[15]:


a = np.array([[0,2],[2,0]],float)
print(a.nonzero()) #행렬에서 0이 아닌 부분은 1로, 나머지는 0으로 출력


# In[18]:


a = np.array([1, np.NaN, np.Inf], float)
print(a) 
print(np.isnan(a)) #a의 각 원소가 not a number인지 확인하는 함수
print(np.isfinite(a)) #a의 각 원소가 유한한지 판별해준다


# In[19]:


a = np.array([1,2], int)
b = np.array([2,4], int)
print(np.dot(a,b)) #각각 같은 위치의 원소를 곱하고 1*2, 2*4 하고 그 합을 계산


# In[21]:


print(np.outer(a,b)) #외적
print(np.inner(a,b)) #내적


# In[23]:


a = np.array([[4,2,0],[6,3,4],[1,2,3]],float)
print(np.linalg.det(a)) #det은 determinant이다
#numpy패키지에서 linalg패키지를 이용하면 det를 구할 수 있다.


# In[24]:


b = np.linalg.inv(a)
print(np.dot(a,b))
#inv함수는 inverse 즉 역함수를 구해주는 메소드이다. linalg패키지 내장


# In[25]:


a = np.array([[1,2,3],[4,5,6],[5,3,2]],float)
U ,s ,Vh = np.linalg.svd(a) #svd 특이값 분해 Singular Value Decomposition
print(U)
print(s)
print(Vh)


# In[26]:


print(np.poly([-1,2,3,4,5])) #poly함수는 방정식의 계수를 구해주는 함수
#따라서 -1,2,3,4,5는 해가 된다.


# In[27]:


print(np.roots([1,4,2,-2]))
#roots는 해를 구하는 함수이고 안에 들어가는 값은 계수이다.


# In[28]:


print(np.polyder([1/4, 3,2,1/3,])) #다항식을 미분해 주는 함수


# In[41]:


print(np.polyval([1,0,0],4))
#polyval은 스칼라값에서 다항식의 해를 구한다.


# In[43]:


x = [1,2,3,4,5]
y = [0,1,2,3,4]
print(np.polyfit(x,y,2))
#polyfit는 입력과 출력값을 통해 다항식의 계수를 찾아준다.
#마지막 인자값은 차수의 다항식계수값이다.


# In[58]:


print(np.random.seed(0))
#seed는 특정한 시작 숫자를 정해주면 컴퓨터가 
#정해진 알고리즘에 의해 마치 난수처럼 보이는 수열을 생성한다.
#이 시작 숫자를 seed라고 한다.
print(np.random.rand(5))#0부터 1사이의 균일분포 함수로 5개를 출력
print(np.random.rand(2,3)) #0부터 1사이 2행3열의 행렬 생성
print(np.random.random())
print(np.random.randint(5,12)) #randint는 균일 분포의 정수 난수


# In[59]:


l = list(range(10))
print(l)
np.random.shuffle(l)
 #random패키지의 shuffle함수를 통해 range로 정렬되어 나오는 원소들을 마구잡이로
    #섞을 수 있다.
print(l)


# In[ ]:




