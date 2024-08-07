n=int(input("enter a number "))
a=0
b=1
sum=0
for m in range (n):
    print(sum,end=" ")
    sum=a+b
    b=a
    a=sum

2. Factorial Calculation
Write a function to compute the factorial of a given number using a loop. For example, factorial(5) should return 120.

n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial=factorial* i
print(factorial)

3. Sum of Digits
Write a function that takes an integer and returns the sum of its digits. For example, for the number 1234, the output should be 10 (1 + 2 + 3 + 4).

i=int(input("Enter a number: "))
result=0
while i>0:
    dig=i%10
    result=result+dig
    i=i//10
    print(result)


4. Prime Number Check
Write a function to check if a given number is prime using a loop. For example, is_prime(29) should return True, and is_prime(10) should return False.

n = int(input("Enter a number: "))
if n == 2:
    print("It's a prime number")
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print("It's a prime number")
    else:
        print("Not a prime number")



5. Reverse a String
Write a function to reverse a given string using a loop. For example, for the input "hello", the output should be “olleh”.

s = input("Enter a string: ")

for i in range(len(s) - 1, -1, -1):
    print(s[i], end="\t")


6. Palindrome Check
Write a function to check if a given string is a palindrome using a loop. For example, "madam" is a palindrome.
a = input("Enter a string: ")
b = a[::-1]
if a == b:
    print("palindrome")
else:
    print("not palindrome")

7. Print Multiplication Table
Write a function that prints the multiplication table for a given number n up to 10.
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
8. Find the Largest Number in a List
Write a function that finds the largest number in a list using a loop. For example, given [4, 7, 1, 8, 3], the output should be 8.

a = []
num = int(input("Enter number of elements in the list: "))
for i in range(num):
    b = int(input("Enter element: "))
    a.append(b)
print("Largest element is:", max(a))
10. Print a Pattern
Write a function that prints a pattern of stars based on the number of rows provided. For example, if rows = 5, the output should be:
*
**
***
****
*****
rows = int(input("Enter the number of rows: "))
for row in range(1, rows + 1):
    for col in range(row):
        print('*', end='')
    print()

Or

rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    print('*' * i)

* Print a Pattern
Write a function that prints a pattern of stars based on the number of rows provided. For example, if rows = 5, the output should be:
****
 ***
  **
   *

n=int(input("Enter a number:"))
for row in range(1,n+1):
    for space in range(1,row):
        print(" ",end="")
    for stars in range(1,n-row+1):
        print("*",end="")
    print()

11. Even and Odd Numbers
Write a function that takes a list of integers and returns two lists: one containing all the even numbers and the other containing all the odd numbers.
i = input("Enter numbers separated by spaces: ")
n = [int(num) for num in i.split()]
even_numbers = []
odd_numbers = []
for num in n:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

12. Count Vowels and Consonants
Write a function that takes a string and returns the count of vowels and consonants. For example, for the input "hello world", the output should be {'vowels': 3, 'consonants': 7}.

vowel= 0
consonant = 0
var = input("Enter a string: ")
vowels = 'aeiouAEIOU'
for i in var:
    if i in vowels:
        vowel =vowel+ 1
    else:
        consonant += 1
print('Count of vowels:', vowel)
print('Count of consonants:', consonant)

13. Number Pattern
Write a function that prints a number pattern based on a given integer n. For example, for n = 4, the output should be:
1
22
333
4444
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    print(str(i) * i)

14. Multiples of a Number
Write a function that prints all multiples of a given number up to a specified limit. For example, for num = 3 and limit = 20, the output should be 3, 6, 9, 12, 15, 18.
a= int(input("Enter the number: "))
b= int(input("Enter the limit: "))
for i in range(a, b + 1, a):
    print(i, end=', ')
print() 


15. Sum of Even and Odd Numbers in a List
Write a function that takes a list of integers and returns a tuple with the sum of even numbers and the sum of odd numbers. For example, for the list [1, 2, 3, 4, 5, 6], the output should be (12, 9).
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
odd_sum = 0
even_sum = 0
print("Odd numbers:")
for num in range(start, end + 1):
    if num % 2 != 0:
        print(num)
        odd_sum += num
print("\nEven numbers:")
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num)
        even_sum += num
print("\nSum of odd numbers:", odd_sum)
print("Sum of even numbers:", even_sum)
print("Total sum of all numbers:", odd_sum + even_sum)