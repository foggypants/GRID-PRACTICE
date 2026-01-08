import numpy as np  
'''
arr=np.array(['a','2','3'], dtype='a')
print(arr)
print(arr.dtype)

arr=np.array(["apple","banana","cherry"])
print(arr.dtype)

arr=np.array([0.10,0.20,0.13])
print(arr)
print(arr.dtype)
newarr=arr.astype(bool)
print(newarr)
print(newarr.dtype)
arr=np.array([1,0,3])
newarr=arr.astype('f')
print(newarr)
print(newarr.dtype)

arr=np.array([1,2,3,4,5])
x=arr.copy()
arr[0]=42
print(arr)
print(x)
x=arr.view()
arr[1]=99
print(arr)
print(x)

arr=np.array([1,2,3,4,5])
x=arr.view()
x[0]=31
print(arr)
print(x)
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr.reshape(6,2))

def f(x,y=5,*args):
    return x+y+sum(args)
print(f(2,3,4,5))

a=np.arange(0,9).reshape(3,3)
print(a[1,:])
x=None
if x:
    print("yes")
else:
    print("no")
'''
arr=np.array([10,20,30,40,50,60])

print("Mean:",np.mean(arr))
print("Median:",np.median(arr))
print("Standard deviation:",np.std(arr))
print("Variance:",np.var(arr))
print("Sum:",np.sum(arr))
print("Min:",np.min(arr))
print("Max:",np.max(arr))