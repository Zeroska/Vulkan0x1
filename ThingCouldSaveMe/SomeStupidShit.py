#!/usr/bin/python3.7 




#Level of electricity usage start from level 1 
level1 = 83900 #I don't think of a proper name right now so ...
level2 = 86700 #shit I'm drunk again 
level3 = 201400
level4 = 253600
level5 = 283400 #pure garbage

#USER PLEASE ENTER
userInput = int(input())

def processUserInput(userInput): #not a good function but still it works 
    totalMoney = 0.0 #Don't judge me :V :V 
    if (userInput >= 0 and userInput <= 50):
        totalMoney = userInput * 1678 #LEVEL 1 
    elif(50 < userInput and userInput <= 100): #omg look at this condtion, who the fuck would wrote this line ????
        totalMoney = ((userInput - 50) * 1734) + level1 #LEVEL 2
    elif(100 < userInput and userInput <= 200):
        totalMoney = ((userInput - 100) * 2014) + level1 + level2 #LEVEL 3
    elif(200 < userInput and userInput <= 300):   #HOLY SHIT TOO MANY MAGIC NUMBER 
        totalMoney = ((userInput - 200) * 2536) + level1 + level2 + level3 #LEVEL 4
    elif(300 < userInput and userInput <= 400):
        totalMoney = ((userInput - 300) * 2834) + level1 + level2 + level3 + level4 #LEVEL 5
    else:
        totalMoney = ((userInput - 400) * 2927) + level1 + level2 + level3 + level4 + level5
    shitTotalMoney = totalMoney + (totalMoney * 10.0/100)
    return shitTotalMoney



print(processUserInput(userInput))