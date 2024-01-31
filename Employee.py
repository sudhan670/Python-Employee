def employee(name):
    print(name) 

employee("sudhan") 
count=0
while count<=5:
    count+=1
    print(count) 

total=0
while True:
    user_input=input("enter the input")
    if user_input=="exit":
        break
    total+=int(user_input)
    print(total) 

l=["apple","orange","banana"]
for i in l:
    print("The New Fruit is",{i}) 
    for numbers in range(1,3):
        print(numbers)
        for index,number in enumerate(l):
            print(index,number)
numbers=[1,2,3]
a,b,c=numbers
print(a)
print(b)
print(c)
n="New"
e="employee"
print(n.lower()+e.upper()) 
p=" Python Programming Version Is New "
print(p.strip()) 
contains="Python" in p 
print(contains)
print(p[4:10])
print(p[:11])
print(p[4:]) 
l=[]
for i in p.split():
    l.append(i) 
o=l[::-1]
for i in o:
    print(i,end=" ")  
#Tuples for the Python  
tup=("orange",'apple','banana')
print(len(tup))
print(tup)
o=list(tup)
o.append("kwik")
print(o)
o.remove("apple")
o.pop(1)
print(o)
p=["L","p","i"]
o.extend(p)
print(o)
o[:2]=["f",'g','t','y','e']
print(o)
del o[0]
print(o)
index=0
while index<len(o):
    print(o[index],':',index)
    index+=1 
i=('8','9','world')
print(i)
tuy='o','l','jbvoue'
print(tuy) 
#Accessing Tuples in python  
print(tup[-1])
print(tup[0]) 
print(tup[1:3])
result='apple' in tup
print(result)
op=(1,2,3,4,5)
print(op.index(3)) 
print(tup+(5,6,7,7,8,13)) 
# nested tuple
my_tuple=((34,5),(5,6),(9,0))
print(my_tuple)
for i in my_tuple:
    for num in i:
        print(num) 
set1={4,3,4,56}
set2={4,5,62,3}
print(set1|set2)
print(set1&set2)
print(set1-set2)
print(set1.union(set2))
print(set.intersection(set2))
print(set1.difference(set2)) 
print(4 in set1)
first_item=next(iter(set1))
my_dict={'name':'john','age':'25','desination':'engineer'}
for i in range(0,5):
    dict_my=my_dict.get("occupation",i)
    print(i)
keys=my_dict.keys()
values=my_dict.values()
items=my_dict.items()
print(keys)
print(values)
print(items)
my_dict.update({'age':'34','occupation':'Doctor'})
print(my_dict)
my_dict['age']=234
print(my_dict)
remove_de=my_dict.pop('age')
my_dict['age']=remove_de+1
print(my_dict)
my_dict['country']='india'
my_dict.update({'country':'france','professional':'software developer'})
my_dict.setdefault('hobby','reading')
print(my_dict) 
g={"car":"porsche","bike":"BMW",
   "Country":"Germany","New Jersey":"USA",
   "Lithuvia":"Punjab"}
print(g.keys())
print(g.items())
print(g.values())



