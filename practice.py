i=1
while i<=100:
    if i<=100:
      print(i,end=",")
    i+=1   
print("printed 1 to 100 using while loop")  




a=100
while a>=1:
  if a>=1:
    print(a,end=",")
  a-=1  
print("reverse of 1 to 100 using while loop")


num = 9089
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))