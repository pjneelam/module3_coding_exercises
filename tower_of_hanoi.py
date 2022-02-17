# Creating a recursive function
# peg=rod
#count number of times the disks must be moved, create variable count or runcount, runcount+1, global runcount
runcount=0

def tower_of_hanoi(disks, peg1, peg2, peg3):
    global runcount
    runcount=runcount+1  
    if(disks == 1):
        print('Move disk 1 from rod {} to rod {}.'.format(peg1, peg3))  
        return  
    # function call itself  
    tower_of_hanoi(disks - 1, peg1, peg3, peg2)  
    print('Move disk {} from rod {} to rod {}.'.format(disks, peg1, peg3))  
    tower_of_hanoi(disks - 1, peg2, peg1, peg3)  
  
  
disks = int(input('Enter the number of disks: '))  
# We are referring source as A, auxiliary as B, and target as C  
tower_of_hanoi(disks, 'A', 'B', 'C')  # Calling the function  


print(runcount)
#number of moves: (number of disks*2)+1 (3 disks=3*2 - 1= 7;)
#Formula= 2 power n -1
#Source: https://www.javatpoint.com/tower-of-hanoi-puzzle-using-python
