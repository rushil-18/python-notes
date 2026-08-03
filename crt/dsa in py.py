word = input("Enter the string: ")
count = {}
for char in word:
    if char in count:
        count[char] = count[char] + 1
    else:
        count[char] = 1
repeating = []
for char in count:
    if count[char] > 1:
        repeating.append(char)

third = repeating[2]

print("3rd repeating character:", third)
print("Number of repetitions:", count[third])



def factorial(n):
    if n == 0 or n == 1:
        return 1 
    return n * factorial(n-1)
print(factorial(n=5))



def fibonacci(n):
    n = int(input("enter a number"))
    a, b = 0, 1
    if n <= 0 :
        print("print positive number pls")
    elif n == 1:
        print(a)
    else :
        print("fibonacci series :")
        print(a, end=" ")

        print(b, end = " ")
        for i in range(2, n):
            c = a + b
            print(c , end = " ")
            a = b 
            b = c


