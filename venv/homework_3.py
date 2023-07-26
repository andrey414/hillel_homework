test_string = input(str("Введите строку: "))
lengs_string= len(set(test_string))
if lengs_string>10:
    print(True)
else: print(False)