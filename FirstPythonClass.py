print('variables')
_a,_1,s2=5,6,7;

print(_1,_a,s2);

print('list')
list=['a',1,'xyz']
print(list)
list[0]='b'
print(list)
print('tuples')
_a=('rama','sita',2)
b1=(9,'latha',10)
a1=_a[0]+'sri'
_a=('ramaa','siya',2)
print('rama : '+_a[0]+','+'a1...'+a1)
print(_a)
z=_a[2]
print(_a+b1)
print(b1[1])
print(z)

print('dictionary')
dictionar={1:3,2:'sweety',3:4}
print(dictionar.keys())
print(dictionar.values())
print('print dic..'+dictionar[2]);
f1={'a':2,'a':8}
print(f1)

""""a=int(input("Enter a :"))
b=a+200;
c=a+b;
print("c ",b)"""

#name=str(input("Enter your name : "))
#   print("Hello..",name)

x=7;
y=8;
z=9;

if x>y and x>z :
    print(x,' is greater');

if y>z and y>x :
    print(y," is greater");

if z>x and z>y :
    print(z," is greater");


i=1
n=int(input("Enter no : "))

for i in range(1,n):
    print("%d X %d = %d"%(n,i,n*i));