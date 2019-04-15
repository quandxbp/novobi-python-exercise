class Knight:
    __knightHp = 0
    __knightMaxHp = 0
    __knightLevel = 0
    __knightRingSign = 0
    __journeyList = list()
    __ringSignList = list()

    def __init__(self, knightHP, knightLevel, knightRingSign, knightJourneyList):
        self.__knightHp = int(knightHP)
        self.__knightMaxHp = int(knightHP)
        self.__knightLevel = int(knightLevel)
        self.__knightRingSign = knightRingSign
        self.__ringSignList = [int(knightRingSign)]
        self.__journeyList = knightJourneyList

    # Get set knight hp
    def getKnightHp(self):
        return self.__knightHp

    def setKnightHp(self, newKnightHp):
        self.__knightHp = newKnightHp
    
    # Get set knight hp
    def getKnightMaxHp(self):
        return self.__knightMaxHp

    def setKnightMaxHp(self, knightBaseHp):
        self.__knightMaxHp = knightBaseHp

    # Get set knigh level
    def getKnightLevel(self):
        return self.__knightLevel

    def setKnightLevel(self, newKnightLevel):
        self.__knightLevel = newKnightLevel
    
    # Get set knigh level
    def getRingSign(self):
        return self.__knightRingSign

    def setRingSign(self, newRingSign):
        self.__knightRingSign = newRingSign

    # Get, append, clear journet list
    def getJourneyList(self):
        return self.__journeyList
    
    def appendJourneyList(self, journey):
        self.__journeyList.append(journey)

    def clearJourneyList(self):
        self.__journeyList.clear()
    
    # Get, append, clear ring sign list
    def getRingSignList(self):
        return self.__ringSignList
    
    def appendRingSignList(self, ringSign):
        self.__ringSignList.append(ringSign)

    def clearRingSignList(self):
        self.__ringSignList.clear()



        
    


    

        
        

    
