import random

print(random.randint(1, 100))


print(random.random())

items=['red', 'blue', 'green', 'yellow']
print(random.choice(items))


random.shuffle(items)
print(items)



print(random.sample(items,4))