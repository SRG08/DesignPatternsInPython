# """
# Credit: Darinka Zobenica ,
# """

# Factory Design pattern provides an interface for creating objects in a superclass,
# but allows subclasses to alter the type of objects that will be created

# Implementation steps :

# Replace direct object construction calls (using the new operator) with calls to a special factory method
# override the factory method in a subclass and change the class of products being created by the method.

# Analogy of Transport Company

class Logistics(object):                 # Creat a Super class
    def  driver_working(self):
        pass

class Roadways(Logistics):                # subclass 1
    def __init__(self , drivername , weeklyhours , workinghours):  # Parameter related to Rodways business
        self.drivername = drivername
        self.weeklyhours = weeklyhours
        self.workinghours = workinghours
        self.logestic_type = "Roadways"

    def calcWorking(self):                        # Method for calculating working hours (did not call in this example)
        return self.workinghours /self.workinghours

    def __str__(self):
        return self.drivername+" ["+str(self.workinghours)+"] "+str(self.weeklyhours)+" "+str(self.logestic_type)


class SteamerBoat(Logistics):          # subclass 2
    def __init__(self , drivername ,  weeklyhours , workinghours ):
        self.drivername = drivername
        self.weeklyhours = weeklyhours
        self.workinghours = workinghours
        self.logestic_type = "SteamerBoat"


    def calcWorking(self):      # Dummy Method of SteamerBoat(did not call in this example)

        if self.workinghours:
            return self.workinghours+2
        else:
            return self.workinghours+5

    def __str__(self):
        if self.workinghours:
            return self.drivername+"["+str(self.workinghours)+"] "+str(self.weeklyhours)+" "+str(self.logestic_type)
        # else:
        #     return self.drivername+"["+str(self.workinghours)+"] "+str(self.weeklyhours)+" "+str(self.logestic_type)



class LogisticsCompany:            # Factory Class for calling all the businesses
    def get_driver(self , type_of_transport):
        if type_of_transport == 'Roadways':
            return Roadways("Jhon" , 40 , 40  , )
        else:
            return SteamerBoat("Smith" , 45 , 40)

if __name__ == "__main__":

    Transport_type = LogisticsCompany()

    Logistics_R = Transport_type.get_driver('Roadways')
    print(Logistics_R)

    Logistics_S = Transport_type.get_driver('SteamerBoat')
    print(Logistics_S)



