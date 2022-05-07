import unittest
from Fractional_Knapsack import GreedyAlgorithm
from Fractional_Knapsack import F_BruteForce
from Knapsack import K_BruteForce
from Knapsack import DynamicPrograming

class KnapsackTestCase(unittest.TestCase):
    def test_0_1_Knapsack(self):
        #Case 1
        w_1=[3,4,6,5]
        p_1=[2,3,1,4]
        m_1=8
        n_1=len(w_1)
        #Case 2
        w_2=[12,2,1,1,4]
        p_2=[4,2,1,2,4]
        m_2=15
        n_2=len(w_2)
        self.assertEqual(K_BruteForce(n_1,m_1,p_1,w_1),(6, 8, '1001'))
        self.assertEqual(DynamicPrograming(n_1,m_1,p_1,w_1),6)
        self.assertEqual(K_BruteForce(n_2,m_2,p_2,w_2),(9, 8, '01111'))
        self.assertEqual(DynamicPrograming(n_2,m_2,p_2,w_2),9)
    
    def test_fractional(self):
        #Case 1
        p_1=[12,14,56,8]
        w_1=[2,7,10,5]
        m_1=20
        n_1=len(p_1)
        #Case 2
        w_2=[12,2,1,1,4]
        p_2=[4,2,1,2,4]
        m_2=15
        n_2=len(w_2)
        self.assertEqual(F_BruteForce(n_1,m_1,p_1,w_1),(83.6, 20, '1110'))
        self.assertEqual(GreedyAlgorithm(n_1,m_1,p_1,w_1),83.6)
        self.assertEqual(F_BruteForce(n_2,m_2,p_2,w_2),(11.333333333333332, 15, '01111'))
        self.assertEqual(GreedyAlgorithm(n_2,m_2,p_2,w_2),11.333333333333332)

if __name__ == "__main__":
    unittest.main() 

