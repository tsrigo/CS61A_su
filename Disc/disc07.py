class Tree:
    """A tree is a label and a list of branches."""
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches
     

def height(t):
    """Return the height of a tree.

    >>> t = Tree(3, [Tree(5, [Tree(1)]), Tree(2)])
    >>> height(t)
    2
    >>> t = Tree(3, [Tree(1), Tree(2, [Tree(5, [Tree(6)]), Tree(1)])])
    >>> height(t)
    3
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        return 0
    
    tep = 0
    for i in t.branches:
        hh = height(i)
        if hh > tep:
            tep = hh
    return tep + 1
    # alternate solutions
    '''
    return 1 + max([height(branch) for branch in t.branches])
    return 1 + max([-1] + [height(branch) for branch in t.branches])
    return max([1 + height(b) for b in t.branches], default=0)
    '''


def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = Tree(1, [Tree(5, [Tree(1), Tree(3)]), Tree(10)])
    >>> max_path_sum(t)
    11
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        return t.label
    
    tep = 0
    for i in t.branches:
        hh = max_path_sum(i)
        if hh > tep:
            tep = hh
    return tep + t.label
    # subsitute ans
    return t.label + max([max_path_sum(b) for b in t.branches])

def find_path(t, x):
    """
    >>> t = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    if t.label == x:
        return [t.label]
    
    for i in t.branches:
        tep = find_path(i, x)
        if tep:
            return [t.label] + tep

