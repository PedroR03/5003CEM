
class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self): #function to print the list of days 
        printval = self.headval
        while printval is not None: #loop that goes through all days
            print(printval.dataval) #prints the current day 
            printval = printval.nextval #this is to get the next day
            
    def AtBeginning(self,newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def AtEnd(self, newdata): 
        NewNode = Node(newdata) #newnode is going to be the last day
        if self.headval is None: #this if is for a case where is no values in
            self.headval = NewNode #the last day will be set as the value
            return
        last = self.headval
        while(last.nextval): #this while is to search through the days for the las day
            last = last.nextval
        last.nextval = NewNode #to sset the nextval to be the value  

    def Insert(self,val_before,newdata): #this function is used to add a new day in the middle of the week
        NewNode = Node(newdata) #is to generate a new day
        if val_before is None: #if the value is no generated print the error message
            print("No node to insert after")
            return
        else:
            next = self.headval
            while(next): #this while is used to loop through all days, and finds the val_before of that day
                if next.dataval == val_before: #when the val_before is found
                    NewNode.nextval = next.nextval #newnode equals to val_before
                    next.nextval = NewNode #nextval is euqal to newnode
                    break
                next = next.nextval            
        

list = SLinkedList() #create object
list.headval = Node("Mon") #first val 

e2 = Node("Tue") 
e3 = Node("Thur")
e4 = Node("Fri")
e5 = Node("Sat")
list.headval.nextval = e2 #connects betwen the first and second
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5
list.AtEnd("Sun") #this is the last so is going to end here

list.Insert("Tue", "Weds") #insertion of 2 days


list.listprint() #is used to print the list