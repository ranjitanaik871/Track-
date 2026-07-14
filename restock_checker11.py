# Inventory Restock Checker

inventory = {
    "Pen": 50,
    "Notebook": 15,
    "Pencil": 30,
    "Eraser": 10,
    "Marker": 25
}
#products store the name from inventory
#stock<20 checks the condition
for product, stock in inventory.items():
    if stock < 20:
        print(product, "- Reorder Needed")
    else:
        print(product, "- Stock OK")