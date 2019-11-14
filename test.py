from string import Template

input("Please what would like to drink? ")
input("How many packs would you like? ")


def Main():
    cart = []
    cart.append(dict(item="Juice", price=100, Qty=3))
    
    t = Template("$Qty x $item = $price")
    Total = 0
    print("Cart:")
    
    for data in cart:
        print(t.substitute(data))
        Total += data["price"]
    print("Total: "+ str(Total))
    
if __name__ == '__main__':
    Main()
