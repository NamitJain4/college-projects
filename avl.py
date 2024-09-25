def comp_1(node_1, node_2):
    return (node_1.val if str(type(node_1))=="<class 'node.Node'>" else node_1) < (node_2.val if str(type(node_2))=="<class 'node.Node'>" else node_2)

class AVLTree:
    def __init__(self, compare_function=comp_1):
        self.root = None
        self.size = 0
        self.comparator = compare_function

    def height(self, node):
        if not node:
            return 0
        return node.height

    def update_node_height(self, node):
        if not node:
            return 0
        node.height = 1+max(self.height(node.left), self.height(node.right))

    def height_diff(self, node):
        if not node:
            return 0
        return self.height(node.right) - self.height(node.left)
        
    def rotate_right(self, X):
        Y = X.left
        if Y==None:return X
        p = Y.right

        Y.right = X
        X.left = p

        self.update_node_height(X)
        self.update_node_height(Y)

        return Y

    def rotate_left(self, X):
        Y = X.right
        if Y==None:return X
        p = Y.left

        Y.left = X
        X.right = p

        self.update_node_height(X)
        self.update_node_height(Y)

        return Y

    def insert_node(self, node, root):
        if not root:
            self.size+=1
            return node
                
        if self.comparator(root, node):
            root.right = self.insert_node(node, root.right)
        else:
            root.left = self.insert_node(node, root.left)

        self.update_node_height(root)

        balance = self.height_diff(root)

        if balance < -1:
            if self.comparator(node, root.left):
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        if balance > 1:
            if self.comparator(root.right, node):
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def inorder_successor(self, node):
        if node.right:
            t = node.right
            while t.left:
                t = t.left
            return t
        
        curr = self.root
        succ = None
        while curr:
            if self.comparator(node, curr):
                succ = curr
                curr = curr.left
            elif self.comparator(curr, node):
                curr = curr.right
            else:
                break
        return succ

    def delete_node(self, node, root):
        if not root:
            return None
        
        if self.comparator(node, root):
            root.left = self.delete_node(node, root.left)
        elif self.comparator(root, node):
            root.right = self.delete_node(node, root.right)
        else:
            self.size -= 1
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            t = self.inorder_successor(root)
            root.val = t.val

            root.right = self.delete_node(t, root.right)

        self.update_node_height(root)

        balance = self.height_diff(root)

        if balance < -1:
            if self.comparator(node, root.left):
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        if balance > 1:
            if self.comparator(root.right, node):
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root
        
    def search_node(self, node_id, root):
        if self.comparator(node_id, root):
            return self.search_node(node_id, root.left)
        if self.comparator(root, node_id):
            return self.search_node(node_id, root.right)
        return root
            
    def least_capacity_least_id(self, value, root):
        curr = root
        ans = -1
        while curr!=None:
            if curr.val.capacity < value:
                curr = curr.right
            else:
                ans = curr
                curr = curr.left
        return ans
        
    def inorder_predecessor(self, t):
        if t.left:
            t = t.left
            while t.right:
                t = t.right
            return t
    
        curr = self.root
        pred = None
        while curr:
            if self.comparator(curr, t):
                pred = curr
                curr = curr.right
            elif self.comparator(t, curr):
                curr = curr.left
            else:
                break
        return pred
        
    def least_capacity_greatest_id(self, value, root):
        t = self.least_capacity_least_id(value, root)
        if t==-1:
            return -1
        p = self.least_capacity_least_id(t.val.capacity+1, root)
        if p!=-1:
            q = self.inorder_predecessor(p)
            return q
        else:
            r = self.root
            while r.right:
                r = r.right
            return r
            
    def greatest_capacity_greatest_id(self, value, root):
        while root.right:
            root = root.right
        if root.val.capacity < value:
            return -1
        return root
        
    def greatest_capacity_least_id(self, value, root):
        cap = self.greatest_capacity_greatest_id(value, root)
        if cap==-1:
            return -1
        cap = cap.val.capacity
        curr = root
        ans = -1
        while curr:
            if curr.val.capacity < cap:
                curr = curr.right
            else:
                ans = curr
                curr = curr.left
        return ans
        
