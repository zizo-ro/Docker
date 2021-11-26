# importing module
from pandas import *
import random
import time


# reading CSV file
data = read_csv("jockes.csv")

# converting column data to list
ID= data['ID'].tolist()
joke = data['Joke'].tolist()

Logo = """
   '||'                 '||                     
    ||    ...     ....   ||  ..    ....   ....  
    ||  .|  '|. .|   ''  || .'   .|...|| ||. '  
    ||  ||   || ||       ||'|.   ||      . '|.. 
|| .|'   '|..|'  '|...' .||. ||.  '|...' |'..|' 
 '''                                            
                                                
 '''                                   
"""

print( Logo )

while True:
    time.sleep(5)
    r=random.randint(0,ID[-1])
    print( "ID : "+ str(ID[r])+"   |  "+joke[r] )