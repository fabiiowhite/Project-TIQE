import random

def TIQE_Intro():
    print(" ")
    print("---------------------------------")
    print(" ")
    print("Welccome to the TIQE project!")
    print(" ")
    print("---------------------------------")
    print(" ")
def lineBreak():
    print()
def safeDetails(safeName,safeDuration,safeDestribution,safeUsers,safeUsersList):
    print("-----SAFE DETAILS-------")
    print(" ")
    print("Safe name: " +safeName+ "\nSafe duration: "+str(safeDuration)+ "\nSafe Destribution: " +str(safeDestribution)+ "\nSafe users: " +str(safeUsers)+ "\n")
    print("Participants: " + str(safeUsersList))
    lineBreak()
    print("------------------------")
def userRegistration():

    lineBreak()
    print("----User Resgistration-----")
    lineBreak()

    userName = input("Name: ")

    #ID generation per user, ensurance of unique/exclusive generated ID

    while True:
        userId = random.randint(100,999)
        if userId not in generatedIdsList:
            generatedIdsList.append(userId)
            break

    safeUsersList.append(str(userId)+"."+userName)

    lineBreak()
    print("Successful!")
    lineBreak()

TIQE_Intro()

safeUsersList = []
generatedIdsList = []
safeDurationList = ["weekly","monthly"]

#General creation of the xitique/safe

safeName = input("Create a name of the safe for your xitique: ")
lineBreak()

safeDuration = int(input("Choose the duration. Pick 1 for weekly/2 for monthly: "))
lineBreak()

while safeDuration != 1 and safeDuration != 2:
    safeDuration = int(input("Insertion error. Pick 1 for weekly/2 for monthly: "))
    lineBreak()

safeDestribution = int(input("How much will be destributed "+safeDurationList[safeDuration-1]+": "))

safeUsers = int(input("Number of people that will be participating: "))
lineBreak()

for i in range(safeUsers):
    userRegistration()

safeDetails(safeName,safeDuration,safeDestribution,safeUsers,safeUsersList)