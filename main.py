import os
from random import randint
import threading

features = [
    "Fixed bugs",
    "Removed lag",
    "Deleted rand data",
    "Added more files",
    "Added more test cases",
    "Remove pub file"
]

for i in range(1, 365):
    for j in range(0 , randint(1,10)):
        d = str(i) + ' days ago'
        
        with open('data.txt', 'a') as file:
            file.write(d)
        os.system('git add .')
        os.system('git commit --date="'+d+'" -m "'+features[randint(0, len(features)-1)]+'"')
        

