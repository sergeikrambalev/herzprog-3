"""Модуль генерации бинарного дерева (итеративная версия).
Вариант 7.

Дерево представляется вложенными словарями вида
    {"value": <int>, "left": <поддерево>, "right": <поддерево>},
у листьев поля "left" и "right" — пустые словари.

Дерево строится по уровням без рекурсии: на каждой итерации для всех
узлов текущего уровня создаются потомки, которые становятся узлами
следующего уровня.

Значения потомков по умолчанию вычисляются функциями:
    left_leaf(root)  = root * 3
    right_leaf(root) = root - 4
"""

left_leaf_default = lambda root: root*3
right_leaf_default = lambda root: root-4

def gen_bin_tree(height: int = 4, root: int = 7, left_leaf = left_leaf_default, right_leaf = right_leaf_default):
    """Генерирует и возвращает бинарное дерево с заданными параметрами.

    Реализация итеративная: узлы обходятся по уровням, потомки
    добавляются в узлы текущего уровня и становятся узлами следующего.

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
    tree = {"value": root, "left": {}, "right": {}}

    level = [tree]
    for _ in range(height):
        next_level = []
        for node in level:
            left_value: int = left_leaf(node["value"])
            right_value: int = right_leaf(node["value"])

            node["left"] = {"value": left_value, "left": {}, "right": {}}
            node["right"] = {"value": right_value, "left": {}, "right": {}}

            next_level.append(node["left"])
            next_level.append(node["right"])
        level = next_level

    return tree
