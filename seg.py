import numpy as np

class SegmentTree:

    def __init__(self, array,sort):
        self.array = array
        self.sorted_array = sort
        self.root = SegmentTreeNode(0, len(array) - 1, self)

    def query(self, start, end):
        return self.root._query(start, end)

    def __repr__(self):
        return self.root.__repr__()

def create_occurrence(sortedA,A,start,end):
    C = [0]*len(A)
    for x in range(len(A)):
        if sortedA[x] in set(A[start:end+1]):
            C[x] = 1
    return C

def new(left,right):
    return list(np.array(left) + np.array(right))

class SegmentTreeNode:

    def __init__(self, start, end, segment_tree):
        self.range = (start, end)
        self.parent_tree = segment_tree
        self.range_value = None
        self.values = create_occurrence(segment_tree.sorted_array,segment_tree.array,start,end)
        self.ordered = sorted(segment_tree.array[start:end+1])
        self.left = None
        self.right = None
        if start == end:
            return
        self.left = SegmentTreeNode(start, start + (end - start) // 2,
                                    segment_tree)
        self.right = SegmentTreeNode(start + (end - start) // 2 + 1, end,
                                     segment_tree)

    def _query(self, start, end):
        if end < self.range[0] or start > self.range[1]:
            return None
        if start <= self.range[0] and self.range[1] <= end:
            return self.values
        left_res = self.left._query(start, end) if self.left else None
        right_res = self.right._query(start, end) if self.right else None
        if left_res is None:
            return right_res
        if right_res is None:
            return left_res

        return new(left_res,right_res)

    def __repr__(self):
        ans = "({}, {}): {} {} {}\n".format(self.range[0], self.range[1],
                                      self.values, self.ordered,self.generated)
        if self.left:
            ans += self.left.__repr__()
        if self.right:
            ans += self.right.__repr__()
        return ans

