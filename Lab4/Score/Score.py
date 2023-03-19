import time
from abc import abstractmethod
class Environment(object):
 @abstractmethod
 def __init__(self,n):
     self.n = n
 def executeStep(self,n=1):
     raise NotImplementedError('action must be defined!')
 def executeAll(self):
     raise NotImplementedError('action must be defined!')

 def delay(self,n=100):
     self.delay = n 



#Room class
class Room:
 def __init__(self,location,status="dirty"):
     self.location = location
     self.status = status

#Abstract agent
from abc import abstractmethod
class Agent(object):

 @abstractmethod
 def __init__(self): 
    pass

 @abstractmethod
 def sense(self,environment):
     pass

 @abstractmethod
 def act(self):
     pass
 
#Vaccum cleaner Agent
class VaccumAgent(Agent):
  def __init__(self):
      pass

  def sense(self,env):
      self.environment = env
  def act(self):
      if self.environment.currentRoom.status == 'dirty':
          return 'clean' 
      if self.environment.currentRoom.location == 'A':
          return 'right'
      else:
         return 'left' 
      
class TwoRoomVaccumCleanerEnvironment(Environment):
 def __init__(self,agent):
     
#Constructor
    self.r1 = Room('A','dirty')
    self.r2 = Room('B','dirty')
    self.agent = agent
    self.currentRoom = self.r1
    self.delay = 1000 
    self.step = 1 
    self.action = ""
    self.score=-10

 def executeStep(self,n=1):
    for _ in range(0,n):

        self.displayPerception()
        self.agent.sense(self)
        res = self.agent.act()
        self.action = res
        if res == 'clean':
            self.currentRoom.status ='clean' 
            self.score+=25
        elif res == 'right': 
            self.currentRoom = self.r2 
            self.score-=1
        else:
            self.currentRoom = self.r1
            self.score-=1
        self.displayAction()
        self.step += 1
        self.displayScore()

 def executeAll(self):
     raise NotImplementedError('action must be defined!')
 def displayPerception(self):
     print("Perception at step %d is [%s,%s]" %(self.step,self.currentRoom.status,self.currentRoom.location))
 def displayAction(self):
     print("------- Action taken at step %d is [%s]" %(self.step,self.action))

 def delay(self,n=100):
     self.delay = n 
 def displayScore(self):
    time.sleep(1)
    print("the score: ",self.score)
#Test program
if __name__ == '__main__': 
    vcagent = VaccumAgent() 
    env = TwoRoomVaccumCleanerEnvironment(vcagent)
    env.executeStep(10) 