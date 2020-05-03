class Node:
   def __init__(self, key):
      self.left = None
      self.right = None
      self.val = key


def run():
   root = Node(1)
   root.left = Node(2)
   root.right = Node(3)
   root.left.left = Node(4)
   root.left.right = Node(5)

   print("Preorder traversal of binary tree is")
   print_preorder(root)

   print("Inorder traversal of binary tree is")
   print_inorder(root)

   print("Postorder traversal of binary tree is")
   print_postorder(root)


def print_inorder(node):
   if node:
      # First recur on left child
      print_inorder(node.left)

      # then print the data of node
      print(node.val),

      # now recur on right child
      print_inorder(node.right)

   # A function to do postorder tree traversal


def print_postorder(node):
   if node:
      # First recur on left child
      print_postorder(node.left)

      # the recur on right child
      print_postorder(node.right)

      # now print the data of node
      print(node.val),

   # A function to do preorder tree traversal


def print_preorder(node):
   if node:
      # First print the data of node
      print(node.val),

      # Then recur on left child
      print_preorder(node.left)

      # Finally recur on right child
      print_preorder(node.right)


if __name__ == "__main__":
    run()