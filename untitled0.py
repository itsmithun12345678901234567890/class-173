class parent():
    def __init__(self):
        print("This is Parent Class")
    def menu(dish):
        if dish=="burger":
            print("You can add the following toppings")
            print("More Cheese|Jalapenos")
        elif dish=="iced_americano":
            print("You can add the following toppings")
            print("Add chocolate|Add caramel")
        else:
            print("Please enter Valid Dish")
    def final_amount(dish,add_ons):
        if dish =="burger"and add_ons=="cheese":
            print("you need to pay $3")
        elif dish=="burger" and add_ons=="Jalapenos":
            print("YOU NEED TO PAY 1$")
        elif dish=="iced_americano"and add_ons=="chocolate":
            print("you need to pay 500 dollars")
        elif dish=="iced americano" and add_ons=="caramel":
            print("you need to pay 1 million dolors")
class child1(parent):
    def __init__(self,dish):
        self.new_dish = dish
    def get_menu(self):
        parent.menu(self.new_dish)
class child2(parent):
    
    def __init__(self,dish,addons):
        self.new_dish = dish
        self.addons=addons
    def get_final_amount(self):
        parent.final_amount(self.new_dish,self.addons)
child1_object=child1("burger")
child1_object.get_menu()

child2_object=child2("burger","Jalapenos")
child2_object.get_final_amount()
        