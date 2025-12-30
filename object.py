class VendingMachine:
    def __init__(self,name):
        self.name = name
        self.deposit = 0
        self.cup_stock = 0

    def add_cup(self,num):
        self.cup_stock += num

        if self.cup_stock > 100:
            self.cup_stock = 100

    def press_button(self,item):
        if self.deposit < item.price:
            return ""
        
        if isinstance(item, CupCoffee):
            if self.cup_stock <= 0:
                return ""
            self.cup_stock -= 1
        
        self.deposit -= item.price
        return item.name
            

    def _press_manufacturer_name(self):
        return self.name
    
    def deposit_coin(self,money):
        if money == 100 :
            self.deposit += money

class Item:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class Beverage(Item):
    def __init__(self,name):
        if name == "cola":
            price = 150
        else:
            price = 100
        super().__init__(name,price)

class CupCoffee(Item):
    def __init__(self, type):
        name = f"{type} cup coffee"
        super().__init__(name,100)

class Snack(Item):
    def __init__(self):
        super().__init__("potato chips",150)   
    

hot_cup_coffee = CupCoffee('hot')  # カップコーヒーのクラス
cider = Beverage('cider')  # 飲み物のクラス
snack = Snack()  # スナック菓子のクラス
vending_machine = VendingMachine('サントリー')
vending_machine.deposit_coin(100)
vending_machine.deposit_coin(100)
print(vending_machine.press_button(cider))

print(vending_machine.press_button(hot_cup_coffee))
vending_machine.add_cup(1)
print(vending_machine.press_button(hot_cup_coffee))

print(vending_machine.press_button(snack))
vending_machine.deposit_coin(100)
vending_machine.deposit_coin(100)
print(vending_machine.press_button(snack))