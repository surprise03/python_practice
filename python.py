a=[5,3,7,5,3,90,56,4,5]

a=(set(a))
print(a)

a=(list(a))
print(a)


for i in range(0,len(a)):
    for j in range(i+1 ,len(a)):
        if a[i] >=a[j]:
            a[i],a[j]=a[j],a[i]  
print("sorted",a)           
r