# def exampleOne(a,*b):
#     res=a
#     for i in b:
#         res += i
#     return res  


# # exampleOne(1,8)

# def ExampleTwo(**a):
#     res=a
#     for


# def example(x):
#     return x*x

# res=map(example,[1,2,3,4,5])
# print(list(res))


def key(**kargs):
    res=0
    for i,j in kargs.items():
        print(i,":",j)

key(username=input("UserName:"),password=input("enter the password:") , gender=input("male/female:") ,remakrs=input("any remarks:"),country=input("your country?!:")     )
