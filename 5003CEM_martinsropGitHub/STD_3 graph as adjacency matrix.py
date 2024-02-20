class Graph(object):
    
    def __init__(self, size):
        self.adjMatrix = []
        self.vertexCount = size
        for i in range(self.vertexCount):
            self.adjMatrix.append([0 for i in range(self.vertexCount)])
        self.size = size

    #(1)adding the vertex;
    def add_vertex(self):
        for i in range(self.vertexCount): #loop to see the amount of vertices
            self.adjMatrix[i].append(0) #append 0 for all vertex
        self.vertexCount = self.vertexCount + 1 #number of vertices will be increased
        self.adjMatrix.append([0 for i in range(self.vertexCount)]) #the new vertex will be fill with zeros
            
    #(2) adding an edge;
    def add_edge(self, v1, v2):
        if v1 == v2: #can be add an edge with equal vertice
            print("The vertices are the same")
            return 
        elif v1 not in range(1, self.vertexCount): # can be used a new vertex to generate an edge
            print("Vertex ", v1, " doesn´t exist.")
        elif v2 not in range(1, self.vertexCount): # can be used a new vertex to generate an edge
            print("Vertex ", v2, " doesn´t exist.")
        elif self.adjMatrix[v1][v2] == 0 and self.adjMatrix[v2][v1] == 0: #is to certifie that is possible to create the edge
            self.adjMatrix[v1][v2] = 1 #replacement the 0 with 1 so it can be created the edge
            self.adjMatrix[v2][v1] = 1 ##replacement the 0 with 1 so it can be created the edge
        else:
            print("The edge already exists")
    
    #(3) removing an edge; 
    def remove_edge(self, v1, v2):
        if v1 == v2: #is not possible to remove a edge that doesn´t exist
            print("The vertices are the same")
            return 
        elif v1 not in range(1, self.vertexCount): #is not possible to remove a edge that doesn´t exist
            print("Vertex ", v1, " doesn´t exist.")
        elif v2 not in range(1, self.vertexCount): #is not possible to remove a edge that doesn´t exist
            print("Vertex ", v2, " doesn´t exist.")
        elif self.adjMatrix[v1][v2] == 1 and self.adjMatrix[v2][v1] == 1: #to make sure the edge exists, so can be created
            self.adjMatrix[v1][v2] = 0 #replacement the 1 with 0 so it can be removed the edge
            self.adjMatrix[v2][v1] = 0 #replacement the 1 with 0 so it can be removed the edge
        else:
            print("The are allready removed")
    
     #(4) printing the matrix
    def print_matrix(self): 
        print(6 * ' ', end='') #print the first spaces, so can be strucuted
        for i in range(self.vertexCount): #loop trought the vertices 
            print(i, ' ', end='') #prints the lines
        print() #print a new line

        print(6 * ' ', end='') #print the spaces, so can be structure
        for i in range(self.vertexCount): #loop trought the vertices
            print("---", end='') #prints "---" for each number 
        print() #print a new line

        for i in range(self.vertexCount): #last loop going trough the vertices
            print(i, ' |   ', end='') #prints the "|" to each line
            for j in range(self.vertexCount): #this loop is to print the other part after the "|" prints
                print(self.adjMatrix[i][j], ' ', end='') #is to print the vertices
            print() #print a new line

        print() #print a new line
    #matrix should appear here


#remember list indexing - this is 1 out, unless we start the matrix at 0 (not a +ve integer)     
def main():
    g = Graph(4)
    g.add_vertex()   
    g.add_edge(1,2)
    g.print_matrix()
    g.remove_edge(1,2)
    g.print_matrix()



            
if __name__ == '__main__':
   main()