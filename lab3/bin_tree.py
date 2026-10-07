
# вар. 7

left_leaf_default = lambda root: root*3
right_leaf_default = lambda root: root-4

def gen_bin_tree(height=4, root=7, left_leaf=left_leaf_default, right_leaf=right_leaf_default):
    """Return binary tree of chosen 'height', with 'root' value on root node and values on leaves, determined by 'left_leaf' and 'right_leaf' lambda function"""
    if height == 0:
        return {"value": root, "left": {}, "right": {}}
    return {"value": root, "left": gen_bin_tree(height-1, left_leaf(root), left_leaf, right_leaf), "right": gen_bin_tree(height-1, right_leaf(root), left_leaf, right_leaf)}

print(gen_bin_tree(1))
