# '''
# Credit: Darinka Zobenica
# '''


# Abstract Factory design pattern that lets you produce families of related objects
# without specifying their concrete classes.
# Abstract Factory design pattern is simillar to Factory design pattern , but the difference is
# in AFD we do not have same variables/arguments for other classed , but in FD we have same nature variables/arguments for many classes.

# Implementation steps:
#
# 1) Explicitly declare interfaces for each distinct product of the product family
# 2) make calls to all the classed of particular family
#
#
# Analogy of a Furniture shop

# from abc import ABC, abstractmethod

class Furniture_shop(object):
    def Purchase(self):
        pass

class Chair_normal(Furniture_shop):
    product = "Chair_NORMAL"
    def Purchase(self):
        print("This is a normal chair :" +self.product)

class Sofa_normal(Furniture_shop):
    product = "Sofa_NORMAL"
    def Purchase(self):
        print("This is a normal Sofa :" +self.product)

class Chair_royal(Furniture_shop):
    product = "Chair_ROYAL"
    def Purchase(self):
        print("This is a ROYAL chair :" +self.product)

class Sofa_royal(Furniture_shop):
    product = "Sofa_ROYAL"
    def Purchase(self):
        print("This is a ROYAL Sofa :" +self.product)



# ##############################################################

class furniture_type(object):
    def product(type_of_product):
        pass

class Normal_customer(furniture_type):
    def product(type_of_product):
        if type_of_product == "chair":
            return Chair_normal()
        if type_of_product == "sofa":
            return Sofa_normal()

    def product_chair(self):
        return Chair_normal()

    def product_sofa(self):
        return Sofa_normal()


class Royal_customer(furniture_type):
    def product(type_of_product):
        if type_of_product == "chair":
            return Chair_royal()
        if type_of_product == "sofa":
            return Sofa_royal()

    def product_chair(self):
        return Chair_royal()

    def product_sofa(self):
        return Sofa_royal()

################################################################

class Furniture_purchase:
    def get_furniture(self , type_of_customer):
        if type_of_customer == "Royal":
            return Royal_customer
        if type_of_customer == "Normal":
            return Normal_customer


if __name__ == "__main__":

    obj = Furniture_purchase()

    obj1= obj.get_furniture("Royal")
    chair = obj1.product("chair")
    chair.Purchase()

    obj2= obj.get_furniture("Normal")
    sofa = obj2.product("sofa")
    sofa.Purchase()