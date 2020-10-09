'''
Credit:

'''

# Strategy design pattern can change algorithms during runtime.


# Implementation steps:
#
# create an object which can change algorithms and represents different strategies
# Context object which will change its behavour as per the strategies.


# Analogy: Menu and Tourist type  ( When Coder is Hungry ;-) )

class Tourist:
    def __init__(self , Menu , TouristType = None):
        self.TouristType = TouristType
        self.Menu = Menu


    def Tourist_type(self):
        if self.TouristType:
            Touristtype  = self.TouristType(self)
            return Touristtype
        else:
            print("There is no tourist type")


    def __str__(self):
        tourist = self.Tourist_type()
        menue = self.Menu
        TT = "<Menu: {}, TouristType: {}>"
        return TT.format(menue , tourist)


def Asian_Tourist(Tourist):
    if Tourist.Menu == "Pizza":
        return("Asian Tourist doesnt like : "   +  Tourist.Menu)
    else:
        return ("Asian Tourist likes : "  +  Tourist.Menu)



def American_Tourist(Tourist):
    if Tourist.Menu == "Biryani":
        return("American Tourist doesnt like : "   +  Tourist.Menu)
    else:
        return ("American Tourist like : "   +  Tourist.Menu)


if __name__ == "__main__":

    tourist1 = Tourist("Biryani" , TouristType = Asian_Tourist)
    tourist2 = Tourist("Pizza" , TouristType = American_Tourist)
    tourist3 = Tourist("Pizza" , TouristType = Asian_Tourist)
    tourist4 = Tourist("Biryani" , TouristType = American_Tourist)
    print(tourist1)
    print(tourist2)
    print(tourist3)
    print(tourist4)