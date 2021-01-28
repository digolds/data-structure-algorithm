import singly_linked_list
import queue

class Vertex:
    def __init__(self, value):
        self.value = value
        self.associated_edges = singly_linked_list.SinglyLinkedList()

class Graph:
    def __init__(self):
        self.vertexes = {}
    
    def add_vertex(self, node_no, value):
        if node_no not in self.vertexes:
            node = Vertex(value)
            self.vertexes[node_no] = node

    def remove_vertex(self, node_no):
        if node_no in self.vertexes:
            associated_edges = self.vertexes[node_no].associated_edges
            removed_edge = associated_edges.remove_from_head()
            while removed_edge is not None:
                self.vertexes[removed_edge.key].associated_edges.remove(node_no)
                removed_edge = associated_edges.remove_from_head()

    def add_edge(self, node_no_1, node_no_2, cost):
        if node_no_1 in self.vertexes:
            self.vertexes[node_no_1].associated_edges.add_to_tail(node_no_2, cost)
    
    def remove_edge(self, node_no_1, node_no_2):
        if node_no_1 in self.vertexes and node_no_2 in self.vertexes:
            self.vertexes[node_no_1].associated_edges.remove(node_no_2)
            self.vertexes[node_no_2].associated_edges.remove(node_no_1)
    
    def neighbors(self, node_no):
        if node_no in self.vertexes:
            return self.vertexes[node_no].associated_edges
    
    def set_vertex_value(self, node_no, value):
        if node_no in self.vertexes:
            self.vertexes[node_no].value = value

    def get_vertex_value(self, node_no):
        if node_no in self.vertexes:
            return self.vertexes[node_no].value
        return None
    
    def adjacent(self, node_no_1, node_no_2):
        if node_no_1 in self.vertexes and node_no_2 in self.vertexes:
            return self.vertexes[node_no_1].associated_edges.find(node_no_2) is not None
        return False
    
    def dfs(self, start_node_no, call_back):
        if start_node_no in self.vertexes:
            visited = {}
            stack = []
            stack.append(start_node_no)
            while len(stack) != 0:
                top = stack[0]
                if visited[top] is None:
                    call_back(self.vertexes[top].value)
                    visited[top] = True
                # get unvisited node
                associated_edges = self.vertexes[top].associated_edges
                current_node = associated_edges.head
                while current_node:
                    if visited[current_node.key] is None:
                        break
                    current_node = current_node.next
                if current_node is not None:
                    stack = [current_node.key] + stack
                else:
                    stack = stack[1:]

    def bfs(self, start_node_no, call_back):
        if start_node_no in self.vertexes:
            visited = {}
            dequeue = queue.DeQueue()
            dequeue.push_back(start_node_no)
            while not dequeue.empty():
                front_node = dequeue.pop_front()
                visited[front_node] = True
                call_back(self.vertexes[front_node].value)
                associated_edges = self.vertexes[front_node].associated_edges
                current_node = associated_edges.head
                while current_node:
                    if current_node.key not in visited:
                        dequeue.push_back(current_node.key)
                    current_node = current_node.next