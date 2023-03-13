from datetime import datetime
import csv
import random

print("Hi! Welcome to pizza order system!")

menu_txt = '''*Please Choose a Base Pizza
1: Classic
2: Turkish Pizza
3: Plain Pizza
4: Margherita
*choose your sauces:
5: Olives
6: Mushrooms
7: GoatCheese
8: Meat
9: Onions
10: Corn
*Thank You!
'''

with open('Menu.txt','w') as file:
    file.write(menu_txt)

class Pizza:
    def __init__(self,description=None,cost=None):
        self.description = description
        self.cost = cost

    def get_cost(self):
        return self.cost
    def get_description(self):
        return self.description

class Classic(Pizza):
    def __init__(self):
        super().__init__("Classic Pizza",69.99)

class Turkish_Pizza(Pizza):
    def __init__(self):
        super().__init__("Turkish Pizza",89.99)

class Margherita(Pizza):
    def __init__(self):
        super().__init__("Margherita",85.99)

class Plain_Pizza(Pizza):
    def __init__(self):
        super().__init__("Plain Pizza",74.99)



class Decorator(Pizza):
    def __init__(self):
        super().__init__()

    def get_cost(self):
        return self.cost
    def get_description(self):
        return self.description


class GoatCheese(Decorator):
    def __init__(self):
        super().__init__()
        self.description="Goat Cheese"
        self.cost = 7.49

class Meat(Decorator):
    def __init__(self):
        super().__init__()
        self.description="Meat"
        self.cost = 16.99

class Mushrooms(Decorator):
    def __init__(self):
        super().__init__()
        self.description="Mushrooms"
        self.cost = 9.99

class Olives(Decorator):
    def __init__(self):
        super().__init__()
        self.description="Olives"
        self.cost = 4.99

class Corn(Decorator):
    def __init__(self):
        super().__init__()
        self.description="Corn"
        self.cost = 8.49

class Onions(Decorator):
    def __init__(self):
        super().__init__()
        self.description="Onions"
        self.cost = 5.99


def main():
    with open('Menu.txt','r') as f_menu:
        for i in range(5):
            line = f_menu.readline()
            print(line,end="")

    pizza_selection = int(input("Select your base pizza(1-4): "))

    if pizza_selection == 1:
        pizza = Classic()

    elif pizza_selection == 2:
        pizza = Turkish_Pizza()

    elif pizza_selection == 3:
        pizza = Plain_Pizza()

    elif pizza_selection == 4:
        pizza = Margherita()

    else:
        print("Wrong choice! Please try again...")

    amount = pizza.get_cost()
    sauce_cost= 0.0

    with open('Menu.txt', 'r') as f_menu:
        for i, line in enumerate(f_menu):
            if 5 <= i <= 11:
             print(line,end="")
    sauce_selection = int(input("Select your sauce(5-10): "))

    if sauce_selection == 5:
        sauce = Olives()
        sauce_cost = (sauce.get_cost())

    elif sauce_selection == 6:
        sauce = Mushrooms()
        sauce_cost = (sauce.get_cost())

    elif sauce_selection == 7:
        sauce = GoatCheese()
        sauce_cost = (sauce.get_cost())

    elif sauce_selection == 8:
        sauce = Meat()
        sauce_cost=(sauce.get_cost())

    elif sauce_selection == 9:
        sauce = Onions()
        sauce_cost=(sauce.get_cost())

    elif sauce_selection == 10:
        sauce = Corn()
        sauce_cost=(sauce.get_cost())

    else:
        print("Wrong choice! Please try again...")


    total_cost = amount + sauce_cost

    print("*****************ORDER INFORMATION IS BELOW*****************")
    customer = input("Name: ")

    number = random.randint(1000, 9999)
    print("Your order number:", number)
    print("Your pizza is getting ready...")
    print("YOUR ORDER IS READY!")
    order_description= pizza.get_description()+" with this "+sauce.get_description()+" equals to "+" %.2f"%(total_cost)+" TL."

    print("Order: ",order_description)
    order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Order Time:",order_time)

    with open('Order_Database.csv', 'r+', newline='') as file:
        writer = csv.writer(file)
        first_line = file.read()
        if not first_line:
            writer.writerow(['Name', 'Order Number', 'Total Cost', 'Order Time', 'Order Description'])

        writer.writerow([customer, number, " %.2f"%(total_cost), order_time,order_description])


if __name__ == "__main__":
    main()














