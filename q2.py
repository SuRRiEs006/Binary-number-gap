class BinaryNumber:
    def __init__(self, number):
        self.number = number

    def generate_binary_numbers(self):
        queue = []
        large_string = ""
        for x in range(self.number, 0, -1):
            queue.append(x)
        for N in queue: 
            L = []
            if N == 0:
                L.append(str(0))
            while(N != 0):
                temp = N % 2
                L.append(str(temp))
                N = N//2
            L.reverse()
            string = (''.join(L))
            if string != "1":
                large_string += (string + ', ')
            else:
                large_string += string

        return large_string
    
    def binaryGapRecursive(n):
        Gapqueue = [i for i in list(range(32)) if (n >> i) & 1]
        if len(Gapqueue) < 2:
            return 0
        returnOut = max(Gapqueue[i+1] - Gapqueue[i] for i in list(range(len(Gapqueue) - 1)))
        if returnOut == 1 :
            returnOut=0
        return(returnOut)


def run():
    userInput = int(input("Enter number: "))
    binary = BinaryNumber(userInput)

    print("The binary numbers are " , binary.generate_binary_numbers())
    print("The binary gap is ",BinaryNumber.binaryGapRecursive(userInput))
    print()
    if input("again? (y/n)").lower() == "y":
        print()
        print()
        run()
    else:
        pass

run()