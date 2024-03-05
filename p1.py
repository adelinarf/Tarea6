import random 

class TreapNode:
	def __init__(self, key,pos):
		self.key = key
		self.priority = random.randint(0, 99)
		self.pos = pos
		self.left = None
		self.right = None

def rightRotate(y):
	x = y.left
	T2 = x.right	
	x.right = y
	y.left = T2
	return x
	
def leftRotate(x):
	y = x.right
	T2 = y.left	
	y.left = x
	x.right = T2	
	return y

def insert(root, key,pos):
	if not root:
		return TreapNode(key,pos)	
	if key <= root.key:
		root.left = insert(root.left, key,pos)		
		if root.left.priority > root.priority:
			root = rightRotate(root)
	else:
		root.right = insert(root.right, key,pos)		
		if root.right.priority > root.priority:
			root = leftRotate(root)
	return root

def deleteNode(root, key):
	if not root:
		return root
	
	if key < root.key:
		root.left = deleteNode(root.left, key)
	elif key > root.key:
		root.right = deleteNode(root.right, key)
	else:
		if not root.left:
			temp = root.right
			root = None
			return temp
		elif not root.right:
			temp = root.left
			root = None
			return temp		
		elif root.left.priority < root.right.priority:
			root = leftRotate(root)
			root.left = deleteNode(root.left, key)
		else:
			root = rightRotate(root)
			root.right = deleteNode(root.right, key)

	return root

def search(root, key):
	if not root or root.key == key:
		return root
	if root.key < key:
		return search(root.right, key)
	return search(root.left, key)

def inorder(root):
	if root:
		l = []
		if root.left:
			l = inorder(root.left)
		r = []
		if root.right:
			r = inorder(root.right)
		return l+[root.key]+r

def searchKey(root, pos):
	if not root or root.pos == pos:
		return root.key
	if root.right:
		return searchKey(root.right, pos)
	if root.left:
		return searchKey(root.left, pos)

def changeKeys(root, pos,newkey):
	if root.pos == pos:
		root.key = newkey
		return root	
	if root.right:
		return changeKeys(root.right, pos,newkey)
	if root.left:
		return changeKeys(root.left, pos,newkey)

def swap(root,i,j):
	node_i = searchKey(root,i)
	node_j = searchKey(root,j)
	changeKeys(root,i,node_j)
	changeKeys(root,j,node_i)

def multiswap(root,i,j,N):
	a,b = i,j 
	while a<j and b<N:
		swap(root,a,b)
		a+=1
		b+=1


def swap_permutation(M,i,j):
	random.seed(0)

	root = None
	for x in range(len(M)):
		root = insert(root, M[x],x)

	x = multiswap(root, i,j,len(M))
	z = inorder(root)
	return (z)
	
def permutation(M,i,j):
	z = swap_permutation(M,i,j)
	string = "La operacion multiswap({},{}) de {} da como resultado: {}\n".format(i,j,M,z)
	print(string)

M = [1,2,3,4,5]
permutation(M,1,3)