# method overloading
# one class is enough for method overloading
# can have same method names and arguments must be different
from multipledispatch import dispatch


class Product:

    # methods: instance m, static m, class m

    # instance method
    @dispatch(int, str)
    def product_details(self, product_id, product_name):  # instance variables

        print(product_id, product_name)

    @dispatch(int, str, float)
    def product_details(self, product_id, product_name, product_price):
        print(product_id, product_name, product_price)

    @dispatch(str, int)
    def product_details(self, product_id, product_name):  # instance variables
        print(product_id, product_name)


Product().product_details(101, "Sony")
Product().product_details(101, "Mi", 10000.00)
Product().product_details("Mi", 101)
