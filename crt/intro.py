#whether odd or even; - asking and answer 5 times

'''count = 0
while(count < 6):

    a = int(input("enter a number:"))

    if (a % 2 == 0):


        print("even")


    else: 
        print("odd")

    count +=1'''
#same using for
'''for i in range(5):
    a = int(input("enter a number"))
    if (a%2 == 0):
        print("even")
    else :
        print("odd")'''
#reverse list 
'''A = [1,2,3,4,5,6,7,8,9,10]
        for a in A[::-1]:
 
            print(a)'''
#enumarate methods
'''
for index,i in enumerate(range(9,-1,-1)):

    print(index, i)
'''
'''
A = ["rushil" , "jbiet" , "csds"]
for index,a in  enumerate(A, start=1):
    print(index,a)'''

#zip

'''a = ["rushil", "csds", "jbiet"]
b = ["rahul" , "cse", "jbiet"]

for A,B in zip(a,b):
    print(A,B)'''




'''a = ["rushil", "jasmin", "blah"]
b = [39,49,59]

for A,B in zip(a,b):
    print(A,B)'''


#BLINKIT
while(True):
    username = input("USERNAME : ")
    password = input("PASSWORD : ")


    if (username and password is None):
        print("user logged in")
        break;
    else:
        print("enter again")

print("========================\n")
print("items :")

items = ["apple" , "bananas", "mangoes"]
cart = []
print(items)

while(True):
    select = input("select the items in the list(type done when finished)")
    if select == "done":
        break

    elif select in items:
        cart.append(select)
        print("your cart consists of", select)

    

    else :
        print("item not available")






