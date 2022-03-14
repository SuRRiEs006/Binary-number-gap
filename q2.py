from ast import Return
import queue
outputArray = []

def generatePrintBinary(n):
 
    # Create an empty queue
    from queue import Queue
    q = Queue()
 
    # Enqueue the first binary number
    q.put("1")
 
    # 0 as left child and 1 as right child and so on
    while(n > 0):
        n -= 1
        # Print the front of queue
        s1 = q.get()
        outputArray.append(s1)

 
        s2 = s1  # Store s1 before changing it
 
        # Append "0" to s1 and enqueue it
        q.put(s1+"0")
 
        # Append "1" to s2 and enqueue it. Note that s2
        # contains the previous front
        q.put(s2+"1")



n = int(input("Enter your value for n"))
generatePrintBinary(n)
switchArray = []
for i in range((len(outputArray)-1),-1,-1):
    print(i)
    switchArray.append(outputArray[i])
print(switchArray)
class Solution:
   def binaryGap(self, n):
      B = bin(n).replace('0b','')
      K = str(B)
      K = list(K)
      Max = 0
      C = 0
      S =0
      Flag =False
      for i in range(len(K)):
         if K[i] == '1' and C == 0 and Flag == False:
            C=i
            Flag = True
         elif K[i] == '1' and Flag:
            S=i
            if Max<abs(S-C):
               Max = abs(S-C)
               C=S
      return Max
ob = Solution()

M = format(n, "b")

print("The number", n, "(binary representation", M, ", has a gap of ", ob.binaryGap(n))