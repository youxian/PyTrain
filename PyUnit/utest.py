#-*- coding:utf-8 -*-

from ut_target import SplitZero, EqualToZero
import unittest

# unittest基本使用方法
# 1.import unittest
# 2.定义一个继承自unittest.TestCase的测试用例类
# 3.定义setUp和tearDown，在每个测试用例前后做一些辅助工作。
# 4.定义测试用例，名字以test开头。
# 5.一个测试用例应该只测试一个方面，测试目的和测试内容应很明确。主要是调用assertEqual、assertRaises等断言方法判断程序执行结果和预期值是否相符。
# 6.调用unittest.main()启动测试
# 7.如果测试未通过，会输出相应的错误提示。如果测试全部通过则不显示任何东西，这时可以添加-v参数显示详细信息。
class SzTestCase(unittest.TestCase):

	def setUp(self):
		print "test start"
	def  tearDown(self):
		print "test finish"

	def testSzBig(self):
		num=10
		sz = SplitZero()
		self.assertEqual(sz.splitzero(num), "num is bigger than zero")

	def testSzSmall(self):  
	 	num = -10
	 	sz = SplitZero()
	 	self.assertEqual(sz.splitzero(num), "num is smaller than zero")


	def testSzEqual(self):
		num = 0
		sz = SplitZero()
		self.assertRaises(EqualToZero, sz.splitzero, num)
 
if __name__ == "__main__":
	unittest.main()