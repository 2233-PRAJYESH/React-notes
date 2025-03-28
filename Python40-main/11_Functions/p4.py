# global keyword
def get_product_details():

    global product_id
    product_id = 101  # local v
    product_name = "Apple"
    product_price = 20000.00

    print(product_id, product_name, product_price)


get_product_details()

print('Outside:', product_id)



