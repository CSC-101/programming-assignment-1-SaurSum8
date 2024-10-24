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
    def test_books_by_author_1(self):
        b0 = data.Book(['Leshy', 'Grimora', 'Magnifus', 'P03'], "Inscryption")
        b1 = data.Book(['Leshy'], "The Scrybe Of Beasts")
        b2 = data.Book(['Luke', 'Dealer'], "Buckshot Roulette")

        inp = [b0, b1, b2]
        expected = [b0, b1]
        actual = hw1.books_by_author("Leshy", inp)
        self.assertEqual(actual, expected)

    def test_books_by_author_2(self):
        b0 = data.Book(['Leshy', 'Grimora', 'Magnifus', 'P03'], "Inscryption")
        b1 = data.Book(['Leshy'], "The Scrybe Of Beasts")
        b2 = data.Book(['Luke', 'Dealer'], "Buckshot Roulette")

        inp = [b0, b1, b2]
        expected = []
        actual = hw1.books_by_author("Golly", inp)
        self.assertEqual(actual, expected)

    # Part 7
    def test_circle_bound_1(self):
        pL = data.Point(0, 0)
        pR = data.Point(6, 8)

        pC = data.Point(3.0, 4.0)
        inp = data.Rectangle(pL, pR)

        expected = data.Circle(pC, 5.0)
        actual = hw1.circle_bound(inp)
        self.assertEqual(actual, expected)

    def test_circle_bound_2(self):
        pL = data.Point(0, 0)
        pR = data.Point(0, 0)

        pC = data.Point(0, 0)
        inp = data.Rectangle(pL, pR)

        expected = data.Circle(pC, 0.0)
        actual = hw1.circle_bound(inp)
        self.assertEqual(actual, expected)

    # Part 8
    def test_below_pay_average_1(self):
        e0 = data.Employee("Leshy", 100)
        e1 = data.Employee("P03", 999)
        e2 = data.Employee("Dealer", 700)
        e3 = data.Employee("Grimora", 250)
        e4 = data.Employee("Magnifus", 50)

        inp = [e0,e1,e2,e3,e4]
        expected = ["Leshy", "Grimora", "Magnifus"]
        actual = hw1.below_pay_average(inp)

        self.assertEqual(actual, expected)

    def test_below_pay_average_2(self):
        inp = []
        expected = []
        actual = hw1.below_pay_average(inp)

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
