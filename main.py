def f(n): 
    sum = 0 
    for i in range(0,(n * 2)+1, 2): 
        sum += i 
    return sum

def test_sum_fun1(self):
    assert f(5) == 30

def test_sum_fun2(self):
    assert f(10) == 110

def test_sum_fun3(self):
    assert f(15) == 240