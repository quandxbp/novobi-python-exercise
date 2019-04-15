from general import *
from knight import Knight
from event import Event


class Battle:
    knightTuple = tuple()

    def __init__(self, fileName):
        self.knightTuple = self.processDataFromFile(fileName)

    def processDataFromFile(self, fileName):
        # Read data from file
        dataFromFile = readFile("./" + fileName)

        # Separating the data from file into two lines
        data = dataFromFile.split("\n")

        # Assign data
        dataFirstLine = data[0]

        # Assign knight infomation
        splitDataFirstLine = dataFirstLine.split(" ")
        knightHp = splitDataFirstLine[0]
        knightLevel = splitDataFirstLine[1]
        knightRingSign = splitDataFirstLine[2]

        # Get journey list
        journeyList = list()
        for index in range(1, len(data)):
            journeyList += data[index].split(" ")
        
        # Remove '' element
        while '' in journeyList:
            for x in journeyList:
                if x == '':
                    journeyList.remove(x)
            
        print(journeyList)
        return (knightHp, knightLevel, knightRingSign, journeyList)

    def fightImplementation(self):
        # [0] is knightHp, [1] is knightLevel, [2] is knightRingSign, [3] is journeyList
        knight = Knight(self.knightTuple[0], self.knightTuple[1], self.knightTuple[2], self.knightTuple[3])

        # Get knight ring sign list
        knightRingSignList = knight.getRingSignList()

        index = 1
        for journey in knight.getJourneyList():
            #Get knight Hp
            knightHp = knight.getKnightHp()
            # If knight Hp <= 0 => Lose the game
            if knightHp <= 0 : break
            # Get index of the journey
            indexJourney = index
            # Increase index
            index += 1

            # Create event object
            # print(str(journey) + " " + str(indexJourney))
            eventObj = Event(journey, indexJourney)

            # [0] is code, [1] is levelO, [2] is ringSignO
            eventTuple = eventObj.processEvent()

            # Get Event
            event = eventTuple[0]

            # Case finish journey
            if event == 0:
                print("Knight finish the competition !")
                break
            # Case pass journey
            elif event == -1:
                continue

            knightRingSignList, knightHp = self.processBattleCase(event, knightHp, knight.getKnightMaxHp(), knight.getKnightLevel(), knightRingSignList, eventObj.getLevelO(), eventObj.getRingSignO())
            
            knight.setKnightHp(knightHp)

        # print(knight.getRingSignList())
        stringRingSignList = [str(x) for x in knightRingSignList]
        stringRingSignList = "".join(stringRingSignList)

        return stringRingSignList, knight.getKnightHp()
    
    def processBattleCase(self, event, knightHp, knightMaxHp, knightLevel, knightRingSignList, levelO, ringSignO):
        # The knight encounter a beautiful half-elf princess of Rivendell, Arwen.
        if event == 7:
            return self.event7_EncounterArwen(knightRingSignList, ringSignO), knightHp
        # Encounter Galadriel, the elven co-ruler of Lothlórien.
        elif event == 8:
            return self.event8_EncounterGaladriel(knightRingSignList, knightHp, knightMaxHp )

        # The knight win the battle
        if knightLevel > levelO:
            knightRingSignList.append(ringSignO)
            # the knight defeats Saruman
            if event == 9:
                knightRingSignList = self.event9_EncounterSaruman(knightRingSignList, winFlag =  True)
        # The knight lose the battle
        elif knightLevel < levelO:
            # the knight loses to Gollum
            if event == 4:
                knightRingSignList = self.event4_EncounterGollum(knightRingSignList, ringSignO)
            #  the knight loses to Lurtz
            elif event == 5:
                knightRingSignList = self.event5_EncounterLurtz(knightRingSignList)
            # the knight loses Saruman
            elif event == 9:
                knightRingSignList = self.event9_EncounterSaruman(knightRingSignList, ringSignO, winFlag = False)
            # Get damage 
            damage = self.getdamage(event, levelO)
            # Recalculating the knight hp

            knightHp = int(knightHp - damage)
            
            # If the knight loses the battle
            if knightHp <= 0:
                knightRingSignList = []
                return knightRingSignList, knightHp
        # The battle is tie
        else: 
            return knightRingSignList, knightHp
        # print("knightHP : " + str(knightHp))
        return knightRingSignList, knightHp
    
    def event1_FightingUruk(self):
        pass

    def event2_EncounterRingwraiths(self):
        pass

    def event3_EncounterStrider(self):
        pass

    # If the knight loses to Gollum, Gollum will take the last ringsign with its same number
    # from the knight's EC. If no such ringsign exists in the knight's EC list, Gollum will do nothing (the
    # knight still loses HP
    def event4_EncounterGollum(self, knightRingSignList, ringSignO):
        foundIndex = -1

        for index in range(0, len(knightRingSignList)):
            if knightRingSignList[index] == ringSignO:
                foundIndex = index
        
        if foundIndex != -1:
            knightRingSignList.pop(foundIndex)
        
        return knightRingSignList
        
    def event5_EncounterLurtz(self, knightRingSignList):
        
        return knightRingSignList[3::]

    def event6_EncounterGimli(self):
        pass

    # she will take all the knight's
    # ringsigns and grant the knight a different Elrond’s Code so that the new the Elrond’s Code of the
    # knight will be greater than the old properly X units.
    def event7_EncounterArwen(self, knightRingSignList, ringSignO):
        index = 1
        
        try:
            tempRingSignO = knightRingSignList[-index] + ringSignO
        # In case there is no ring sign in list
        except IndexError:
            # tempRingSignO = ringSignO
            # knightRingSignList.append(tempRingSignO)
            return knightRingSignList
        
        if tempRingSignO < 10:
            knightRingSignList[-1] = tempRingSignO

        while tempRingSignO > 9:
            newValue = int((str(tempRingSignO)[-1]))
            
            knightRingSignList[-index] = newValue

            walker = index + 1
            
            # If the index is out of range
            if walker > len(knightRingSignList):
                knightRingSignList = [0] + knightRingSignList
            else:
                knightRingSignList[-walker] = knightRingSignList[-walker] + 1
                
                tempRingSignO = knightRingSignList[-walker]

                index += 1
        
        return knightRingSignList

    # Galadriel is the elven co-ruler of Lothlórien alongside her husband. When the knight meets
    # Galadriel, the knight will trade the last rignsign in his Elrond’s Code to restore his HP to maxHP.
    # If the knight’s HP is equal to maxHP, the knight will not do the trade.
    def event8_EncounterGaladriel(self, knightRingSignList, knightHp, knightMaxHp ):
        if knightHp != knightMaxHp:
            # If ring sign list is empty => Do not trade
            if knightRingSignList == []:
                return knightRingSignList, knightHp
            knightRingSignList = knightRingSignList[:-1]
            knightHp = knightMaxHp

        return knightRingSignList, knightHp
            
    # If the knight defeats and takes ringsign from Saruman, Saruman will reverse the order
    # of the knight's EC list. On the other hand, if the knight loses Saruman, Saruman would snatch all
    # the ringsigns with the same number on the ringsign of Saruman.
    def event9_EncounterSaruman(self, knightRingSignList, *ringSignO , winFlag):
        if winFlag is True:
            return knightRingSignList[::-1]
        else :

            # Get the index of element with has the same value with Saruman ringsign
            for x in knightRingSignList:
                if x == ringSignO:
                    knightRingSignList.remove(x)

            return knightRingSignList
    
    def getdamage(self, event, levelO):
        baseDamage = {
            1 : 0.8,
            2 : 1.2,
            3 : 4.1,
            4 : 7.9, 
            5 : 6.5,
            6 : 8.7,
            9 : 0.1
        }
        
        damage = round(baseDamage.get(event)* levelO* 10)

        print("DAMAGE : " + str(baseDamage.get(event)) + " * " + str(levelO) + " * "+ "10 = " + str(damage))

        return damage
        
    
    
            

            

            

        