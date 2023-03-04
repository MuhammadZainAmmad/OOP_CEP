class Products:  # return the list of hard coded products list as well as their details
    def __init__(self):
        self.productList = []
        Products.getProductList(self)

    def getProductList(self):  # return list of products available
        try:
            f = open('Products.txt', 'r')
            for line in f:
                product = eval(line)
                self.productList.append(product[0])
            f.close()
        except FileNotFoundError:
            print('No products available :(')

    def getProductDetails(self, product):  # return product detail on passing name of product
        f = open('Products.txt', 'r')
        for line in f:
            lst = eval(line)
            if lst[0] == product:
                return lst
            else:
                pass


# a = Products()
# print(a.getProductDetails('Realme 5i'))
# print(a.productList)
