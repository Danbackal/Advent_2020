import unittest
import Find_2020


class TestFind_2020(unittest.TestCase):
    def setUp(self):
        # create/clear a txt file for testing
        self.list_path = "C:\\Users\\Backal\\Python_tests\\2020_list.txt"

    def resetList(self):
        number_list = open(self.list_path, "w")
        number_list.close()

    def testEmptyList(self):
        # -1 will be response for errors, since it will return an integer
        # and the result will always be much higher/lower
        self.resetList()
        self.assertEqual(Find_2020.main(self.list_path), -1)

    def testOneItemList(self):
        self.resetList()
        number_list = open(self.list_path, "w")
        number_list.write("501\n")
        number_list.close()
        self.assertEqual(Find_2020.main(self.list_path), -1)

    def testPositiveSuccess(self):
        self.resetList()
        number_list = open(self.list_path, "w")
        number_list.write("501\n")
        number_list.write("-256\n")
        number_list.write("2000\n")
        number_list.write("103\n")
        number_list.write("20\n")
        number_list.write("007\n")
        number_list.close()
        self.assertEqual(Find_2020.main(self.list_path), 40000)

    def testPositiveNegativeSuccess(self):
        self.resetList()
        number_list = open(self.list_path, "w")
        number_list.write("501\n")
        number_list.write("-980\n")
        number_list.write("2000\n")
        number_list.write("103\n")
        number_list.write("3000\n")
        number_list.write("007\n")
        number_list.close()
        self.assertEqual(Find_2020.main(self.list_path), -2940000)

    def testNoSuccess(self):
        self.resetList()
        number_list = open(self.list_path, "w")
        number_list.write("501\n")
        number_list.write("-980\n")
        number_list.write("2000\n")
        number_list.write("103\n")
        number_list.write("-3000\n")
        number_list.write("007\n")
        number_list.close()
        self.assertEqual(Find_2020.main(self.list_path), -1)

    def testNonNumberError(self):
        self.resetList()
        number_list = open(self.list_path, "w")
        number_list.write("501\n")
        number_list.write("-980\n")
        number_list.write("2000\n")
        number_list.write("103\n")
        number_list.write("3000\n")
        number_list.write("abc\n")
        number_list.close()
        self.assertEqual(Find_2020.main(self.list_path), -1)

