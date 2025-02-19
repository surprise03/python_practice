# 1 This to compare the gratest number betwwn 3 numbers 
num1=int(input("enter the number1:"))
num2=int(input("enter the number2:"))
num3=int(input("enter the number3:"))

if num1>=num2 and num1>=num3:
    greatest=num1
elif num2>=num1 and num2>=num3:
    greatest=num2
else:
    greatest=num3

print(f" the greatest number is {greatest}")





# 2 LEAP YEAR
year=int(input("enter the number:"))
if (year%4==0 and year % 100 != 0) or(year%400==0):
    print(f"the year {year} is a leap year ")
else:
    print(f"the year {year} is not a leap year ")  



# 3 VOWELS

char = input("Enter a single character: ").lower()  # Convert input to lowercase

if char in "aeiou":  
    print(f"{char} is a vowel.")
elif char.isalpha():  
    print(f"{char} is a consonant.")
else:  
    print(f"{char} is neither a vowel nor a consonant.")


# 4 MARKS

score=int(input("enter the score obtained"))


if score>100:
    print("invalid marks") 
elif score>=90 :
    print("Gread A")
elif score>=80:
    print("Gread B")
elif score>=70:
    print("GREAD C")
    
else:
    print("Fail") 



# 5 TRIANGLE


a = float(input("Enter length of first side: "))
b = float(input("Enter length of second side: "))
c = float(input("Enter length of third side: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    print("The given sides form a valid triangle.")
else:
    print("The given sides do not form a valid triangle.")

          

