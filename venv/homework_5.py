def test_funk(first_arg, second_arg):

    if isinstance(first_arg, int) and isinstance(second_arg, int):
        return first_arg * second_arg
    elif type(first_arg)== str and type(second_arg) == str:
        return first_arg + second_arg
    else:
        return (first_arg, second_arg,)

result = test_funk(10,28)
print("Результат: ", result)
result = test_funk("abv","acg")
print("Результат: ", result)
result = test_funk(1.1,2.1)
print("Результат: ", result)
