import os
from asciitree.drawing import BoxStyle, BOX_LIGHT, BOX_HEAVY, BOX_DOUBLE
from asciitree import LeftAligned

def tree(directory):
    def build_tree(path):
        name = os.path.basename(path)
        if os.path.isdir(path):
            return (name, [build_tree(os.path.join(path, child)) for child in os.listdir(path)])
        else:
            return name
    
    tree = build_tree(directory)
    box_style = BoxStyle(gfx=BOX_LIGHT, horiz_len=1)
    tr = LeftAligned(draw=box_style)
    return tr(tree)

if __name__ == '__main__':
    print(tree('/path/to/directory'))
