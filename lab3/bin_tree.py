
# вар. 7

left_leaf_default = lambda root: root*3
right_leaf_default = lambda root: root-4

def gen_bin_tree(height=4, root=7, left_leaf=left_leaf_default, right_leaf=right_leaf_default):
    """Генерирует и возвращает словарь, содержащий бинарное дерево с заданными параметрами
    
    Аргументы:
    height - глубина дерева (по умолчанию 4)
    root - значение в корне (по умолчанию 7)
    left_leaf - лямбда-функция для вычисления значения левого потомка (по умолчанию lambda root: root*3)
    right_leaf - лямбда-функция для вычисления значения правого потомка (по умолчанию lambda root: root-4)
    """
    return {"value": root, "left": gen_bin_tree(height-1, left_leaf(root), left_leaf, right_leaf) if height > 0 else {}, "right": gen_bin_tree(height-1, right_leaf(root), left_leaf, right_leaf)  if height > 0 else {}}
