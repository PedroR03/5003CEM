from collections import defaultdict
import sys      

class Graph():
    def __init__(self, size):
        self.edges = defaultdict(list)  
        self.weights = {}                
        self.size = size    
        self.dist = []
        for i in range(size):   
            self.dist.append(sys.maxsize)
        self.previous = []
        for i in range(size):   
            self.previous.append(None)
        
    
    def add_edge(self, from_node, to_node, weight): 
        self.edges[from_node].append(to_node)   
        self.edges[to_node].append(from_node)   
        self.weights[(from_node, to_node)] = weight 
        self.weights[(to_node, from_node)] = weight 


    def find_Smallest_Node(self):    
        smallest = self.dist[self.getIndex(self.Q[0])]      
        result = self.getIndex(self.Q[0])        
        for i in range(len(self.dist)): 
            if self.dist[i] < smallest:
                node = self.unpoppedQ[i]        
                if node in self.Q:          
                    smallest = self.dist[i]      
                    result = self.getIndex(node)   
        return result
            

    def getIndex(self, neighbour):  
        for i in range(len(self.unpoppedQ)):
            if neighbour == self.unpoppedQ[i]:
                return i


    def getPopPosition(self, uNode): 
        for i in range(len(self.Q)):
            if self.Q[i] == uNode: 
                return i
        return 0


    def getUnvisitedNodes(self, uNode): 
        resultList = []
        allNeighbours = self.edges[uNode]   
        for neighbour in allNeighbours:
            if neighbour in self.Q: 
                resultList.append(neighbour)
        return resultList          


    #This function is going to return the path with less weight from A to B
    def dijsktra(self, start, end): 
        self.Q = []
        for key in self.edges:      #this for is to set the Q to all the edges
            self.Q.append(key)
        for i in range(len(self.Q)):    #set the starting edge to 0 distance 
            if self.Q[i] == start:
                self.dist[i] = 0
        
        self.unpoppedQ = self.Q[0:]     #unpoppedQ is going to be equal to Q   
        
        #this is a loop troguht all the vertices 
        while self.Q:   #while is still items in Q         
            u = self.find_Smallest_Node()     #Get the index of the lightest node                                    
            if self.dist[u] == sys.maxsize: #if the smallest node is maxsize, means it didn´t found any edge and the function breaks 
                break                                           
            if self.unpoppedQ[u] == end:    #If the unpoppedQ is the same as the last one, this means that it was found and the fucntion breaks
                break
            
            #This code is to find the smallest value closer; and will add the results to the list 
            uNode = self.unpoppedQ[u]
            self.Q.pop(self.getPopPosition(uNode))        #this removes the vertex from Q
            for v in self.getUnvisitedNodes(uNode):      #the for is to check all the neighbours that weren´t visited yet
                alt = self.dist[u] + self.weights[uNode, v]     #this is to show the distance between the neighbour
                
                realPos = self.getIndex(v)      #is to get the position of the neighbour
                if alt < self.dist[realPos]:    #if the alt is less than the real position of the neighbour, update with this path
                    self.dist[realPos] = alt
                    self.previous[realPos] = uNode
            
        shortest_path = []      #the smaller path is going to be stored
        shortest_path.insert(0, end)    #is going to add the value from the target to the list 
        u = self.getIndex(end)      #this gets the index                                                 
        while self.previous[u] != None:  #this while is used so when is no arrived yet to the starter value   
            shortest_path.insert(0, self.previous[u])       #is going to add the previous value                       
            u = self.getIndex(self.previous[u])             #U is set as the prevoius value index
        return str(shortest_path) + "\nThe weigth is " + str(self.dist[self.getIndex(end)])     #This rerturns the shortest path and is weight


graph = Graph(8) #use to create the graph


edges = [
    ('O', 'A', 2),
    ('O', 'B', 5),
    ('O', 'C', 4),
    ('A', 'B', 2),
    ('A', 'D', 7),
    ('A', 'F', 12),
    ('B', 'C', 1),
    ('B', 'D', 4),
    ('B', 'E', 3),
    ('C', 'E', 4),
    ('D', 'E', 1),
    ('D', 'T', 5),
    ('E', 'T', 7),
    ('F', 'T', 3),
]   
    

for edge in edges:  #the for is used to add the edges
    graph.add_edge(*edge)

print(graph.dijsktra('O', 'T')) 