# '''
# Credit: Darinka Zobenica ,
# '''

# Builder design pattern that lets you construct complex objects step by step

# Implementation steps:
# 1) Create the base class
# 2) Create the abstract class / abstract Builder which defines the interface for building
# 3) Builder classes to initialize these values

# Analogy of a Apartment

# from abc import ABC, abstractmethod

class Apartment_Plan:         # Step 1
    def __init__(self):
        self.door = False
        self.basement = False
        self.parkinglot = False
        self.windows = False
        self.doormaterial = []
        self.windowmaterial = []

    def __str__(self):      # Step 2
        string = ""
        if self.door:
            string += "Door \n"
        if self.basement:
            string += "Basement \n"
        if self.parkinglot:
            string += "Parkinglot \n"
        if self.windows:
            string += "Windows \n"
        else:
            string += "HOUSE\n"

        if self.doormaterial:
            string += "DoorMaterial \n"

        for Dmaterial in self.doormaterial:
            string += "- " + str(Dmaterial) + "\n"

        if self.windowmaterial:
            string += "WindowMaterial \n"

        for Wmaterial in self.windowmaterial:
            string += "- " + str(Wmaterial) + "\n"

        return string

class twoBHK_Appartmentdoor:                # Step 5
    def __str__(self):
        return "rose_wood"

class twoBHK_Appartmentwindow:                # Step 5
    def __str__(self):
        return "neem_wood"

class threeBHK_Appartmentdoor:                # Step 5
    def __str__(self):
        return "Sandle_wood"

class threeBHK_Appartmentwindow:                # Step 5
    def __str__(self):
        return "Teak_wood"

class threeBHK_Appartmentgrill:                # Step 5
    def __str__(self):
        return "TMT Strong Iron"


class Apartment_builder(object):             #  Step 3  abstract Builder which defines the interface for building

    # @abstractmethod
    def reset(self):               # resetting to default values
        pass

    # @abstractmethod
    def build_doormaterial(self):        # This should match the Builder class
        pass

    # @abstractmethod
    def build_windowmaterial(self):    # This should match the Builder class
        pass

class twoBHK_Appartment(Apartment_builder):   #  Step 4 Builder classes to initialize these values
    def __init__(self):
        self.Apartment = Apartment_Plan()

    def reset(self):
        self.Apartment = Apartment_Plan()

    def get_apartment(self):
        return self.Apartment

    def build_doormaterial(self):
        self.Apartment.door = True
        self.Apartment.doormaterial.append(twoBHK_Appartmentdoor())  #  Step 5 Declare the class for door material


    def build_windowmaterial(self):  #  Step 5 Declare the class for Window material
        self.Apartment.windows = True
        self.Apartment.windowmaterial.append(twoBHK_Appartmentwindow())


class threeBHK_Appartment(Apartment_builder):  #  Step 4 Builder classes to initialize values
    def __init__(self):
        self.Apartment = Apartment_Plan()

    def reset(self):
        self.Apartment = Apartment_Plan()


    def get_apartment(self):
        return self.Apartment

    def build_doormaterial(self):
        self.Apartment.door = True
        self.Apartment.doormaterial.append(threeBHK_Appartmentdoor())    #  Step 5 Declare the class for door material

    def build_windowmaterial(self):          #  Step 5 Declare the class for Window material
        self.Apartment.windows = True
        self.Apartment.windowmaterial.append(threeBHK_Appartmentwindow())
        self.Apartment.windowmaterial.append(threeBHK_Appartmentgrill())

if __name__ == "__main__":
    builder = twoBHK_Appartment()
    builder.build_doormaterial()
    # print(builder.get_apartment())
    builder.build_windowmaterial()
    print(builder.get_apartment())

    builder1 = threeBHK_Appartment()
    builder1.build_doormaterial()
    builder1.build_windowmaterial()
    print(builder1.get_apartment())




