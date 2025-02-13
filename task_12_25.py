def key(**kargs):
    res=0
    for i,j in kargs.items():
        print(i,":",j)

key(username=input("UserName:"),password=input("enter the password:") , gender=input("male/female:") ,remakrs=input("any remarks:"),country=input("your country?!:")     )
