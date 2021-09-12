import socket

class Assignment2:

    # Task 1 - Constructor
    def __init__(self, age):
        self.age = age

    # Task 2 - Birth Year
    def tellBirthYear(self, currentYear):
        age = self.age
        print("Your birth year is " + str(currentYear - age))

    # Task 3 - List
    def listAnniversaries(self, n):
        arr = []
        i = 1
        while (i <= self.age):
            if (i%n == 0):
                arr.append(i)
                i = i + n
            else:
                i = i + 1

        return arr

    # Task 4 - String Manipulation
    def modifyAge(self, n):
        age = str(self.age)
        age1 = str(self.age * n)
        result = age1

        i = 0
        age2 = ""
        while (i < n):
            age2 = age2 + age[0]
            i = i + 1
        result = result + age2

        age3 = ""
        temp = self.age ** n
        ageN = str(temp)
        i = 0
        while(i <= len(ageN)):
            age3 = age3 + ageN[i]
            i = i + 2
        result = result + age3

        return result

    # Task 5 Loop and Conditional statements
    def checkGoodString(string):
        length = False
        lowercase = False
        checkNum = False
        result = False

        if len(string) >= 8:
            length = True

        firstChar = string[0].islower()

        if firstChar == True:
            lowercase = True

        for char in string:
            if char.isnumeric():
                checkNum = True
                break

        if length == True and lowercase == True and checkNum == True:
            result = True

        return result

    # Task 6 - Socket
    def connectTcp(host, port):
        success = False
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((host, port))
            success = True
        except:
            success = False

        return success
