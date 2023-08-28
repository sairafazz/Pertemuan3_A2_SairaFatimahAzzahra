x=[1,3,2,4,]
z=['Alice', 'Bob']
z.sort()
x.sort()
print(x)
print(z)

print("Hello there!\nHow are you?\nI\'m doing fine.")

multi_line="""Hello there!
How are you?
I'm fine."""
print(multi_line)

spam='Hello World'
a=spam.strip()
b=spam.lstrip('Hell')
c=spam.rstrip('orld')
print(a)
print(b)
print(c)

print(','.join(['cats', 'rats', 'bats']))
print(' '.join(['My', 'name', 'is', 'Simon']))
print('My name is Simon'.split())
print('MyABCnameABCisABCSimon'.split('ABC'))
print('My name is Simon'.split('m'))
