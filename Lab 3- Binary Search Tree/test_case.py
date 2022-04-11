import unittest
from bst import BinarySearchTree

class BSTTestCase(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()
        self.bst.add(20, "Value for 20")
        self.bst.add(30, "Value for 30")
        self.bst.add(40, "Value for 40")
        self.bst.add(5, "Value for 5")
        self.bst.add(1, "Value for 1")
        self.bst.add(10, "Value for 10")
        self.bst.add(25, "Value for 25")
        self.bst.add(0, "Value for 0")
        self.bst.add(60, "Value for 60")
        self.bst.add(35, "Value for 35")
        self.bst.add(4, "Value for 4")
    
    def test_add(self):
        bsTree = BinarySearchTree()
        self.assertEqual(bsTree.BSTsize(), 0)
        bsTree.add(15, "Value for 15")
        self.assertEqual(bsTree.BSTsize(), 1)
        bsTree.add(10, "Value for 10")
        self.assertEqual(bsTree.BSTsize(), 2)
        self.assertEqual(bsTree.search(10), "Value for 10")
        self.assertEqual(bsTree.search(15), "Value for 15")

    def test_inorder(self):
        actual_output = self.bst.inorder_walk()
        expected_output = [0, 1, 4, 5, 10, 20, 25, 30, 35, 40, 60]
        self.assertListEqual(actual_output, expected_output)
    
    def test_postorder(self):
        actual_output = self.bst.postorder_walk()
        expected_output = [0, 4, 1, 10, 5, 25, 35, 60, 40, 30, 20]
        self.assertListEqual(actual_output, expected_output)

    def test_preorder(self):
        actual_output = self.bst.preorder_walk()
        expected_output = [20, 5, 1, 0, 4, 10, 30, 25, 40, 35, 60]
        self.assertListEqual(actual_output,expected_output)

    def test_search(self):
        actual_output = self.bst.search(25)
        expected_output = "Value for 25"
        self.assertEqual(actual_output, expected_output)
        actual_output = self.bst.search(45)
        expected_output = False
        self.assertEqual(actual_output, expected_output)

    def test_remove(self):
        self.bst.remove(10)
        self.assertEqual(self.bst.BSTsize(), 10)
        self.assertListEqual(self.bst.inorder_walk(), [0, 1, 4, 5, 20, 25, 30, 35, 40, 60])
        self.assertListEqual(self.bst.preorder_walk(), [20, 5, 1, 0, 4, 30, 25, 40, 35, 60])
        self.assertListEqual(self.bst.postorder_walk(), [0, 4, 1, 5, 25, 35, 60, 40, 30, 20])
    
    def test_smallest(self):
        self.assertTupleEqual(self.bst.smallest(), (0, "Value for 0"))
        self.bst.remove(0)
        self.assertTupleEqual(self.bst.smallest(), (1, "Value for 1"))
    
    def test_largest(self):
        self.assertTupleEqual(self.bst.largest(), (60, "Value for 60"))
        self.bst.remove(60)
        self.assertTupleEqual(self.bst.largest(), (40, "Value for 40"))

if __name__ == "__main__":
    unittest.main() 