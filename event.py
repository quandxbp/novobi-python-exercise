
# 0 : Knight finish the competition
# 1X : Fighting with Uruk-hai orc.
# 2X : Encounter the Ringwraiths
# 3X : Encounter Strider, a friend of Gandalf
# 4X : Encounter Gollum
# 5X : Encounter Lurtz, the commander of Saruman's Orc forces
# 6X : Encounter Gimli, a dwarf warrior
# 7X : Encounter a beautiful half-elf princess of Rivendell, Arwen
# 8 : Encounter Galadriel, the elven co-ruler of Lothlórien.
# 9X : Encounter Saruman, the fallen head of the Istari Order.

class Event:
    __index = 0
    __eventCode = 0
    __ringSignO = 0
    __levelO = 0 
    
    def __init__(self, eventCode, index):
        self.__index = index
        self.__eventCode = int(eventCode)

    def processEvent(self):
        if self.__eventCode == 0:
            return self.finishJourney()
        elif self.__eventCode < 8 or self.__eventCode == 9 or self.__eventCode > 100 or self.__eventCode in range(80,90):
            return self.eventNotExist()
        
        # Get event of the event code
        i = self.__index
        b = i % 10

        # levelO = i > 6? (b > 5? b : 5) : b
        self.__levelO = (b if b > 5 else 5) if i > 6 else b

        # X factor of event code
        self.__ringSignO = self.__eventCode % 10
        
        event = int(str(self.__eventCode)[:1])
        
        return (event , self.__levelO, self.__ringSignO)

    def eventNotExist(self):
        return (-1, -1 , -1)
    
    def finishJourney(self):
        return (0, -1 , -1)

    def getLevelO(self):
        return self.__levelO
    
    def getRingSignO(self):
        return self.__ringSignO
    
    


