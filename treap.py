import random 

class TreapNode:
	def __init__(self, key):
		self.key = key
		self.priority = random.randint(0, 99)
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

def insert_implicit(root,n):
	if not root:
		return TreapNode(n,-1)	
	if key <= root.key:
		root.left = insert_implicit(root.left, key)		
		if root.left.priority > root.priority:
			root = rightRotate(root)
	else:
		root.right = insert_implicit(root.right, key)		
		if root.right.priority > root.priority:
			root = leftRotate(root)
	return root


def insert(root, key):
	if not root:
		return TreapNode(key)	
	if key <= root.key:
		root.left = insert(root.left, key)		
		if root.left.priority > root.priority:
			root = rightRotate(root)
	else:
		root.right = insert(root.right, key)		
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


def order_treap(M,A):
	random.seed(0)

	root = None
	for x in range(len(M)):
		if M[x]==1:
			root = insert(root, A[x])

	z = inorder(root)
	return z

