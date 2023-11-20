import unittest
from operaciones import sumar, restar, multiplicar, dividir

class TestSumar(unittest.TestCase):
	def testSumar(self):
		self.assertEqual(sumar(3, 2), 5)
		self.assertEqual(sumar(-1, 1), 0)
		self.assertEqual(sumar(-1, -1), -2)

class TestRestar(unittest.TestCase):
	def testRestar(self):
		self.assertEqual(restar(3, 2), 1)
		self.assertEqual(restar(-1, 1), -2)
		self.assertEqual(restar(-1, -1), 0)

class TestMultiplicar(unittest.TestCase):
	def testMultiplicar(self):
		self.assertEqual(multiplicar(3, 2), 6)
		self.assertEqual(multiplicar(-1, 1), -1)
		self.assertEqual(multiplicar(-1, -1), 1)

class TestDividir(unittest.TestCase):
	def testDividir(self):
		self.assertEqual(dividir(3, 2), 3/2)
		self.assertEqual(dividir(-1, 1), -1)
		self.assertEqual(dividir(-1, -1), 1)
		self.assertEqual(dividir(-1, 0), "MATH_ERROR")


if __name__ == "__main__":
	unittest.main()