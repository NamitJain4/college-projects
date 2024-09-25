from avl import AVLTree
from node import Node


class Bin:
    def __init__(self, bin_id, capacity):
        self.bin_id = bin_id
        self.capacity = capacity
        self.objectsInside = AVLTree(self.comparator)
        
    def comparator(self, a, b):
        return (a.val.object_id if str(type(a))=="<class 'node.Node'>" else a) < (b.val.object_id if str(type(b))=="<class 'node.Node'>" else b)

    def add_object(self, object):
        # Implement logic to add an object to this bin
        self.capacity-=object.size
        if self.objectsInside.root == None:
            self.objectsInside.root = Node(object)
        else:
            self.objectsInside.root = self.objectsInside.insert_node(Node(object), self.objectsInside.root)

    def remove_object(self, obj_id):
        # Implement logic to remove an object by ID
        obj = self.objectsInside.search_node(obj_id, self.objectsInside.root)
        self.capacity+=obj.val.size
        self.objectsInside.root = self.objectsInside.delete_node(obj, self.objectsInside.root)
        obj.bin_id = None