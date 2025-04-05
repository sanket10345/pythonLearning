"""
LeetCode Problem 71: Simplify Path
"""

def simplifyPath(path):
    """
    :type path: str
    :rtype: str
    """
    pathArr=path.split('/')
    pathStack = []
    for i in pathArr:
        if i =='' or i == '.':
          continue
        if i == '..':
           pathStack.pop() if pathStack else None
           continue
        pathStack.append(i)
        #print(i)
    return '/'+ '/'.join(map(str, pathStack))

print(simplifyPath('/../'))