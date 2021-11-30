# importing module
from pandas import *
import random
import time


# reading CSV file
data = read_csv("trivia.csv")

# converting column data to list
ID= data['ID'].tolist()
Question = data['Question'].tolist()
Answer = data['Answer'].tolist()


Logo = """
               ----Trivia----
      __...--~~~~~-._   _.-~~~~~--...__
    //               `V'               \\ 
   //                 |                 \\ 
  //__...--~~~~~~-._  |  _.-~~~~~~--...__\\ 
 //__.....----~~~~._\ | /_.~~~~----.....__\\
====================\\|//====================                                 
"""

print( Logo )

while True:
    time.sleep(5)
    r=random.randint(0,ID[-1])
    #print( "ID : "+ str(ID[r]))
    print( "ID : "+ str(ID[r])+" |  "+Question[r] + " | Answer : " + Answer[r] )