import matplotlib.pyplot as plt
import numpy as np
'''
print(matplotlib.__version__)

x=np.array([1,6])
y=np.array([3,25])

plt.plot(x,y)
plt.show()

y=np.array([3,8,1,10,14,1])
plt.plot(y, marker='o')
plt.show()


x=np.array([12,4,1,23,13,6,45,4,57,23,53,1,23,53,57,68])
y=np.array([3,8,1,10,14,1,23,24,45,45,67,67,68,54,43,65])
plt.title("GRAPH")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.scatter(x,y,color='red')
plt.show()


x=np.array(['A','B','C','D'])
y=np.array([3,8,1,10])
plt.title("GRAPH")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.bar(x,y,color='red')
plt.show()
'''
x=np.random.normal([12,43,24,47])
labels=['Apples','Banana','Cherry','Dates']
colours=['black','skyblue','pink',"#F3494 9"]
plt.pie(x,labels=labels,colors=colours)
plt.show()
