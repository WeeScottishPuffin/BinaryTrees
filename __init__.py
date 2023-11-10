class BinaryTree:
  def __init__(self, startval):
    self.root = BinaryTree.Node(startval)
    self.root.tree = self
    self.nodes = [self.root]
    self.queue = []

  def __step(self,node,l):
    if node.left:
      self.__step(node.left,l)
    l.append(node.value)
    if node.right:
      self.__step(node.right,l)

  def sort(self):
    result = []
    self.__step(self.root,result)
    print(result)

  def printTree(self):
    for node in self.nodes:
      node._itr = False
    itr = True
    curItrNode = self.root
    strs = ""
    while itr:
      #print node
      if not curItrNode._itr:
        print("|   " * curItrNode.level, strs, curItrNode.value,sep="")
      curItrNode._itr = True
      #left first
      if curItrNode.left and not curItrNode.left._itr:
        curItrNode = curItrNode.left
        strs = "l"
      elif curItrNode.right and not curItrNode.right._itr:
        curItrNode = curItrNode.right
        strs = "r"
      else:
        #else, go one up
        if curItrNode.parent == None: return
        curItrNode = curItrNode.parent

  def appendNode(self, value):
    newNode = BinaryTree.Node(value)
    newNode.tree=self
    self.nodes.append(newNode)
    #append the node
    itr = True
    level = 0
    curItrNode = self.root
    while itr:
      level += 1
      if value > curItrNode.value:
        #right is bigger
        if curItrNode.right:
          curItrNode = curItrNode.right
        else:
          curItrNode.right = newNode
          newNode.level = level
          newNode.parent = curItrNode
          newNode.side = "right"
          curItrNode.isLeaf = False
          curItrNode.children = [curItrNode.left, curItrNode.right]
          itr = False
      else:
        #left is smaller or equal
        if curItrNode.left:
          curItrNode = curItrNode.left
        else:
          curItrNode.left = newNode
          newNode.level = level
          newNode.parent = curItrNode
          newNode.side = "left"
          curItrNode.isLeaf = False
          curItrNode.children = [curItrNode.left, curItrNode.right]
          itr = False

  class Node:
    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None
      self.parent = None
      self.tree = None
      self.level = 0
      self.children = [self.left, self.right]
      self._itr = False
      self.isLeaf = True
      self.side = ""

    def __repr__(self):
      lv,rv,pv=None,None,None
      if self.left: lv = self.left.value
      if self.right: rv = self.right.value
      if self.parent: pv = self.parent.value

      return str("Node(value=%s,left=%s,right=%s,parent=%s)" % (
          self.value, lv,rv,pv))

    def delete(self,first=True):
      if self == self.tree.root: return
      oldLeft = self.left
      oldRight = self.right
      if self.side == "left": self.parent.left = None
      if self.side == "right": self.parent.right = None
      if self.parent: self.parent.children = [self.parent.left, self.parent.right]
      if self.parent.left == None and self.parent.right == None:
        self.parent.isLeaf = True
      oldVal = self.value
      tree = self.tree
      self = None
      if oldLeft: 
        oldLeft.delete(False)
      if oldRight:
        oldRight.delete(False)
      if not first: 
        tree.appendNode(oldVal)