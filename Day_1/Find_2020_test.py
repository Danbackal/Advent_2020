import unittest
import Find_2020


class TestFind_2020(unittest.test):
    def __init__(self):
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
        number_list.write("501")
        number_list.close()
        self.assertEqual(Find_2020.main(self.list_path), -1)

    def testPositiveSuccess(self):
        self.resetList()
        number_list = open(self.list_path, "w")
        number_list.write("501")
        number_list.write("-256")
        number_list.write("2000")
        number_list.write("103")
        number_list.write("20")
        number_list.write("007")
        number_list.close()
        self.assertEqual(Find_2020.main(self.list_path), 40000)

    def testPositiveNegativeSuccess(self):
        self.resetList()
        number_list = open(self.list_path, "w")
        number_list.write("501")
        number_list.write("-980")
        number_list.write("2000")
        number_list.write("103")
        number_list.write("3000")
        number_list.write("007")
        number_list.close()
        self.assertEqual(Find_2020.main(self.list_path), -2940000)

    def testNoSuccess(self):
        self.resetList()
        number_list = open(self.list_path, "w")
        number_list.write("501")
        number_list.write("-980")
        number_list.write("2000")
        number_list.write("103")
        number_list.write("-3000")
        number_list.write("007")
        number_list.close()
        self.assertEqual(Find_2020.main(self.list_path), -1)

    def testNonNumberError(self):
        self.resetList()
        number_list = open(self.list_path, "w")
        number_list.write("501")
        number_list.write("-980")
        number_list.write("2000")
        number_list.write("103")
        number_list.write("3000")
        number_list.write("abc")
        number_list.close()
        self.assertEqual(Find_2020.main(self.list_path), -1)

