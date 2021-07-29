"""
Build a tree data structure that takes name and designation in data part of TreeNode class.
Now extend print_tree function such that it can print either name tree, designation tree or name and designation 
tree. 
"""


class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level += 1

        return level

    def print_tree(self, filter):
        space = '  ' * self.get_level()
        prefix = space + '\\'

        if filter == 'name':
            print(prefix + self.name)
            if self.children:
                for child in self.children:
                    child.print_tree(filter)

        if filter == 'designation':
            print(prefix + self.designation)
            if self.children:
                for child in self.children:
                    child.print_tree(filter)

        if filter == 'both':
            print(prefix + f'{self.name} ({self.designation})')  # name (designation) -> Taufiq (CEO)
            if self.children:
                for child in self.children:
                    child.print_tree(filter)


def build_management_tree():
    root = TreeNode('Taufiq Rahman', 'CEO')

    branch_1 = TreeNode('Jeff Besos', 'Infra Head')
    branch_1.add_child(TreeNode('Bill Gates', 'Cloud Manager'))
    branch_1.add_child(TreeNode('Steve Jobs', 'App Manager'))

    branch_2 = TreeNode('Mark Zuckerberg', 'HR Head')
    branch_2.add_child(TreeNode('Peter Pan', 'Recruitment Manager'))
    branch_2.add_child(TreeNode('Elon Musk', 'Policy Manager'))

    root.add_child(branch_1)
    root.add_child(branch_2)

    return root


if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name")  # prints only name hierarchy
    print()
    root_node.print_tree("designation")  # prints only designation hierarchy
    print()
    root_node.print_tree("both")  # prints both (name and designation) hierarchy
