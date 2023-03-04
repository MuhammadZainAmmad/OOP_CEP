class Admin:  # Controls the admin activity
    def __init__(self):
        self.adminE = 'admin@gmail.com'
        self.password = '123'

    def addProduct(self):  # Add a new product with its properties to existing product list or file
        try:
            name = input('Enter product name: ')
            color = input('Enter color of product: ')
            ram = input('Enter RAM in product: ')
            price = int(input('Enter price of product: '))
            product = [name, ['color', color], ['RAM', ram], ['Price', price]]
            f = open('Products.txt', 'a')
            f.write(str(product) + '\n')
            f.close()
            print('Product added!')
        except ValueError:
            print('Please enter price in integer not in string')
            self.addProduct()

    def deleteProduct(self):  # Delete a product from product list or file
        product = input('Enter name of product to delete: ')
        try:
            f = open('Products.txt', 'r')
            lines = f.readlines()
            f.close()
            evalLines = []
            for i in lines:
                line = eval(i)
                evalLines.append(line)
            for i in evalLines:
                if i[0] == product:
                    evalLines.remove(i)
                    print()
                    print("Product removed successfully!")
            f = open('Products.txt', 'w')
            for line in evalLines:
                f.write(str(line) + '\n')
            f.close()
        except FileNotFoundError:
            print("No product available!!!")
            pass


#a = Admin()
# a.addProduct()
# a.addProduct()
# a.addProduct()
#a.deleteProduct()