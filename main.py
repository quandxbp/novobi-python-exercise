from battle import Battle
from general import *
import sys

def knight_journey_to_file(filename,case):

    battle = Battle(filename)

    result = battle.fightImplementation()

    print("Fighter Elrond’s Code : " +  result[0])
    print("Fighter HP : " +  str(result[1]))
    print("------------------------------------------------")
    if result[0] == "":
        appendTextFile("./result.txt",str(case) + " " + "LOSE" + " " + str(result[1]))
    else:
        appendTextFile("./result.txt",str(case) + " " + str(result[0]) + " " + str(result[1]))

def knight_journey(filename):

    battle = Battle(filename)

    result = battle.fightImplementation()

    return result[0]

def compare():

    myResult = readFile("./result.txt").split("\n")
    binhResult = readFile("./binh.txt").split("\n")

    for x in range(1,351):
        if myResult[x] != binhResult[x]:
            print(myResult[x])
            print(binhResult[x])
            print("\n")


if __name__ == "__main__":
    # knight_journey(sys.argv[1:][0])
    # knight_journey("Input/input (244).txt")
    # appendTextFile("./result.txt", "Case RingSignList KnightHp")

    for index in range(1,351):
        try:
            print("Test case : " + str(index) )
            knight_journey_to_file("Input/input (" + str(index) + ").txt", index)
        except Exception as e:
            print("Test case Error " + str(index) + " : " + str(e))

    compare()
