# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.
# To find odd or even numbers 
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

num1 = int(input("Enter a number: "))
if (num1 % 2) == 0:
      print(num1," is Even")
else:
      print(num1," is Odd")
