import search
import random
import util
import operator
from random import shuffle


# Module Classes

class jumpingFrogs:
    def __init__(self):
        self.pond=['g','g','g',0,'b','b','b']
        #shuffle(self.pond)

    def isGoalState(self,state):
        if state==['b','b','b',0,'g','g','g']:
            return True
        else:
            return False

    def getStartState(self):
        return self.pond
    
    def getSuccessors(self,state):
        pond=state
        successors=[]
        for i in range(2,5):
            if pond[i]==0:
                pond_copy=pond[:]
                pond_copy[i]=pond_copy[i-1]#1 places jump
                pond_copy[i-1]=0
                list_p=[]
                list_p.append(pond_copy)
                list_p.append("left1")#blank space moves left by 1
                list_p.append(1)
                successors.append(list_p)
                pond_copy=pond[:]
                pond_copy[i]=pond_copy[i-2]# places jump
                pond_copy[i-2]=0
                list_p=[]
                list_p.append(pond_copy)
                list_p.append("left2")
                list_p.append(2)
                successors.append(list_p)
                pond_copy=pond[:]
                pond_copy[i]=pond_copy[i+2]#2 places jump
                pond_copy[i+2]=0
                list_p=[]
                list_p.append(pond_copy)
                list_p.append("right2")
                list_p.append(2)
                successors.append(list_p)
                pond_copy=pond[:]
                pond_copy[i]=pond_copy[i+1]#1 places jump
                pond_copy[i+1]=0
                list_p=[]
                list_p.append(pond_copy)
                list_p.append("right1")
                list_p.append(1)
                successors.append(list_p)
        if pond[0]==0:
            pond_copy=pond[:]
            i=0
            pond_copy[i]=pond_copy[i+2]#2 places jump
            pond_copy[i+2]=0
            list_p=[]
            list_p.append(pond_copy)
            list_p.append("right2")
            list_p.append(2)
            successors.append(list_p)
            pond_copy=pond[:]
            pond_copy[i]=pond_copy[i+1]#1 places jump
            pond_copy[i+1]=0
            list_p=[]
            list_p.append(pond_copy)
            list_p.append("right1")
            list_p.append(1)
            successors.append(list_p)
        elif pond[1]==0:
            i=1
            pond_copy=pond[:]   
            pond_copy[i]=pond_copy[i+2]#2 places jump
            pond_copy[i+2]=0
            list_p=[]
            list_p.append(pond_copy)
            list_p.append("right2")
            list_p.append(2)
            successors.append(list_p)
            pond_copy=pond[:]
            pond_copy[i]=pond_copy[i+1]#1 places jump
            pond_copy[i+1]=0
            list_p=[]
            list_p.append(pond_copy)
            list_p.append("right1")
            list_p.append(1)
            successors.append(list_p)
            pond_copy=pond[:]
            pond_copy[i]=pond_copy[i-1]#1 places jump
            pond_copy[i-1]=0
            list_p=[]
            list_p.append(pond_copy)
            list_p.append("left1")
            list_p.append(1)
            successors.append(list_p)
          
        elif pond[5]==0:
            i=5
            pond_copy=pond[:]   
            pond_copy[i]=pond_copy[i-2]#2 places jump
            pond_copy[i-2]=0
            list_p=[]
            list_p.append(pond_copy)
            list_p.append("left2")
            list_p.append(2)
            successors.append(list_p)
            pond_copy=pond[:]
            pond_copy[i]=pond_copy[i+1]#1 places jump
            pond_copy[i+1]=0
            list_p=[]
            list_p.append(pond_copy)
            list_p.append("right1")
            list_p.append(1)
            successors.append(list_p)
            pond_copy=pond[:]
            pond_copy[i]=pond_copy[i-1]#1 places jump
            pond_copy[i-1]=0
            list_p=[]
            list_p.append(pond_copy)
            list_p.append("left1")
            list_p.append(1)
            successors.append(list_p)
        elif pond[6]==0:
            i=6
            pond_copy=pond[:]   
            pond_copy[i]=pond_copy[i-2]#2 places jump
            pond_copy[i-2]=0
            list_p=[]
            list_p.append(pond_copy)
            list_p.append("left2")
            list_p.append(2)
            successors.append(list_p)
            pond_copy=pond[:]
            pond_copy[i]=pond_copy[i-1]#1 places jump
            pond_copy[i-1]=0
            list_p=[]
            list_p.append(pond_copy)
            list_p.append("left1")
            list_p.append(1)
            successors.append(list_p)
            
        return successors
            

            
    def getCostOfActions(self, actions):
        cost=0
        for i in actions:
            if i=="left1" or i== "right1":
                cost+=1
            elif i=="left2" or i== "right2":
                cost+=2
        return cost

    def getHeuristic(self,state):#misplaced frogs
        h=0
        #print(state)
        pond=state
        for i in range(3):
            if pond[i]!='b':
                h+=1
        for i in range(4,len(pond)):
            if pond[i]!='g':
                h+=1
        return h

problem = jumpingFrogs()
path = search.aStarSearch(problem)
print(('Search found a path of %d moves ' % (len(path)-1)))
