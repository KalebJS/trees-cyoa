print('Once upon a time...')

######
# TREENODE CLASS
######

class TreeNode :
    def __init__(self, story_piece) :
        self.story_piece = story_piece
        self.choices = []
    
    def get_input (self) :
        choice = input('Enter 1 or 2 to continue the story: ')
        choices = ['1','2']
        while choice not in choices :
            choice = input('Please. Only enter a valid choice of 1 or 2. Try again: ')
        else :
            if choice == '1' :
                return 0
            elif choice == '2' :
                return 1

    def add_choice (self, choice) :
        if choice not in self.choices :
            self.choices.append(choice)
    
    def traverse (self) :
        story_node = self
        print(story_node.story_piece)

        while len(story_node.choices) > 0 :
            choice = story_node.get_input()
            story_node = story_node.choices[choice]
            print(story_node.story_piece)
        else :
            print("End of game. Thanks for playing.")




######
# VARIABLES FOR TREE
######

story_root = TreeNode("""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
""")
choice_a = TreeNode("""
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
""")
choice_a_1 = TreeNode("""
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")
choice_a.add_choice(choice_a_1)
choice_a_2 = TreeNode("""
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.

YOU REMAIN LOST.
""")
choice_a.add_choice(choice_a_2)
story_root.add_choice(choice_a)
choice_b = TreeNode("""
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
""")
choice_b_1 = TreeNode("""
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.

YOU REMAIN LOST.
""")
choice_b.add_choice(choice_b_1)
choice_b_2 = TreeNode("""
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")
choice_b.add_choice(choice_b_2)
story_root.add_choice(choice_b)




######
# TESTING AREA
######

story_root.traverse()