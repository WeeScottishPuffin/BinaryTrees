# About
---

This is a simple python module to create and manipulate Binary trees.

## Binary Trees and Nodes
A binary tree object can be created with.
```BinaryTree.BinaryTree(root)```

This will create a binary tree with one (root) node. To add nodes, just use ```BinaryTree.appendNode(value)```.
At any time, you can call the ```delete()``` function on a ```Node()``` object to destroy it. This will re-add all other nodes to the tree.
A list of nodes can be accessed with ```BinaryTree.nodes```.
Other functions and attributes include:
### BinaryTree()
- ```appendNode(value)```
- ```printTree()```
- ```sort()```
- ```nodes```
- ```root```
### Node()
- ```delete()```
- ```children```
- ```isLeaf```
- ```left```
- ```level```
- ```parent```
- ```right```
- ```side```
- ```tree```
- ```value```