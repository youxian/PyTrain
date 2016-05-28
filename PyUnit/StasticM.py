#-*- coding:utf-8 -*-

import unittest
import Tested


class  NumAsserTestCase(unittest.TestCase):
	def runTest(self):
		num=1
		self.assertEqual(Tested.NumAssert(num),"num = 0")


if __name__ == '__main__':
	testCase = NumAsserTestCase()
	testCase.runTest()