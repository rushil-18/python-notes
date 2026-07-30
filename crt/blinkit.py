from random import random , randint
def main():
    credentials = usercredentials()
    categories = productcategories()
    products = productselection()

def usercredentials():
    while True:
        
        username =  input("enter your mobile number : ")
        if len((username)) == 10 and username != "" :
            break
        else :
            print("enter a 10digit phone number")

         
            
                
            
        otp = randint(1000,9999)                     
        print("your otp is : ", otp)
        password = int(input("enter otp : "))

        if  password != "":
            if password == otp:

                print("user logged in")
                break;
            else :
                print("enter valid otp")
            
          

def productcategories():
    print("Categories you'd want to explore:")
    categories = ["dairy" , "snacks" , "electronics"]
    for category in categories : 
        print(category)
    userselection = input("enter a category you'd like to explore : ").lower().strip()

    if userselection == "dairy":
        dairy = {"milk" : 32, "cheese":100, "butter" : 150 }
        for dairyproducts in dairy:
            print("products in this catrgory :" ,dairyproducts,dairy[dairyproducts])           #a way to print prices as well


    elif userselection == "snacks":
        snacks = {"chips":20, "coke":45, "chakodi": 50}
        for snack in snacks:
            print("products in this catrgory :", snack, snacks[snack])  #only snack gives keys. snacks[snack] gives key value pair

    elif userselection == "electronics":
        electronics = {"earphones":250, "headphones" : 500, "phone" : 1000 }
        for electronic in electronics:

            print("products in this catrgory :", electronic, electronics[electronic])                #a way to go back to a category and select products 


def productselection():
    products = []
    while True:
        for product in products:
            productselected = input("enter the products you would like to add in this category : \nenter 'done' when you are finished : ").lower().strip()
            if productselected == "done":
                break
            else:
                products.append(productselected)
                print(f"You have selected the following products : {product}")
                      

        print(f"Your cart consists of :" {products, }) 

main()
