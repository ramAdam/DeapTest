import unittest
from hypothesis import given
import hypothesis.strategies as st
from hypothesis.strategies import lists, sets, composite
from util import allDuplicates, occurence, Frequency
import hypothesis
import pdb


class TestUtility(unittest.TestCase):
    def setUp(self):
        self.elements = Frequency([4, 3, 4, 3, 2, 1])
        self.singleElement = Frequency([1])
        self.emptylist = Frequency([])
        self.twodup = Frequency([1, 1])
        self.twoUnique = Frequency([1, 2])
        self.allUnique = Frequency([4, 3, 2, 1, 0])

    @composite
    def listOfUniqueIntegrs(
        draw,
        elements=st.integers(min_value=1, max_value=10),
    ):
        xs = draw(lists(elements, max_size=5, min_size=5, unique=True))
        return xs

    @composite
    def listOfIntegers(draw, elements=st.integers(min_value=1, max_value=10)):
        ls = draw(lists(elements, max_size=6, unique=False))
        return ls

    @given(x=listOfIntegers())
    def testListOfIntegersOfVariableLength(self, x):
        e = Frequency(x)
        self.assertEqual(len(e.ind), len(x))

    @given(x=listOfUniqueIntegrs())
    def testallDuplicates(self, x):
        assert not allDuplicates(x)

    def testTwoDuplicates(self):
        self.assertEqual(self.twodup[1], 2)

    def testTwoUniqueElements(self):
        self.assertEqual(self.twoUnique[1], 1)
        self.assertEqual(self.twoUnique[2], 1)

    def testFrequency(self):
        assert self.elements[4] == 2
        assert self.elements[3] == 2
        assert self.elements[2] == 1
        assert self.elements[1] == 1
        assert self.singleElement[1] == 1

    def testGetItem(self):
        assert self.elements[3] == 2

    def testKeyError(self):
        with self.assertRaises(KeyError):
            self.emptylist[1]

    def testAnyDuplicates(self):
        self.assertEqual(self.twodup[1], 2)
        self.assertTrue(self.twodup.anyDuplicates())

        self.assertFalse(self.twoUnique.anyDuplicates())

    def testAreAllUnique(self):
        self.assertTrue(self.twoUnique.areAllUnique())
        self.assertTrue(self.allUnique.areAllUnique())
        self.assertFalse(self.elements.areAllUnique())

    def tearDown(self):
        del self.elements
        del self.emptylist
        del self.singleElement
        del self.twoUnique
        del self.twodup
        del self.allUnique