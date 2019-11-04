"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        # pass  # TODO
        self.vertices[vertex]=set()


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if self.vertices.get(v1) == None:
            raise IndexError(f'{v1} not in graph')
        if self.vertices.get(v2) == None:
            raise IndexError(f'{v2} not in graph')
        self.vertices[v1].add(v2)

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        
        temp = Queue()
        temp.enqueue(starting_vertex)
        done=[starting_vertex]
        print('bft')
        while temp.size()>0:
            current = temp.dequeue()
            done.append(current)
            for node in self.vertices[current]:
                if not node in done:
                    temp.enqueue(node)
                    done.append(node)
            print(current)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        temp = Stack()
        temp.push(starting_vertex)
        done=[starting_vertex]
        print('dft')
        while temp.size() >0:
            current = temp.pop()
            for node in self.vertices[current]:
                if not node in done:
                    temp.push(node)
                    done.append(node)
            print(current)

    def dft_recursive(self, starting_vertex, done = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # pass  # TODO
        if not starting_vertex:
            return

        if not done:
            done=[starting_vertex]
            print('Recurse DFT')
        else:
            done.append(starting_vertex)

        print(starting_vertex)
        for node in self.vertices.get(starting_vertex):
            if not node in done:
                self.dft_recursive(node,done)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # pass  # TODO
        temp = Queue()
        temp.enqueue(starting_vertex)
        done=[]
        path={
            starting_vertex:None
        }
        print(f'pathing from {starting_vertex} to {destination_vertex}')
        while temp.size>0:
            current = temp.dequeue()
            if current==destination_vertex:
                ret = f''
                while path.get(current):
                    ret = f'{current} {ret}'
                    current=path.get(current)
                return ret
            else:
                for node in self.vertices.get(current):
                    temp.push(node)
                    if not path.get(node,None):
                        path[node]=current


        print('Not a Vertex')

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
