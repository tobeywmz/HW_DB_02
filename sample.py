print("enter users count:")
n = input()
m = int(n)

user=[]
user.append([])

a=0
while a<m:

    print("enter name:")
    user[a].append(input())

    print("enter age:")
    user[a].append(input())
    
    a= a+1
    user.append([])

    
print("whose age are you looking for?")
name = input();


b=0
while b<m:
    if(name==user[b][0]):
        print(user[b][1])

    b= b+1
