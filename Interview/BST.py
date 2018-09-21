import Queue

class BSTNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
    @staticmethod    
    def insert(node, val):
        if node == None:
            return BSTNode(val)        
        if val < node.val:
            node.left = BSTNode.insert(node.left, val)
        elif val > node.val:
            node.right = BSTNode.insert(node.right, val)
        return node
        
    
      
    @staticmethod
    def insert3(node, val):
        if node is None:
            return BSTNode(val)
        cur = node
        
        while True:            
            if val < cur.val:
                if cur.left is None:
                    cur.left = BSTNode(val)
                    break
                else:
                    cur = cur.left 
            elif val > cur.val:
                if cur.right is None:
                    cur.right = BSTNode(val)
                    break
                else:
                    cur = cur.right
            else:
                return node

        return node 
        
    @staticmethod    
    def preOrderTraverseRecursive(node):
        if node is not None:
            print(node.val)        
            BSTNode.preOrderTraverseRecursive(node.left)
            BSTNode.preOrderTraverseRecursive(node.right)   

    @staticmethod
    def preOrderTraverse(node):
        stack = list()
        if node is not None:
            stack.append(node)
        while(len(stack)>0):
            current = stack.pop()
            print(current.val)
            if current.right is not None:
                stack.append(current.right)
            if current.left is not None:
                stack.append(current.left)
                
    @staticmethod
    def inOrderTraverseRecursive(node):
        if node is not None:
            BSTNode.inOrderTraverseRecursive(node.left)
            print(node.val)
            BSTNode.inOrderTraverseRecursive(node.right)
    
    @staticmethod
    def inOrderTraverse(node):
        stack = list()
        p = node
        while(p is not None or len(stack)>0):
            while(p is not None):
                stack.append(p)
                p = p.left
            p = stack.pop()
            print(p.val)
            p = p.right
            
    @staticmethod
    def postOrderTraverseRecursive(node):
        if node is not None:
            BSTNode.postOrderTraverseRecursive(node.left)
            BSTNode.postOrderTraverseRecursive(node.right)
            print(node.val)
    
    @staticmethod     
    def postOrderTraverse(node):
        stack = list()
        p = node
        c = None
        while(p is not None or len(stack)>0):
            while(p is not None):
                stack.append(p)
                p = p.left
            p = stack[-1]  # peek
            if p.right is not None and c is not p.right:
                p = p.right                
            else:            
                p = stack.pop()
                print(p.val)
                c = p
                p = None
                
    @staticmethod        
    def hierarchicalTraverse(node):
        q = Queue.Queue()
        if node is not None:
            q.put(node)
        while not q.empty():
            p = q.get()
            print(p.val)
            if p.left is not None:
                q.put(p.left)
            if p.right is not None:
                q.put(p.right)
            
            
class BST(object): 
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        self.root = BSTNode.insert(self.root, val)
    
    def insert3(self, val):
        self.root = BSTNode.insert3(self.root, val)
        
    def preOrderTraverseRecursive(self):
        BSTNode.preOrderTraverseRecursive(self.root)
    
    def preOrderTraverse(self):
        BSTNode.preOrderTraverse(self.root)
        
    def inOrderTraverseRecursive(self):
        BSTNode.inOrderTraverseRecursive(self.root)
    
    def inOrderTraverse(self):
        BSTNode.inOrderTraverse(self.root)
        
    def postOrderTraverseRecursive(self):
        BSTNode.postOrderTraverseRecursive(self.root)
    
    def postOrderTraverse(self):
        BSTNode.postOrderTraverse(self.root)
        
    def hierarchicalTraverse(self):
        BSTNode.hierarchicalTraverse(self.root)

if __name__ == "__main__":
    tree = BST()
    dataArray = {10, 5, 20, 18, 8, 4, 15, 30, 19, 23, 27}
    # dataArray = {5,6,1,2,3,4,7,8,9,10}
    for v in dataArray:
        print(v)
        tree.insert(v)
    print('preOrderTraverseRecursive')
    tree.preOrderTraverseRecursive()
    print("preOrderTraverse NonRecursive")
    tree.preOrderTraverse()
    print("inOrderTraverseRecursive")
    tree.inOrderTraverseRecursive()
    print("inOrderTraverse NoneRecursive")
    tree.inOrderTraverse()
    print('postOrderTraverseRecursive')
    tree.postOrderTraverseRecursive()
    print('postOrderTraverse None Recursive')
    tree.postOrderTraverse()
    print('hierarchicalTraverse')
    tree.hierarchicalTraverse()
    
            
      
        
        