# Task 1: using private attributes
class Product(object):

    # instance method / special method / constructor
    def __init__(self, productName, productModel, productCost): # instance v

        self.pName = productName  # public
        self.__pModel = productModel  # private
        self.__pCost = productCost  # private

        # print(self.pName, self.__pModel, self.__pCost)

    def display(self):
        print(self.pName, self.__pModel, self.__pCost)  # Mi Mi pro 10000


p = Product("Mi", "Mi pro", 10000)  # Mi Mi pro 10000
p.display()

print(p.pName)
# print(p.__pModel)  # AttributeError: 'Product' object has no attribute '__pModel'
# print(p.__pCost)   # AttributeError: 'Product' object has no attribute '__pModel'

# Mangling
print(p.pName)

# objectRef._ClassName__privateAttribute
print(p._Product__pModel)  # Mi pro
print(p._Product__pCost)   # 10000






