i=0
while i<51:
    
    if i%2==0:
        print(i)
    i+=1    

# Get input from the user
num = int(input("Enter a number: "))

# Loop through tables from 1 to the given number
for n in range(1, num + 1):
    print(f"\nMultiplication Table of {n}:")
    for i in range(1, 21):
        print(f"{n} x {i} = {n * i}")

   
      