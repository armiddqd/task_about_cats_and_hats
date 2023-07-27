# Task 1 - Book


class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity


class Book(Product):
    def __init__(self, name, price, quantity, author: str):
        super().__init__(name, price, quantity)
        self.author = author

    def read(self):
        print(f'You are looking for a book named {self.name}')
        print(f'Welcome {self.author} as the author of the book')
        print(f'You can buy it for {self.price} bucks')
        print(f'Only {self.quantity} left!')


the_book = Book('Cat\'s Cradle', 10.67, 2, 'Kurt Vonnegut')

the_book.read()

# Task - 2 Restaurant


class Restaurant:
    def __init__(self, name, cuisine, menu: dict):
        self.name = name
        self.cuisine = cuisine
        self.menu = {}
        # the task text asks not to add quantity into menu
        # but later it's used for quantity calculation
        for key, value in menu.items():
            self.menu[key] = value


class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu: dict, drive_thru: bool):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, dish_name, quantity):

        if dish_name not in self.menu.keys():
            return 'Dish not available'
        elif quantity > self.menu[dish_name]['quantity']:
            return 'Requested quantity not available'
        else:
            order_sum = self.menu[dish_name]['price'] * quantity
            return order_sum


menu = {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5))  # 25
print(mc.order('burger', 15))  # Requested quantity not available
print(mc.order('soup', 5))  # Dish not available
