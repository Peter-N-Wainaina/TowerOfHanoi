def hanoi(disks,src,dest,temp):
    if disks>0:
        hanoi(disks-1,src,temp,dest)
        print("move disk from " +src+" to "+temp)
        hanoi(disks-1,temp,dest,src)

#TODO:DD A CONSOLE
#TODO:Add a method to move disk on console

hanoi(3,"A","C","B")