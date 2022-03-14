#####LIMITS#####
'''
- MAX NUMBER IS 2**25 WHICH SHOULD BE MORE THAN BETTER
'''
#####IMPORTS#####
import copy

##### CODE ######

class BinaryNumber:
    def __init__(self):
        self.nVal = None
        self.nValBin = None
        self.countdownArray = []
        self.gapValue = 0

    def reverseStr(self,stringIn):
        newReversedStr = ""
        for i in range(len(stringIn)-1,-1,-1):
            newReversedStr = newReversedStr + stringIn[i]
        return(newReversedStr)

    def generate_binary_numbers(self,decToBin):
        
        localN = copy.deepcopy(decToBin)

        if decToBin >= 1:
            
            currentBinaryNum = ""
            while localN != 0:
                if (localN % 2) == 1: 
                    currentBinaryNum = currentBinaryNum + "1"
                    localN = (localN-1)/2
                else:
                    currentBinaryNum = currentBinaryNum + "0"
                    localN = (localN)/2
            self.countdownArray.append(self.reverseStr(currentBinaryNum))
            if decToBin == self.nVal:
                self.nValBin = (self.reverseStr(currentBinaryNum))
            decToBin = decToBin-1
            self.generate_binary_numbers(decToBin)



    def binaryGap(self,index,streak):
        
        if index <= len(self.nValBin)-1:
            if self.nValBin[index] == "0":
                streak = streak+1
            elif self.nValBin[index] == "1":
                #print("wrote "+str(streak))
                if streak >= self.gapValue:
                    #print("wrote "+str(streak))
                    self.gapValue = streak+1
                streak = 0
            index = index + 1
            self.binaryGap(index,streak)

            
      

    def main(self):
        self.nVal = 22
        decToBin = copy.deepcopy(self.nVal)
        self.generate_binary_numbers(decToBin)
        print("Output final array: "+str(self.nValBin))
        self.binaryGap(0,1)
        print(self.gapValue)


if __name__ == "__main__":
    BinaryNumber().main()
