from random import random , randint
def main():
    credentials = usercredentials()
    while True:

        cart = []
        categories = productcategories()
        productselection(category, cart)
        choice = input("Do you want to shop another category(yes/no)").lower().strip()

        if choice == "no":
            break

        print(cart)


def usercredentials():
    while True:
        try:

            username =  int(input("enter your mobile number : "))
            if(len(str(username))) == 10:

                break
            else :
                print("enter a 10digit phone number")
        except Exception as e:
            print("Enter a valid mobile number")
    otp = randint(1000,9999)     
    while True:
        try:

                
            
            otp = randint(1000,9999)                     
            print("your otp is : ", otp)
            password = int(input("enter otp : "))

            if  password != "" and password == otp:
                

                print("user logged in")
                break
            else :
                print("enter valid otp")
        except Exception as e:
            print("enter a vallid otp")
            
          

def productcategories():
    print("Categories you'd want to explore:")
    products = {
        "dairy" :{"milk" : 32 , "cheese" : 100, "butter" : 200},
        "snacks":{"chips" : 20 ,"coke" : 40, "kachori" : 40 },
        "electronics" : {"earphones" : 100, "headphones" : 500, "phone" : 10000}
    }              #a way to go back to a category and select products 
    while True :
        for category in products:
            print(category) 
                     #prints only keys   
            
        choice = input("enter the category :").lower().strip()
        if choice in products :
            return products[choice]
        else :
            print("wrong category select again")

            

def productselection(category, cart):
    products = []
    while True:
        for product in products:
            productselected = input("enter the products you would like to add in this category : \nenter 'done' when you are finished : ").lower().strip()
            if productselected == "done":
                break
            else:
                products.append(productselected)
                print(f"You have selected the following products : {product}")
                      



main()



