class BinarySearchTree:

    def __init__(self):
        self.size=0
        self.root=None

    class BSTNode:
        def __init__(self,key,value):
            self.key=key
            self.value=value
            self.left=None
            self.right=None
            self.parent=None
    
    def getRoot(self):
        return self.root

    def BSTsize(self):
        return self.size
    
    def add(self,key,value):
        node=self.BSTNode(key,value)
        root=self.root
        node_pointer=None
        while root != None:
            node_pointer=root
            if node.key < root.key:
                root=root.left
            else:
                root=root.right
        node.parent=node_pointer
        if node_pointer==None:
            self.root=node
        elif node.key < node_pointer.key:
            node_pointer.left=node
        else:
            node_pointer.right=node
        self.size+=1
    
    def _search(self,root,key):
        node_pointer=root
        if node_pointer==None:
            return False
        if node_pointer.key==key:
            return node_pointer.value
        elif key< node_pointer.key:
            return self._search(node_pointer.left,key)
        elif key>node_pointer.key:
            return self._search(node_pointer.right,key)
    
    def search(self,key):
        return self._search(self.root, key)
    
    def smallest(self):
        node_pointer=self.root
        while node_pointer.left != None:
            node_pointer=node_pointer.left
        return (node_pointer.key, node_pointer.value)

    def largest(self):
        node_pointer=self.root
        while node_pointer.right!=None:
            node_pointer=node_pointer.right
        return (node_pointer.key, node_pointer.value)
    
    def remove(self,key):
        return self.deleteNode(self.root,key)

    def deleteNode(self,root,key):
        # if the tree is empty
        if root is None:
            return root
        #if the key to be deleted is smaller than the root's key
        if key<root.key:
            root.left=self.deleteNode(root.left,key)
        #if the key to be deleted is larger than the root's key
        elif key>root.key:
            root.right=self.deleteNode(root.right,key)
        #if the key to be deleted is the root's key
        else:
            #If the root to be deleted has one or no child
            if root.left is None:
                temp=root.right
                root=None
                self.size-=1
                return temp
            elif root.right is None:
                temp=root.left
                root=None
                self.size-=1
                return temp
            #If the root to be deleted has two child
            temp=self.maxValueNode(root.left)
            root.key=temp.key
            root.left=self.deleteNode(root.left,temp.key)
        return root

    def inorder_walk(self):
        node=[]
        self.inorder(self.root,node)
        return node

    def inorder(self,root,node):
        if root:
            self.inorder(root.left,node)
            node.append(root.key)
            self.inorder(root.right,node)
    
    def preorder_walk(self):
        node=[]
        self.preorder(self.root,node)
        return node
    
    def preorder(self,root,node):
        if root:
            node.append(root.key)
            self.preorder(root.left,node)
            self.preorder(root.right,node)
    
    def postorder_walk(self):
        node=[]
        self.postorder(self.root,node)
        return node

    def postorder(self,root,node):
        if root:
            self.postorder(root.left,node)
            self.postorder(root.right,node)
            node.append(root.key)
    
    def maxValueNode(self,node): 
        current=node
        while current.left !=None:
            current=current.left
        return current

if __name__=="__main__":
    bst=BinarySearchTree()
    print("Size of BST", bst.BSTsize())
    bst.add(10, "Value for 10")
    bst.add(52, "Value for 52")
    bst.add(5, "Value for 5")
    bst.add(8, "Value for 8")
    bst.add(1, "Value for 1")
    bst.add(40, "Value for 40")
    bst.add(30, "Value for 30")
    bst.add(45, "Value for 45")
    print("Size After Adding Nodes")
    print("Size of BST",bst.BSTsize())
    print("Searching")
    print(bst.search(40))
    print(bst.smallest())
    print(bst.largest())
    print(bst.inorder_walk())
    print(bst.preorder_walk())
    print(bst.postorder_walk())
    print(bst.search(1))
    print("Size of BST",bst.BSTsize())
    bst.remove(1)
    print(bst.inorder_walk())
    print("Size of BST",bst.BSTsize())
    bst.remove(52)
    print(bst.inorder_walk())
    print("Size of BST",bst.BSTsize())
    bst.remove(40)
    print(bst.inorder_walk())
    print("Size of BST",bst.BSTsize())
