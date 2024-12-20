import unittest

def f(n): 
    sum = 0 
    for i in range(0,(n * 2)+1, 2): 
        sum += i 
    return sum

print(f(5))

class TestAddFunction(unittest.TestCase):
    def test_sum_fun1(self):
        self.assertEqual(f(5), 30)

    def test_sum_fun2(self):
        self.assertEqual(f(10), 110)

    def test_sum_fun3(self):
        self.assertEqual(f(15), 240)

if __name__ == '__main__':
    unittest.main()