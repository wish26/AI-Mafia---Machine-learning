#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


#creating array object
arr = np.array([[1, 2, 3],
                [4, 2, 5]])

#printing array
print( "Array is : \n", arr )

#printing type of arr object
print( "Array is of type : ", type(arr) )

#printing array dimensions (axis)
print( "No. of dimensions : ", arr.ndim ) 

#printing shape of array
print( "Shape of array : ", arr.shape )

#printing size (total no. of elements) of array
print( "Size of array : ", arr.size )

#printing type of elements in array
print( "Array stores elements of type : ", arr.dtype )


# In[3]:


#creating array from list with type float
a = np.array( [[1, 2, 4], [5, 8, 7]], dtype = 'float' )
print( "\nArray created using passed list : \n", a )

#creating array from tuple
b = np.array((1, 3, 2))
print( "\nArray created using passed tuple : \n", b )

#creating a 3*4 arra y with all zeroes
c = np.zeros((3,4))
print( "\n A3*4 array initialized with all zeroes : \n", c )

#create a constant value array of complex type
d = np.full( (3, 3), 6, dtype = 'float' )
print( "\n An array initialized with all 6's. Array type is complex : \n", d )

#Create an array with random values
e = np.random.random((2, 2))
print( "\nAn array with size 2*2 initialized with random values : \n", e )

#create a sequence of integers from 0 to 30 with steps of 5
# f = np.arrange(start = 0, stop = 30, step = 5)
# print( "\nA sequential array with steps of 5 : \n", f )

#create a sequence of 10 values in range 0 to 5
q = np.linspace(0, 2, 5)
print( "\nA sequential array with 10 values between 0 and 5 : \n", q )

#reshaping 3*4 array to 2*2*3 array
arr = np.array( [ [1, 2, 3, 4],
                  [5, 2, 4, 2],
                  [1, 2, 0, 1]] )
newArr = arr.reshape(2, 2, 3)
print( "\nOriginal array : \n", arr )
print( "\nReshaped array : \n", newArr )

#Flatten array
arr = np.array( [ [1, 2, 3], 
                  [4, 5, 6]] )
flArr = arr.flatten()
print( "\nOriginal array : \n", arr )
print( "\nFlatten array : \n", flArr )


# In[4]:


#An example array
arr = np.array( [ [-1, 2, 0, 4],
                  [4, -0.5, 6, 0],
                  [2.6, 0, 7, 8],
                  [3, -7, 4, 2.0]] )

#Slicing
temp1 = arr[:2, ::2]
print( "Array with first 2 rows and alternate columns( 0 and 2 ) : \n", temp1 )

#Integer array indexing example
temp2 = arr[[0, 1, 2, 3], [3, 2, 1, 0]]
print( "\nElements at indices (0, 3), (1, 2), (2, 1), and (3, 0) : \n", temp2 )

#Boolean array indexing example
cond = arr > 0
temp3 = arr[cond]
print( "\nElements greater that zero : \n", temp3 )


# In[5]:


#Operations on single array

a = np.array( [ [1, 2, 5, 3], [3, 5, 2, 1] ] )
print( "\nOriginial array is : \n", a )
print( "\n a+1 : \n", a+1 )
print( "\n a-3 : \n", a-3 )
print( "\n a*10 : \n", a*10 )
print( "\n a**2 : \n", a**2 )


# In[6]:


#Unary operators
arr = np.array( [ [1, 5, 6],
                  [4, 7, 2],
                  [3, 1, 9]] )

print( "Largest element is : ", arr.max() )
print( "Row-wise maximum element is : ", arr.max(axis = 1) )
print( "Column-wise minimum element is : ", arr.min(axis = 0) )
print( "Sum of all array elements is : ", arr.sum() )
print( "Cumulative sum along each row : \n", arr.cumsum(axis = 1) )


# In[7]:


#Binary Operators 
a = np.array( [ [1, 2],
                [3, 4]] )
b = np.array( [ [4, 3],
                [2, 1]] )
print( "Array sum : \n", a+b )
print( "Array multiplication (element-wise) : \n", a*b )
#Matrix Multiplication
print( "Matrix multiplication : \n", a.dot(b) )


# In[8]:


#create an array of sine values
a = np.array( [0, np.pi/2, np.pi] )
print( "\nOriginal array is : \n", a )
print( "Sine values of array elements : \n", np.sin(a) )

a = np.array( [0, 1, 2, 3] )

#exponential values
print( "Exponent of array elements : \n", np.exp(a) )

#square root of array values
print( "Square root of array elements : \n", np.sqrt(a))


# In[9]:


a = np.array( [ [1, 5, 4, 8],
                [3, 2, 9, 6] ] )

#Sorted array 
print( "\nArray elements in sorted order : \n", np.sort(a, axis = None) )

#Sort array row-wise
print( "\nSorting array row-wise : \n", np.sort( a, axis = 1 ) )

#Specifying sort algorithm
print( "\nSoring column-wise by using merge-sort : \n", np.sort( a, axis = 0, kind = 'mergeSort' ) )


# In[10]:


print(np.pi)


# In[11]:


print(np.pi/2)


# In[ ]:




