def f(n): 
    sum = 0 
    for i in range(0,(n * 2)+1, 2): 
        sum += i 
    return sum

def test_sum_fun_1():
    assert f(5)==30

def test_sum_fun_2():
    assert f(10)==110

def test_sum_fun_3():
    assert f(15)==240