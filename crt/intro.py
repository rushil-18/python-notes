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


# BLINKIT
while(True):
    username = input("USERNAME : ")
    password = input("PASSWORD : ")
    if username != "" and password != "":
        print("user logged in")
        break
    else:
        print("try again...")


print("========================")
print("ITEMS :")

items = ["apple", "bananas", "mangoes"]
prices = {
    "apple": 30,
    "bananas": 40,
    "mangoes": 60
}
cart = []
print(items)

while(True):

    select = input("\nselect the item in the list (type done when finished): ")

    if select == "done":
        break

    elif select in items:
        cart.append(select)
        print(select, "added to cart")
        print("your cart consists of", cart)

    else:
        print("item not available")


print("\n========================")
print("YOUR CART")
print("========================")

total = 0

for item in cart:
    print(item, "-", prices[item])
    total = total + prices[item]

print("------------------------")
print("Total amount =", total)


if len(cart) == 0:
    print("your cart is empty")

else:
    order = input("Do you want to place the order? (yes/no): ")

    if order == "yes":
        print("\n========================")
        print("ORDER SUCCESSFUL")
        print("========================")
        print("Items:", cart)
        print("Total amount:", total)
        print("Order placed successfully")
        print("Delivery in approximately 10 minutes")

    else:
        print("order cancelled")






