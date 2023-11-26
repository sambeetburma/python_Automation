products = [
    {"name": "Laptop", "price": 600000},
    {"name": "phone", "price": 25000},
    {"name": "smartwatch", "price": 10000},
    {"name": "Headphones", "price": 5000}
]

print(type(products))
print(type(products[0]))


def is_affordable(products):
    print(products)
    print("which type",type(products))
    #print(item["name"])
    return products["price"] < 20000


affordable_items = list(filter(is_affordable, products))
print(affordable_items)
