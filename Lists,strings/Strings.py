s='Hello, World'
#prints 2th charecter and ignores 5th charecter
print(s[2:5])


#negative indexing

t='Hello, World'
#counts -1th character
print(t[:-2])

m='Hello, World'
print(m[-8:-4])


#modifying stirngs

a="Hello World"
print(a.upper())
print(a.lower())

#removing whitespaces

a=" Hello  World "
print(a.strip())
print(a.replace("H","W"))
print(a.split())

#concatenation

a="Hello "
b="World"
c=a+b
print(c)



# f String
age=18
txt=f"hi user ur age is {age}"
print(txt)


# length
s='Hello hi'
print(len(s))

#steps

x='kaushik'
print(x[3::])
print(x[:4:])
print(x[::2])
print(x[::-1])
print(x[1:5:2])
print('**********************')

#reversing strings

x="kaushik"
rev=''
for res in x:
    rev=res+rev
print(rev)