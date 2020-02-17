#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[20]:


a = np.array([1,2,3],int)
print(a)


# In[3]:


b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]],float)
print(b)


# In[4]:


#Get Dimension
a.ndim


# In[5]:


b.ndim


# In[6]:


#Get Shape
a.shape


# In[7]:


b.shape


# In[22]:


#Get Type
a.dtype


# In[27]:


#Get Size
a.itemsize
b.itemsize


# In[26]:


#Get total size
a.size * a.itemsize
a.nbytes


# In[30]:


a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)


# In[37]:


#Get specific element[r,c]
a[1,5]
# -를 붙여서 끝에서부터의 수로도 나타낼수 있다.
#배열이 너무 커서 끝에 더 가깝다면 -1이 맨 마지막 인덱스라는 것을 기억
a[1,-1] #14


# In[39]:


#Get specific row
a[0,:] 
#한 행을 모두 뽑고 싶으면 해당 행, ':'를 열로 하면 그 행이 다나옴

a[:,2] #3열의 모든 행 값이  다나옴


# In[42]:


#Getting a little more fancy
a[0, 1: ] #1행의 2열부터 끝까지
a[0, 1:-1:2] #1행의 2열부터 끝까지 2칸씩 이동해서 뽑음


# In[47]:


a[1,5] = 20
print(a)

a[1,:] = -1
print(a)
a[:, 2] = 3
print(a)


# In[49]:


b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)


# In[51]:


#Get specific element (work outside in)
b[0,1,-1]


# In[53]:


#replace
b[:,1,:]  = [[6,8],[7,4]]
#첫번째 값은 몇번째 배열을 선택할건지,
        #두번째값은 그 배열의 어떤 행을 선택할건지,
        #세번째는 그 행의 어떤 열을 선택할껀지


# In[54]:


b


# In[57]:


# All 0s matrix
np.zeros((2,2,3))


# In[60]:


#All 1s matrix
np.ones((3,2,2),int)


# In[62]:


#Any other number
np.full((2,2),33)


# In[66]:


#Any other number(full_like)
np.full_like(a,4)


# In[71]:


#Random decimal numbers
np.random.rand(4,2) #0~1사이 의 값을 4행2열 행렬로 만듦


# In[79]:


#Random Integer values
np.random.randint(7,size=(3,3)) #0~7사이 랜덤값 3*3행렬


# In[84]:


np.random.randint(5,10,size= (2,2)) #5~10사이 랜덤


# In[85]:


#indentity matrix
np.identity(3) #단위행렬


# In[87]:


#repeat array
arr = np.array([1,2,3])
r = np.repeat(arr,3,axis =0)
print(r)


# In[104]:


ex = np.zeros((5,5),int)
ex[0,:] = 1
ex[-1:] = 1
ex[:,0] = 1
ex[:,-1] = 1
ex[2,2] = 9
print(ex)
#또는
output = np.ones((5,5),int)
output[1:-1,1:-1] = 0
output[2,2] = 9
print(output)
#또는
ex2 = np.ones((5,5),int)
zero = np.zeros((3,3),int)
zero[1,1]= 9
ex2[1:-1,1:-1] = zero
print(ex2)


# In[111]:


########Be carefull when copying array!!!!!!!!!!!!!!!!!
a = np.array([1,2,3])
b = a
b[0] = 100
#이러면 a도 100으로 원소가 바뀌었다.....
#이를 방지하기 위해
c = a.copy()
c[0] = 1000
print('a: ',a, 'c',c)


# In[112]:


#Mathmatics
a = np.array([1,2,3])
a+2


# In[113]:


a/2


# In[114]:


a**3


# In[117]:


b = np.array([1,0,1])
a+b
c = b.copy()
c[0] = 0
a+c


# In[118]:


np.cos(a) #cosine 함수


# In[126]:


#Linear Algebra
a = np.ones((2,3))
print(a)
b= np.full((3,2),2)
print(b)

c =np.matmul(a,b)
print(c)


# In[128]:


d = np.identity(3)
np.linalg.det(d) #linearalgebra즉 linalg패키지의 det메소드


# In[129]:


##########Statistics about numpy


# In[130]:


stats = np.array([[1,2,3],[4,5,6]])
stats


# In[131]:


np.min(stats)


# In[135]:


np.max(stats, axis =0) #가장 큰 값을 갖는 행전체를 출력


# In[136]:


#Reorganizing Arrays


# In[140]:


before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)
after = before.reshape((8,1)) #2,4행렬을 8*1행렬로 바꾸었다
print(after)


# In[143]:


#Vertically stacking vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
np.vstack([v1,v2])


# In[144]:


# Load Data from file


# In[ ]:




