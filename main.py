import graphviz
from queue import Queue
import random
import time
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_balanced_bst(arr, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    root = TreeNode(arr[mid])
    root.left = build_balanced_bst(arr, start, mid - 1)
    root.right = build_balanced_bst(arr, mid + 1, end)
    return root


def visualize_tree(root):
    g = graphviz.Digraph(format='png')

    def dfs(node, parent=None):
        if node:
            # If the node value is in the target list, add a different style to it
            if node.val in target:
                g.node(str(node.val), style='filled', fillcolor='lightblue')
            else:
                g.node(str(node.val))
            if parent:
                g.edge(str(parent.val), str(node.val))
            dfs(node.left, node)
            dfs(node.right, node)


    dfs(root)
    return g


def find_element_dfs(root, target):
    stack = [root]
    path = []
    while stack:
        node = stack.pop()
        path.append(node.val)
        if node.val == target:
            return node, path
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return None, path

def find_element_bfs(root, target):
    queue = [root]
    path = []
    while queue:
        node = queue.pop(0)
        path.append(node.val)
        if node.val == target:
            return node, path
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return None, path


# Size of the three
n = 31
# Build the tree
arr = list(range(n))
random.shuffle(arr)
root = build_balanced_bst(arr, 0, len(arr) - 1)

DFS_time = 0
BFS_time = 0

repeat = 50
for j in range(1, repeat + 1):
    target = arr.copy()
    random.shuffle(target)
    target = target[:5]

    for i in range(5):
        if j == repeat:
            print(f"Target = {target[i]}")
        # Search for the element 8 using DFS
        start_time = time.time()
        time.sleep(0.25)
        node, path = find_element_dfs(root, target[i])
        end_time = time.time() - 0.25
        DFS_time += (end_time - start_time)
        if j == repeat:
            print("Full traversal path of DFS:", path)

        # Search for the element using BFS
        start_time = time.time()
        time.sleep(0.25)
        node, path = find_element_bfs(root, target[i])
        end_time = time.time() - 0.25
        BFS_time += (end_time - start_time)
        if j == repeat:
            print("Full traversal path of BFS:", path)

        if j == repeat:
            print("=====================================")

print(f"DFS time: {DFS_time/repeat}")
print(f"BFS time: {BFS_time/repeat}")

# Visualize the tree
tree_graph = visualize_tree(root)
tree_graph.render('balanced_bst')


# Create a bar chart
fig, ax = plt.subplots()
bar_width = 0.35
opacity = 0.8
rects1 = ax.bar('DFS', DFS_time/repeat, bar_width, alpha=opacity, color='b', label='DFS')
rects2 = ax.bar('BFS', BFS_time/repeat, bar_width, alpha=opacity, color='g', label='BFS')

# Add labels, title, and legend
ax.set_xlabel('Search Algorithm')
ax.set_ylabel('Time (seconds)')
ax.set_title('Time Comparison of DFS and BFS')
ax.legend()

# Show the graph
plt.show()