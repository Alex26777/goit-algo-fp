import uuid
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def bfs(tree_root):
    """Обхід дерева в ширину зі зміною кольору вузлів."""
    queue = deque([tree_root])
    order = []
    colors = {}
    color_intensity = 255
    while queue:
        node = queue.popleft()
        order.append(node)
        # Встановлення кольору в залежності від послідовності обходу (від темного до світлого)
        colors[node.id] = f'#{color_intensity:02x}91f0'
        color_intensity = max(color_intensity - 30, 100)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
    return order, colors

def dfs(tree_root):
    """Обхід дерева в глибину зі зміною кольору вузлів."""
    stack = [tree_root]
    order = []
    colors = {}
    color_intensity = 255
    while stack:
        node = stack.pop()
        order.append(node)
        # Встановлення кольору в залежності від послідовності обходу (від темного до світлого)
        colors[node.id] = f'#{color_intensity:02x}91f0'
        color_intensity = max(color_intensity - 30, 100)

        # Спочатку додаємо правого нащадка, а потім лівого, щоб лівий був оброблений першим
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
            
    return order, colors

def add_edges(graph, node, pos, colors, x=0, y=0, layer=1):
    """Допоміжна функція для додавання вузлів та ребер до графа."""
    if node is not None:
        graph.add_node(node.id, color=colors.get(node.id, node.color), label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, colors, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, colors, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, colors=None):
    """Візуалізація бінарного дерева з колорованими вузлами."""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos, colors if colors else {})

    node_colors = [data['color'] for node, data in tree.nodes(data=True)]
    labels = {node: data['label'] for node, data in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Функція обходу в ширину (BFS)
bfs_order, bfs_colors = bfs(root)
# Функція обходу в глибину (DFS)
dfs_order, dfs_colors = dfs(root)

# Візуалізація дерева з обходом в ширину
print("Обхід дерева в ширину (BFS):")
draw_tree(root, bfs_colors)

# Візуалізація дерева з обходом в глибину
print("Обхід дерева в глибину (DFS):")
draw_tree(root, dfs_colors)