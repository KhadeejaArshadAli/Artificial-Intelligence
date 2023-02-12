#(II)In a company ,worker efficiency is determined on the basis of the time required for a worker 
#to complete a particular job.If the time taken by the worker is between 2-3 hours then the worker 
#is said to be highly efficient. If the time required by the worker is between 3-4hours,then the worker 
#is ordered to improve speed. If the time taken is between 4-5 hours ,the worker is given training to 
#improve his speed ,and if the time taken by the worker is more than 5 hours ,then the worker haas 
#to leave the company, If the time taken by the worker is input through the keyboard,find the 
#efficiency of the worker
def CalculateEffifiency():
    hours=float(input ("Enter the number of hours taken to complete the task: "))
    if hours>=2 and hours<=3:
        print("You are highly efficient")
    if hours>3 and hours<=4:
        print("You need to improve your speed")
    if hours>4 and hours<=5:
        print("You will recieve training to improve your speed")
    if hours>5:
        print("You are fired effective immediately") 
CalculateEffifiency()
    