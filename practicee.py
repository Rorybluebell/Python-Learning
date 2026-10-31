#char = input("gender: ")
#if char == "male":
 #   print("Good morning sir")
#else:
 #   print("Good morning ma'am")
#a = int(input("Enter a number: "))
#if a % 2 == 0:
 #   print("The number is even")
#else:
 #   print("The number is odd")

#name = input("Enter your name: ")
#age = int(input("Enter your age: "))
#if age >= 18:
 #   print("You are eligible to vote.")
#else:
 #   print("You are not eligible to vote.")

#year = int(input("Enter a year: "))
#if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
 #   print(year, "is a leap year.")  
#else:
 #   print(year, "is not a leap year.")

#temp = int(input("Enter the temperature in Celcius:"))
#if temp < 0:
 #   print("It's freezing cold!")
#elif 0 <= temp < 10:
 #   print("It's very cold!")
#elif 10 <= temp < 20:
 #   print("It's cold!")
#elif 20 <= temp < 30:
 #   print("It's pleasant!")
#elif 30 <= temp < 40:
 #   print("It's hot!")
#elif temp >= 40:
 #   print("It's very hot!")
#else:
 #   print("Invalid temperature input.")


#a = int(input("Enter a number: "))
#statement = "hello world"
#for i in range(a):
 #   print(statement)

#print natural numbers upto n

#n = int(input("Enter a number: "))
#for i in range (1, n+1):
 #   print(i)

#reverse for loop . print n to 1
#n = int(input("Enter a number: "))
#for i in range(n, 0, -1):
 #   print(i)

#take a number as input and print it's table
#n = int(input("Enter a number: "))
#for i in range (n,(n*10)+1,n):
  #  print(i)

#sum upto n terms
#n = int(input("Enter a number: "))
#sum = n*(n+1)/2
#print("The sum of the first", n, "natural numbers is:", sum)
#using for loop
#n = int(input("Enter a number: "))
#sum = 0
#for i in range(1, n+1):
 #   sum += i
#print("The sum of the first", n, "natural nnn numbers is:", sum)

#factorial if a number
#n = int(input("Enter a number: "))
#for i in range(1, n+1):
   # factorial = 1
  #  for j in range(1, i+1):
 #       factorial *= j
  #  print("The factorial of", i, "is:", factorial)

  #sum of all even and odd numbers in a range seartely
#n = int(input("Enter a number: "))
#even_sum = 0
#odd_sum = 0
#for i in range(0, n+1,2):
 # even_sum += i
#for i in range(1, n+1,2):
 # odd_sum += i
#print("The sum of even numbers is:", even_sum)
#print("The sum of odd numbers is:", odd_sum)

#factors of a number
#n = int(input("Enter a number: "))
#for i in range(1, n+1):
#    if n % i == 0:
     #   print(i)

#a number whose summ of factors is equal to the number itself is called a perfect number. For example, 6 is a perfect number because its factors are 1, 2, 3, and 6, and their sum is 12, which is equal to 6.
#n = int(input("Enter a number: "))
#sum_factors = 0
#for i in range(1, n + 1):
 #   if n % i == 0:
  #      print(i)
   #     sum_factors += i

#print("The sum of factors is:", sum_factors//2)
#if sum_factors - n == n:
#    print("The number is perfect.")
#else:
#    print("The number is not perfect.")

#a = int (input("enter a number:"))
#while a > 0:
 #   print(a%10)
  #  a = a//10

#a = int(input("Enter a number: "))
#rev = 0
#while a>0:
 #   rev = rev*10 + a%10
  #  a=a//10
#print("The reverse of the number is:", rev)

#a = int(input("enetr a number:"))

#rev = 0
#copy = a

#while a > 0:
 #   rev = rev*10+ a%10

#    a = a//10

    #if rev == copy:
    #    print("The number is palindrome")
   # else:
  #       print("The number is not palindrome")


#l = [34,56,23,-43,98]

#print ("positive numbers are:")
#for i in l:
  #  if i>= 0:
 #       print(i)

#print ("negative numbers are:")

#for i in l:
    #if i<0:
      #  print(i)   

#l =[32,43,34,65,8,12,98]

#sum = 0

#for i in l:
 #   sum=sum+i

#print (sum/len(l))

#for i in l :

