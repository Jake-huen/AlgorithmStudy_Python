k = int(input())

a=[0]*46
b=[0]*46

a[0]=1

for i in range(1,k+1):
    a[i]=b[i-1]
    b[i]=a[i-1]+b[i-1]

print(a[k],b[k])
