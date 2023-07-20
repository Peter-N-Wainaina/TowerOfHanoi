from constants import *

#TODO: Probably move each class to its own file 
#TODO: Add getters and setters? 
class Tower:

    def __init__(self,numDisks):
        peg_src = Peg(PEG_NAME_SOURCE,numDisks)
        peg_dest =Peg(PEG_NAME_DESTINATION)
        peg_temp =Peg(PEG_NAME_TEMPORARY)
        self.pegs=[peg_src,peg_temp,peg_dest] #TODO:Move to a dictionary{NAME:Peg}

    def solve_tower(self):
        src =self.pegs[0]
        temp=self.pegs[1] 
        dest=self.pegs[2]
        self.hanoi(len(src.disks),src,dest,temp)
      

    def hanoi(self,disks,src,dest,temp):
        if disks == 1:
            src.move_disk(dest)  # Move the top disk from src to dest
        else:
            self.hanoi(disks - 1, src, temp, dest)  # Move the top (disks-1) disks from src to temp
            src.move_disk(dest)  # Move the bottom disk from src to dest
            self.hanoi(disks - 1, temp, dest, src)  # Move the (disks-1) disks from temp to dest


    def print_tower(self):
        print("\tTower of Hanoi")
        for peg in self.pegs:
            peg.print_peg()
    

class Peg:

    def __init__(self,name,numDisks=0):
        assert(numDisks>=0)
        self.name=name
        self.disks=[]
        if numDisks!=0:
            self.disks=self.create_disks(numDisks)

    def create_disks(self,numDisks):
        temp_disks=[]
        for size in range(1,numDisks+1):
            temp_disks.append(Disk(size))
        return temp_disks

    def move_disk(self,other_peg):
        assert(len(self.disks) > 0)
        disk=self.disks.pop(0)
        other_peg.place_disk(disk)

    def place_disk(self,disk):
        if len(self.disks)>0:
           assert(disk.size<self.disks[0].size)
        self.disks.insert(0,disk)

    def print_peg(self):
        print("Peg name: "+self.name )
        for disk in self.disks:
            disk.print_disk()


class Disk:
    def __init__(self,size):
        assert size >0
        self.size=size

    def print_disk(self):
        print("\tDisk "+str(self.size))