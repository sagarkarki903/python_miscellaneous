import unittest
# import index
# from general import result, checker
from .. import  general
print(f"First: {__name__}")
class TestIndex(unittest.TestCase):
    # def test_print_str(self):
    #     result = index.print_str("Sagar Karki")
    #     self.assertEqual(result, "Sagar Karki")
    #
    # def test_print_int(self):
    #     result = index.print_int(23)
    #     self.assertEqual(result, 23)
    def test_general(self):
        res = general.checker(2)
        self.assertEqual(res, 3)

if __name__ == "__main__":
    print(f"Second: {__name__}")
    unittest.main()

