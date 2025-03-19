this_dict={
    "name":"kaushik",
    "age":23
}
print(this_dict)


#creating new dict constructor using dict()
new_dict=dict(name="john",age=58)
print(new_dict) 

#accessing the items
d={
    'year':1998,
    'model':'mustang'
}
print(d['model'])
d['brand']='ford'   #adding elemnt

print(d.items()) #to get all the elements

d['year']=2000
print(d.items())

for x in d.items():
    print(x)


  ############################  
d1={1,2,3,4,5}
d2={4,5,6,7,8,9}
d1.update(d2)
print(d1)
print('*************************************************************')


person={'name':'alicce','age':39}
if 'city' in person:
    print("present")
else:
    print("not present")
print('*************************************************************')



# sorting the dictionary
practice={'a':4,'d':2,'e':1,'b':3}
Sorted_dict=sorted(practice.items(), key=lambda x:x[1])
print(Sorted_dict)
print('*************************************************************')



#converting dictionary to list

k={'x':1,'y':2,'z':3}
key=list(k.keys())
values=list(k.values())
items=list(k.items())

print(key)
print(values)
print(items)