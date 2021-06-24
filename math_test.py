def foo(number1, number2):
  result = number1 + number2
  return result

def test_foo():
  number_a = 2
  number_b = 3
  result = foo(number_a, number_b)
  assert result == 5

  number_c = 4
  number_d = 2
  result = foo(number_c, number_d)
  assert result == 6

  print("All tests on foo finished")

def test_foo_2():
  number_a = 4
  number_b = -2
  result = foo(number_a,number_b)
  assert result == 2

if __name__ == '__main__':
  # This calls the test_foo function 
  # when we run from the command line
  test_foo()
  test_foo_2()  