# n=input("enter the string")
# rev=''

# for i in n:
#     rev=i+rev
# print(rev)



# to check whether given string containg vowels
s="kaushik"
count=0
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count+=1
if count==0:
    print("no vowels found")
else:
    print("vowels found at",count)


#to check if the string is palindrome

s='racecar'
palindrome= s==s[::-1]
print(palindrome)

# stirng formatting

name="alice"
age=38

txt=f'my name is {name} and iam {age} years old'
print(txt)

#replace substring

txt='i love python'
old_text='python'
new_text='programming'

k=txt.replace(old_text,new_text)
print(k)


#sum of list
def sum_list(lst):
    return sum(lst)
n=[1,2,3,4]
print("the sum of list is",+sum_list(n))


# reverse a list
a=[1,2,3,4,5]
rev=a[::-1]
print(rev)

a=[1,2,3,4]
sums=sum(a)
mins=min(a)
print(sums)
print(mins)
print(max(a))


# removing dupicates from the list

def dupli(n):
    return list(dict.fromkeys(n))
n=[1,2,3,4,4,2,1,6,7,8]
print(dupli(n))

#sorting the lsit

list=[6,1,2,9,4,5,8,0,3]
res=list.sort()
print(list)

lst=[1,2,3,4,5]
target=6
if target in lst:
    print("present")
else:
    print("not present")

#inserting elements at specific position

l=[1,2,3,4,5]
l.insert(2,10)
print(l)

#merging two lists

def merge(l1,l2):
    return l1+l2
l1=[1,2,3]
l2=[4,5,6]

print(merge(l1,l2))

#counting the occurence of the list

def occurance(ele,target):
    count=0
    for res in ele:
        if target== res:
            
            count+=1
            print("count",count)
    return count
            
            

ele=[1,2,3,3,3,5,6,3]
target=3
print("function call",occurance(ele,target))

# def add(n1,n2):
#     print(f"the first no is{n1}")
#     print(f"the second no is{n2}")
#     sum=n1+n2
#     print(f"the result of {n1} + {n2} is {sum}")
#     return sum
#     # return n1+n2


# n1=2
# n2=2

# print(add(n1,n2))


# def function(num):
    
#     if num%2==0:
#         print("masala dosa")
#     else:
#         print("tupa dosa")

# num=4
# print(function(num))

def function(num):
    for i in range(num):
        if i%2==0:
            print("even",i)
        else:
            print("odd",i)
function(4)