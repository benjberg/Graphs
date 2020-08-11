
# Note: This Queue class is sub-optimal. Why?
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #make a que
        q = Queue()
        #put starting node in que
        q.enqueue(starting_vertex)
        #make a set for the visited nodes
        visited = set()
        # if our stack's not empty
        while q.size() > 0:
            # get the next node off que
            v = q.dequeue()
            # check if it has been visited
            if v not in visited:
                print(v)
                visited.add(v)
                for i in self.get_neighbors(v):
                    q.enqueue(i)
         
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #make a stack
        stack = Stack()
        #make a set for the visited nodes
        visited = set()

        #put our starting node on top of the stack
        stack.push(starting_vertex)

        #if our stack's not empty
        while stack.size() > 0:
            #get the next node off the top of our stack
            current_node = stack.pop()

            # check if it has been visited
            if current_node not in visited:
                #if not, mark as visited
                visited.add(current_node)
                print(current_node)
                # get its neighbors
                edges = self.get_neighbors(current_node)
                #add all of it's neighbors to the back of the stack
                for edge in edges:
                    stack.push(edge)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        #if visited is None (defaults)
        if visited is None:
            #set visited to empty set
            visited = set()
        #add starting vert to vistited 
        visited.add(starting_vertex)
        print(starting_vertex)
        #check the children of the vert
        for child_vert in self.vertices[starting_vertex]:
            #if theyre not visited
            if child_vert not in visited:
                #call iteslf taking in the child vert and visitd
                self.dft_recursive(child_vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        # Put the starting point in that
        # Enque a list to use as our path
        q.enqueue([starting_vertex])
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the que
        while q.size() > 0:
            #deque the first item
            path = q.dequeue()
            vertex = path[-1]
            #If not visited
            if vertex not in visited:
                if vertex == destination_vertex:
                    # return the path
                    return path
                visited.add(vertex)
                #For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                # Copy path to avoid pass by reference bug
                    new_path = list(path) # Make a copy of path rather than reference
                    new_path.append(next_vert)
                    q.enqueue(new_path)
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        # Put the starting point in that
        # Enstack a list to use as our path
        stack.push([starting_vertex])
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the stack
        while stack.size() > 0:
            #Pop the first item
            path = stack.pop()
            vertex = path[-1]
            #If not visited
            if vertex not in visited:
                if vertex == destination_vertex:
                    #return the path
                    return path
                visited.add(vertex)
                #For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                # Copy path to avoid pass by reference bug
                    new_path = list(path) # Make a copy of path rather than reference
                    new_path.append(next_vert)
                    stack.push(new_path)
        return None
    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        
        visited.add(starting_vertex)

         
        path = path + [starting_vertex]
        print(path, ' path after append')

        #break
        if starting_vertex == destination_vertex:
            return path
        #loop through neighbors of starting vert
        for neighbor in self.get_neighbors(starting_vertex):
            #if the neighbor is not visited
            if neighbor not in visited:
                #create a newpath calling dfs_recursive 
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                #if new path exist return it
                if new_path:
                    return new_path
        return None


