import pandas as pd
'''
d={"Name":['a','b','c'],"Age":[20,30,25],"Gender":["M","F","M"]}
df=pd.DataFrame(d)
print(df)

s=pd.Series([1,2,3,4,5])
print(s)
print(s[2])

d={"Name":["Alice","John","Joe"],"Age":[20,25,18]}
df=pd.DataFrame(d)
print(df)
print(df['Name'])

d=pd.DataFrame({'A':[1,2,3],'B':[4,5,6],'C':[7,8,9]})

print(d)
print(d['A'])

print(d.loc[0])

print(d.iloc[0:2])
print(d[d['C']>4])

d['D']=d['A'] + d['B']


d['E']=d['C']+d['D']


d.loc[0,'A']=2
print(d)


d=d.drop([2],axis=0)
print(d)

d=d.rename(columns={'A':"Alpha"})
print(d)

d=pd.DataFrame({'Name':['A','B','C'],'Age':[30,25,35]})

print(d)
print(d[d['Age']>30])
print(d[(d['Age'] > 20) & (d['Age'] < 30)])


print(d.sort_values(by='Age'))
print(d.sort_values(by='Age', ascending=False))

d=pd.DataFrame({'Team':['A','A','B','B'],'Score':[10,20,10,30]})
print(d.groupby('Team').sum())

df=pd.DataFrame({'A':[1,2,3]}, index=['x','y','z'])
df1=pd.DataFrame({'B':[4,5,6]}, index=['x','y','z'])
print(df.join(df1))


df1=pd.DataFrame({"A": [1,2,3,4]})
df2=pd.DataFrame({"A": [4,5,6,7]})
print(pd.concat([df1,df2]))
print(pd.concat([df1,df2],axis=1))

df=pd.DataFrame({'Date':['2025-01-01','2025-02-01','2025-03-01']})
df['Date']=pd.to_datetime(df['Date'])
print(df['Date'].dt.month)
print(df['Date'].dt.day)

print(df[df['Date']>'2025-02-01'])
'''
df=pd.read_csv('data.csv')
print(df)
df.to_csv('outpu.csv', index=False)