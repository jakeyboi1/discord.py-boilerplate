#importing the needed modules
import random

#random number generator function
def generateRandomNumber(minimumNumber, maximumNumber): #defines function generateRandomNumber with the parameters minimumNumber, and maximumNumber
    return random.randint(minimumNumber, maximumNumber) #returns a randomly generated number between the minimumNumber and the maximumNumber