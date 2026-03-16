owner = input("Type your name here-->")
items = []

cart = (owner,items)

print("==================\n")
print("Type the items you want to add to your cart. If you don't want to add any more items, type 'Done'")
print("You can also type 'View' to view the items in your cart")

def addItem():
    global cart
    item = ""
    while item != "Done" and item != "View":
        item = input("Type your item here-->")
        if item != "Done" and item!="View":
            items.append(item)
        else:
            break    
    

    if item == "Done":
        done()
    elif item == "View":
        doneYes = False
        view(doneYes)

def done():
    doneYes = True
    viewOrNot = input("You have filled your cart, would you like to view it[Yes/No] -->")
    if viewOrNot == "Yes":
        view(doneYes)

def view(doneYes):
    global cart
    if doneYes:
   
        print("Cart Owner -->", cart[0])
        for i in range(len(cart[1])):
            print(str(i+1)+".",cart[1][i])

    elif doneYes == False:
        print("Cart Owner -->", cart[0])

        for i in range(len(cart[1])):   
            print(str(i+1)+".",cart[1][i])
        print("\n")
        addItem()


addItem()