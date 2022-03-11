#####LIMITS#####
'''
- MAX NUMBER IS 2**25 WHICH SHOULD BE MORE THAN BETTER

'''
#####IMPORTS#####

##### CODE ######

class BinaryNumber:
    def __init__(self,nVal):
        self.nVal = nVal
        self.highestPower = None

    def biggestSquare(self):
        Nnum = self.nVal
        for x in range(0,25):
            if Nnum <= (2**x):
                self.highestPower = (x)
                break
        print(str(2**self.highestPower) +" is the biggest square")
        return(None)


    def generate_binary_numbers(self):
        self.biggestSquare()
        binaryOutput = []
        workingNumber = self.nVal
        for i in range((self.highestPower+0),-1,-1):
            if (2**i) <= workingNumber:
                binaryOutput.append("1")
                workingNumber = workingNumber - (2**i)
            else:
                binaryOutput.append("0")
        print("".join(binaryOutput))






    def binCountDown(self):
        for i in range(0,self.nVal):
            print(i)


seven =BinaryNumber(257)

seven.generate_binary_numbers()
