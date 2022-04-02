import unittest
from insertion_sort import Insertion_Sort
from merge_sort import Merge_Sort, Merge

class SortTestCase(unittest.TestCase):
    def test_insertion_sort(self):
        value1=[1,2,3,4,5]
        value2=[5,4,3,2,1]
        value3=[100,56,23,64,23,67]
        value4=[0,23,67,100,234,26,87]
        self.assertListEqual(Insertion_Sort(value1),[1,2,3,4,5])
        self.assertListEqual(Insertion_Sort(value2),[1,2,3,4,5])
        self.assertListEqual(Insertion_Sort(value3),[23,23,56,64,67,100])
        self.assertListEqual(Insertion_Sort(value4),[0,23,26,67,87,100,234])
    
    def test_merge_sort(self):
        value1=[1,2,3,4,5]
        value2=[5,4,3,2,1]
        value3=[100,56,23,64,23,67]
        value4=[0,23,67,100,234,26,87]
        self.assertListEqual(Merge_Sort(value1,0,len(value1)-1),[1,2,3,4,5])
        self.assertListEqual(Merge_Sort(value2,0,len(value2)-1),[1,2,3,4,5])
        self.assertListEqual(Merge_Sort(value3,0,len(value3)-1),[23,23,56,64,67,100])
        self.assertListEqual(Merge_Sort(value4,0,len(value4)-1),[0,23,26,67,87,100,234])

    def test_merge(self):
        value1=[1,2,3,4,5]
        value2=[3,4,5,1,2]
        value3=[23,56,100,23,64,67]
        value4=[0,23,67,100,26,87,234]
        self.assertListEqual(Merge(value1,0,(len(value1)-1)//2,len(value1)-1),[1,2,3,4,5])
        self.assertListEqual(Merge(value2,0,(len(value2)-1)//2,len(value2)-1),[1,2,3,4,5])
        self.assertListEqual(Merge(value3,0,(len(value3)-1)//2,len(value3)-1),[23,23,56,64,67,100])
        self.assertListEqual(Merge(value4,0,(len(value4)-1)//2,len(value4)-1),[0,23,26,67,87,100,234])


if __name__=="__main__":
    unittest.main()
