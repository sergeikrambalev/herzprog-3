"""Модуль генерации бинарного дерева.
Вариант 7.

Дерево представляется вложенными словарями вида
    {"value": <int>, "left": <поддерево>, "right": <поддерево>},
у листьев поля "left" и "right" — пустые словари.

Значения потомков по умолчанию вычисляются функциями:
    left_leaf(root)  = root * 3
    right_leaf(root) = root - 4
"""

left_leaf_default = lambda root: root * 3
right_leaf_default = lambda root: root - 4

def gen_bin_tree(height: int = 4, root: int = 7, left_leaf = left_leaf_default, right_leaf = right_leaf_default):
    """Генерирует и возвращает бинарное дерево с заданными параметрами.

    Аргументы:
        height: число уровней под корнем (при height=0 остаётся только
            корень, у которого "left" и "right" — пустые словари).
        root: значение в корне (по умолчанию 7).
        left_leaf: функция вычисления значения левого потомка
            (по умолчанию ``lambda root: root * 3``).
        right_leaf: функция вычисления значения правого потомка
            (по умолчанию ``lambda root: root - 4``).

    Возвращает:
        Словарь ``{"value": ..., "left": ..., "right": ...}``,
        описывающий построенное дерево.
    """
    if height <= 0:
        return {"value": root, "left": {}, "right": {}}

    left_subtree = gen_bin_tree(
        height - 1, left_leaf(root), left_leaf, right_leaf
    )
    right_subtree = gen_bin_tree(
        height - 1, right_leaf(root), left_leaf, right_leaf
    )

    return {"value": root, "left": left_subtree, "right": right_subtree}
