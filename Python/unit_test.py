import unittest
from selection import selectionSort
from insertion import insertionSort
from merge import mergeSort
from bubble import bubbleSort
from quick import quickSort
from counting import countingSort
from radix import radixSort

class SelectionSortTestCaste(unittest.TestCase):
    
    def test_selectionSort(self):
        self.assertEqual(selectionSort([1,2,3,4,5,6,7,8,9,10]), [1,2,3,4,5,6,7,8,9,10])
        self.assertEqual(selectionSort([61,89,97,2,3,5,7,11,13,17,19,23,29,31,37,41,67,71,73,79,83]), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 61, 67, 71, 73, 79, 83, 89, 97])
        self.assertEqual(selectionSort([43,47,53,59,61,89,97,2,3,5,7,11,13,17,19,23,29,31,37,41,67,71,73,79,83]), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

class InsertionSortTestCase(unittest.TestCase):
    
    def test_insertionSort(self):
        self.assertEqual(insertionSort([1,2,3,4,5,6,7,8,9,10]), [1,2,3,4,5,6,7,8,9,10])
        self.assertEqual(insertionSort([61,89,97,2,3,5,7,11,13,17,19,23,29,31,37,41,67,71,73,79,83]), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 61, 67, 71, 73, 79, 83, 89, 97])
        self.assertEqual(insertionSort([43,47,53,59,61,89,97,2,3,5,7,11,13,17,19,23,29,31,37,41,67,71,73,79,83]), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

class MergeSortlTestCase(unittest.TestCase):

    def test_mergeSort(self):
        self.assertEqual(mergeSort([1,2,3,4,5,6,7,8,9,10]), [1,2,3,4,5,6,7,8,9,10])
        self.assertEqual(mergeSort([61,89,97,2,3,5,7,11,13,17,19,23,29,31,37,41,67,71,73,79,83]), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 61, 67, 71, 73, 79, 83, 89, 97])
        self.assertEqual(mergeSort([43,47,53,59,61,89,97,2,3,5,7,11,13,17,19,23,29,31,37,41,67,71,73,79,83]), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

class QuickSortTestCase(unittest.TestCase):

    def test_quickSort(self):
        self.assertEqual(quickSort([1,2,3,4,5,6,7,8,9,10]), [1,2,3,4,5,6,7,8,9,10])
        self.assertEqual(quickSort([61,89,97,2,3,5,7,11,13,17,19,23,29,31,37,41,67,71,73,79,83]), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 61, 67, 71, 73, 79, 83, 89, 97])
        self.assertEqual(quickSort([43,47,53,59,61,89,97,2,3,5,7,11,13,17,19,23,29,31,37,41,67,71,73,79,83]), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

class BubbleSortTestCase(unittest.TestCase):
    
    def test_bubbleSort(self):
        self.assertEqual(bubbleSort([1,2,3,4,5,6,7,8,9,10]), [1,2,3,4,5,6,7,8,9,10])
        self.assertEqual(bubbleSort([61,89,97,2,3,5,7,11,13,17,19,23,29,31,37,41,67,71,73,79,83]), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 61, 67, 71, 73, 79, 83, 89, 97])
        self.assertEqual(bubbleSort([43,47,53,59,61,89,97,2,3,5,7,11,13,17,19,23,29,31,37,41,67,71,73,79,83]), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])


class CountingSortTestCase(unittest.TestCase):

    def test_countingSort(self):
        self.assertEqual(countingSort([1,2,3,4,5,6,7,8,9,10]), [1,2,3,4,5,6,7,8,9,10])
        self.assertEqual(countingSort([61,89,97,2,3,5,7,11,13,17,19,23,29,31,37,41,67,71,73,79,83]), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 61, 67, 71, 73, 79, 83, 89, 97])
        self.assertEqual(countingSort([43,47,53,59,61,89,97,2,3,5,7,11,13,17,19,23,29,31,37,41,67,71,73,79,83]), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])        


class RadixSortTestCase(unittest.TestCase):

    def test_radixSort(self):
        self.assertEqual(radixSort(3, ['FFF', 'AFA', '100', '400', '004', '003', 'BBB', '002', '001', '001', '002', '003', '004', 'AAA', '0AB', '010', '000', 'FF1']), ['000', '001', '001', '002', '002', '003', '003', '004', '004', '010', '0AB', '100', '400', 'AAA', 'AFA', 'BBB', 'FF1', 'FFF'])

if __name__ == '__main__':
    unittest.main() 

