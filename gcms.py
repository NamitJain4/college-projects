from bin import Bin
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException
from node import Node

class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.BinsCapacity = AVLTree(self.comparator_bins_capacity)
        self.BinsId = AVLTree(self.comparator_bins_id)
        self.Objects = AVLTree(self.comparator_objects_id)
        
    def comparator_bins_capacity(self, a, b):
        if a.val.capacity == b.val.capacity:
            return a.val.bin_id < b.val.bin_id
        return a.val.capacity < b.val.capacity
        
    def comparator_bins_id(self, a, b):
        return (a.val.bin_id if str(type(a))=="<class 'node.Node'>" else a) < (b.val.bin_id if str(type(b))=="<class 'node.Node'>" else b)
        
    def comparator_objects_id(self, a, b):
        return (a.val.object_id if str(type(a))=="<class 'node.Node'>" else a) < (b.val.object_id if str(type(b))=="<class 'node.Node'>" else b)

    def add_bin(self, bin_id, capacity):
        p = Bin(bin_id, capacity)
        self.BinsCapacity.root = self.BinsCapacity.insert_node(Node(p), self.BinsCapacity.root)
        self.BinsId.root = self.BinsId.insert_node(Node(p), self.BinsId.root)

    def add_object(self, object_id, size, color):
        p = Object(object_id, size, color)
        t = -1
        if color == Color.BLUE:
            t = self.BinsCapacity.least_capacity_least_id(size, self.BinsCapacity.root)
        elif color == Color.YELLOW:
            t = self.BinsCapacity.least_capacity_greatest_id(size, self.BinsCapacity.root)
        elif color == Color.RED:
            t = self.BinsCapacity.greatest_capacity_least_id(size, self.BinsCapacity.root)
        elif color == Color.GREEN:
            t = self.BinsCapacity.greatest_capacity_greatest_id(size, self.BinsCapacity.root)
        
        if t==-1:
            #print(self.inorder_traversal_bins(self.BinsCapacity.root))
            raise NoBinFoundException
        else:
            t = t.val
            self.Objects.root = self.Objects.insert_node(Node(p), self.Objects.root)
            p.bin_id = t.bin_id
            self.BinsCapacity.root = self.BinsCapacity.delete_node(Node(t), self.BinsCapacity.root)
            t.add_object(p)
            self.BinsCapacity.root = self.BinsCapacity.insert_node(Node(t), self.BinsCapacity.root)
            
    def inorder_traversal(self, root):
        if not root:return []
        return self.inorder_traversal(root.left) + [root.val.object_id] + self.inorder_traversal(root.right)
        
    def inorder_traversal_bins(self, root):
        if not root:return []
        return self.inorder_traversal_bins(root.left) + [(root.val.capacity, root.val.bin_id)] + self.inorder_traversal_bins(root.right)

    def delete_object(self, object_id):
        # Implement logic to remove an object from its bin
        try:
            obj = self.Objects.search_node(object_id, self.Objects.root)
        except:
            return None
        binn = self.BinsId.search_node(obj.val.bin_id, self.BinsId.root).val
        
        self.Objects.root = self.Objects.delete_node(obj, self.Objects.root)
        self.BinsCapacity.root = self.BinsCapacity.delete_node(Node(binn), self.BinsCapacity.root)
        binn.remove_object(object_id)
        self.BinsCapacity.root = self.BinsCapacity.insert_node(Node(binn), self.BinsCapacity.root)
    
    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        t = self.BinsId.search_node(bin_id, self.BinsId.root)
        return t.val.capacity, self.inorder_traversal(t.val.objectsInside.root)

    def object_info(self, object_id):
        # returns the bin_id in which the object is stored
        try:
            t = self.Objects.search_node(object_id, self.Objects.root)
        except:
            return None
        return t.val.bin_id
    
    