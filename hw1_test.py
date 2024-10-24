import data
import hw1
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count_1(self):
        inp = "hellohi"
        expected = 3
        actual = hw1.vowel_count(inp)
        self.assertEqual(actual, expected)

    def test_vowel_count_2(self):
        inp = "HOWDY"
        expected = 1
        actual = hw1.vowel_count(inp)
        self.assertEqual(actual, expected)

    # Part 2
    def test_short_lists_1(self):
        inp = [[1,2,3,4,5],[0,1],[0],[1,1,1,1],[3,4]]
        expected = [[0,1],[3,4]]
        actual = hw1.short_lists(inp)
        self.assertEqual(actual, expected)

    def test_short_lists_2(self):
        inp = []
        expected = []
        actual = hw1.short_lists(inp)
        self.assertEqual(actual, expected)

    # Part 3
    def test_ascending_pairs_1(self):
        inp = [[1,2,3,4,5],[0,1],[0],[1,1,1,1],[4,3],[-5,-7]]
        expected = [[1,2,3,4,5],[0,1],[0],[1,1,1,1],[3,4],[-7,-5]]
        actual = hw1.ascending_pairs(inp)
        self.assertEqual(actual, expected)

    def test_ascending_pairs_2(self):
        inp = [[]]
        expected = [[]]
        actual = hw1.ascending_pairs(inp)
        self.assertEqual(actual, expected)

    # Part 4
    def test_add_prices_1(self):
        inp1 = data.Price(5, 99)
        inp2 = data.Price(7, 55)
        expected = data.Price(13, 54)
        actual = hw1.add_prices(inp1, inp2)
        self.assertEqual(actual, expected)

    def test_add_prices_2(self):
        inp1 = data.Price(52, 80)
        inp2 = data.Price(8, 19)
        expected = data.Price(60, 99)
        actual = hw1.add_prices(inp1, inp2)
        self.assertEqual(actual, expected)

    # Part 5
    def test_rectangle_area_1(self):
        pL = data.Point(0,0)
        pR = data.Point(5, 7)

        inp = data.Rectangle(pL, pR)
        expected = 35.0
        actual = hw1.rectangle_area(inp)
        self.assertEqual(actual, expected)

    def test_rectangle_area_2(self):
        pL = data.Point(-3,-5)
        pR = data.Point(0, 5)

        inp = data.Rectangle(pL, pR)
        expected = 30.0
        actual = hw1.rectangle_area(inp)
        self.assertEqual(actual, expected)

    # Part 6



    # Part 7


    # Part 8





if __name__ == '__main__':
    unittest.main()
