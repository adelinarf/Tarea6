from seg import *
from treap import *

# Nodo para visitar el arbol y ordenarlo
class Node: 

	def __init__(self,item = 0): 
		self.key = item 
		self.left,self.right = None,None

root = Node() 

root = None

def insert(key): 
	global root 
	root = insert_node(root, key) 

def insert_node(root, key): 
	if (root == None): 
		root = Node(key) 
		return root 

	if (key < root.key): 
		root.left = insert_node(root.left, key) 
	elif (key > root.key): 
		root.right = insert_node(root.right, key) 
	return root 

def inorder_order(root): 
	if (root != None):
		l,r=[],[]
		if root.left!=None:
			l = inorder_order(root.left)
		if root.right!=None:
			r = inorder_order(root.right) 
		return l+[root.key]+r
	
def create_tree(arr): 
	for i in range(len(arr)): 
		insert(arr[i]) 

def consult(A,consultas):
	create_tree(A) #O(n)
	ordered_A = inorder_order(root)   #O(nlogn) y memoria O(n)
	x = SegmentTree(A,ordered_A)   #O(nlogn) y memoria O(logn)

	def Q(a,b,pos): #O(nlogn)
		Z = x.query(a-1,b-1) #O(logn)
		o = order_treap(Z,ordered_A) #O(nlogn)
		return (o[pos-1])

	for z in range(len(consultas)):
		s = consultas[z]
		q = Q(s[0],s[1],s[2])  #O(Q*n*logn)
		string = "El {}-esimo elemento entre {} y {} es {} \n".format(s[2], s[0],s[1],q)
		print(string)

A = [2,6,3,1,8,4,7,9,5]  #modificar con el arreglo deseado
consultas=[[3,5,2],[1,3,2],[2,6,3]]
#La lista de consultas contiene listas de la forma
#[i,j,k] k-esimo elemento del arreglo A[i..j]
consult(A,consultas)