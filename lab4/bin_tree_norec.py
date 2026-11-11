
# вар. 7

left_leaf_default = lambda root: root*3
right_leaf_default = lambda root: root-4

def gen_bin_tree(height=4, root=7, left_leaf=left_leaf_default, right_leaf=right_leaf_default):
    tree = {"value": root, "left": {}, "right": {}}
    
    level = [tree]
    for _ in range(height):
        nlevel = []
        for node in level:
            nleft = left_leaf(node["value"])
            nright = right_leaf(node["value"])
            node["left"] = {"value": nleft, "left": {}, "right": {}}
            node["right"] = {"value": nright, "left": {}, "right": {}}
            nlevel.append(node["left"])
            nlevel.append(node["right"])
        level = nlevel
    
    return tree


print(gen_bin_tree(1))
