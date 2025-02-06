# for i in range(0,21):
#     if i%2==0:
#         print(i)
#     if i==2:
#         break    

# for i in range (0,31):
#     print(i)
#     if i==9 or i==10:
#         break
#     print(i)
    

for class1 in range(1,11):
    for roll in range(1,20):
        if class1==3 and roll > 15:
            continue
        print(class1,roll)
    if class1==3:    
     break    