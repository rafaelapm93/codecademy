######
# TREENODE CLASS
######
class TreeNode:
    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []

    def add_child(self,node):
        self.choices.append(node)

    def traverse(self):
        story_name = self
        print(self.story_piece)


root = """
        You are in a forest clearing. There is a path to the left.
        A bear emerges from the trees and roars!
        Do you: 
        1 ) Roar back!
        2 ) Run to the left...
        """

choice_a = """
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
"""

choice_b ="""
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
"""

story_root = TreeNode(root)
#print(story_root.story_piece)



user_choice = input("What is your name? ")
print(user_choice)

tree_a = TreeNode(choice_a)
tree_b = TreeNode(choice_b)

story_root.add_child(tree_a)
story_root.add_child(tree_b)
######
# VARIABLES FOR TREE
######

######
# TESTING AREA
######
print('Once upon a time…')
story_root.traverse()

while story_root.choices != []:

    choice = input("Enter 1 or 2 to continue the story: ")
    
    if choice not in ['1','2']:
        print('Chocie only can be 1 and 2')
    
    else:
        chose_index = int(choice) - 1
        chosen_child = story_root.choices[chose_index]
        print(chosen_child.story_piece)
        story_node = chosen_child


