import unittest
from linear_search import linear_search
from binary_search import binary_search

class TestSearchMethon(unittest.TestCase):
    
    def test_linear_search(self):
        values=[0,13,16,18,26,100,180]
        self.assertEqual(linear_search(values,0),0)
        self.assertEqual(linear_search(values,18),3)
        self.assertEqual(linear_search(values,100),5)
        self.assertEqual(linear_search(values,1),-1)
    
    def test_binary_search(self):
        values=[0,1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(binary_search(0,len(values)-1,values,0),0)
        self.assertEqual(binary_search(0,len(values)-1,values,1),1)
        self.assertEqual(binary_search(0,len(values)-1,values,100),-1)
        self.assertEqual(binary_search(0,len(values)-1,values,10),10)
        

if __name__=="__main__":
    unittest.main()