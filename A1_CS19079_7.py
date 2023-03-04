from A1_CS19079_2 import UserRecords
from A1_CS19079_3 import History
from A1_CS19079_4 import Products
from A1_CS19079_5 import Cart
from datetime import datetime
from A1_CS19079_6 import Admin

class UserInterface:
    email = ''
    currentCart = []

    def __init__(self):
        UserInterface.signInPage()

    def signInPage():  # Main interface function
        print()
        print('=====***** WELCOME TO ZEE VIRTUAL MOBILE MARKET *****=====')
        print()
        print('1_ Sign in as User')
        print('2_ Sign in as Admin')
        print()
        choice = input('Enter option number: ')
        print()
        if choice == '1':
            UserInterface.userSignIn()
            while True:
                UserInterface.mainMenu()
                choice1 = input('Enter option number: ')
                if choice1 == '1':
                    UserInterface.shoppingHistory()
                elif choice1 == '2':
                    UserInterface.subMenu()
                elif choice1 == '3':  # Will save the cart items as a shopping history
                    if len(UserInterface.currentCart) == 0:
                        break
                    else:
                        saveHistory = History()
                        now = datetime.now()
                        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                        history = [dt_string, UserInterface.currentCart]
                        saveHistory.saveRecords(UserInterface.email, history)
                    break
        elif choice == '2':
            UserInterface.adminSignIn()
        else:
            print('Please select from given options')
            UserInterface.signInPage()

    def userSignIn():  # This function provides user sign in and sign up features using class UserRecords
        email = input("Enter your email: ")
        UserInterface.email = email
        uRecords = UserRecords()
        x = uRecords.checkEmail(email)
        if x:
            while True:
                print()
                password = input('Enter your password: ')
                y = uRecords.checkPass(email, password)
                if y:
                    break
        elif not x:
            while True:
                print()
                print('Your email is not signed up!!!')
                print('1_ Re-enter the email')
                print('2_ Sign up')
                print()
                choice = input('Enter option number: ')
                print()
                if choice == '1':
                    UserInterface.userSignIn()
                    break
                elif choice == '2':
                    uRecords.saveRecords()
                    break
                else:
                    print('Please select given option')

    def adminSignIn():  # This function provides admin sign in and sign up features using class Admin
        admin = Admin()
        email = input('Enter admin email: ')
        while True:
            if email != admin.adminE:
                print()
                email = input('Incorrect email \nEnter email again: ')
            else:
                password = input('Enter password: ')
                while True:
                    if password != admin.password:
                        password = input('\nIncorrect password \nEnter password again: ')
                    else:
                        while True:
                            print()
                            print('1_ Add product')
                            print('2_ Remove product')
                            print("3_ Sign out")
                            print()
                            choice = input("Enter option number: ")
                            print()
                            if choice == '1':
                                admin.addProduct()
                            elif choice == '2':
                                admin.deleteProduct()
                            elif choice == '3':
                                break
                            else:
                                print('Please select from given options')
                        break
                break


    def mainMenu():  # main menu just after the user sign in
        print()
        print('=====***** MAIN MENU *****=====')
        print('1_ Shopping History')
        print('2_ Products')
        print('3_ Check out')
        print('=====*********************=====')
        print()

    def shoppingHistory():  # provide user's shopping history as well as to delete history
        uHistory = History()
        while True:
            print()
            print('=====****** HISTORY ******=====')
            print('1_ View History')
            print('2_ Delete History')
            print('3_ Back')
            print('=====*********************=====')
            print()
            choice = input('Enter option number: ')
            print()
            if choice == '1':  # View History
                histories = uHistory.getHistory(UserInterface.email)
                if not histories:
                    print('You have not buy anything!')
                    pass
                else:
                    for history in histories:
                        print('Time and Date: ' + history[0])
                        for i in range(len(history[1])):
                            if i == len(history[1])-1:
                                print(history[1][i])
                            else:
                                print(history[1][i], end=',')

                        print()
            elif choice == '2':  # Delete history
                if len(uHistory.history) == 0:
                    print('Your history is empty!')
                else:
                    uHistory.deleteHistory(UserInterface.email)  # Printing history as well
                    print("History deleted successfully!!!")
            elif choice == '3':  # Back
                break
            else:
                print('Please select from given options!')

    def subMenu():
        product = Products()
        cart = Cart()
        while True:
            print()
            print('=====****** PRODUCTS ******=====')
            print('1_ Available Products')
            print('2_ Current Cart')
            print('3_ Back')
            print('=====**********************=====')
            print()
            choice1 = input('Enter option number: ')
            if choice1 == '1':  # Available products
                while True:
                    print()
                    print('===*** AVAILABLE PRODUCTS ***===')
                    count1 = 0
                    for i in product.productList:
                        count1 += 1
                        print(str(count1) + '_ ' + i)
                    print('===**************************===')
                    print()
                    print('1_ Product details')
                    print('2_ Add to cart')
                    print('3_ Back')
                    print()
                    choice1a = input("Enter option number: ")
                    if choice1a == '1':  # Product Details
                        choice1b = int(input("Enter Product number to see its details: "))
                        print()
                        print('===**** PRODUCT ' + str(choice1b) + ' Details****===')
                        details = product.getProductDetails(product.productList[choice1b-1])
                        details = details[1:]
                        for i in details:
                            print(i[0] + ': ' + str(i[1]))
                        print('=====**********************=====')
                        print()
                    elif choice1a == '2':  # Add to cart
                        choice1c = int(input("Enter product number to add to cart: "))
                        cart.addToCart(product.productList[choice1c-1])
                        print('Product added!')
                        currentCart = cart.currentCart()
                        UserInterface.currentCart = currentCart
                    elif choice1a == '3':  # Back
                        break
                    else:
                        print('Please select from given options!')
            elif choice1 == '2':  # Current Cart
                currentCart = cart.currentCart()
                UserInterface.currentCart = currentCart
                while True:
                    print()
                    print('=====***** YOUR CART *****=====')
                    count2 = 0
                    if len(currentCart) == 0:
                        print("Empty :\ ")
                    else:
                        for i in currentCart:
                            count2 += 1
                            print(str(count2) + '_ ' + i)
                    print('=====*********************=====')
                    print()
                    print('1_ Remove from cart')
                    print('2_ Empty cart')
                    print('3_ Back')
                    print()
                    choice2a = input('Enter option number: ')
                    if choice2a == '1':  # Remove from cart
                        if len(currentCart) == 0:
                            print('Your cart is empty!!!')
                        else:
                            choice2b = int(input('Enter cart number to remove from cart: '))
                            del currentCart[choice2b-1]
                            print('Product removed!')
                    elif choice2a == '2':  # Empty cart
                        if len(currentCart) == 0:
                            print('Your cart is already empty!!!')
                        else:
                            cart.emptyCart()
                            currentCart = []
                            UserInterface.currentCart = currentCart
                    elif choice2a == '3':  # Back
                        break
                    else:
                        print('Please select from given options!')
            elif choice1 == '3':  # Back
                break
            else:
                print('Please select from given options!')
