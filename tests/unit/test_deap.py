import unittest
from hypothesis import given
import hypothesis.strategies as st
from hypothesis.strategies import lists, sets, composite
from util import allDuplicates, occurence
import hypothesis
import pdb


class TestUtilityFunctions(unittest.TestCase):
    def setUp(self):
        pass

    @composite
    def listOfUniqueIntegrs(
        draw,
        elements=st.integers(min_value=1, max_value=10),
    ):
        xs = draw(lists(elements, max_size=5, min_size=5, unique=True))
        return xs

    @given(x=listOfUniqueIntegrs())
    def testallDuplicates(self, x):
        assert not allDuplicates(x)