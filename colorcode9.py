# Product Colour Code Lookup

stock = {
    (255, 0, 0): 50,      # Red
    (0, 255, 0): 30,      # Green
    (0, 0, 255): 20,      # Blue
    (255, 255, 0): 15     # Yellow
}

r = int(input("Enter R value: "))
g = int(input("Enter G value: "))
b = int(input("Enter B value: "))

colour = (r, g, b)

if colour in stock:
    print("Stock Quantity:", stock[colour])
else:
    print("Colour code not found.")