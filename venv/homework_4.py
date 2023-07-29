# while True:
#     word = input("Введите слово с буквой 'о': ")
#     if 'о' in word.lower():
#         print("Спасибо, слово содержит букву 'о'.")
#         break
#     else:
#         print("Слово не содержит букву 'о'. Попробуйте еще раз.")


# lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum',"Loren Koen",469,"I love hillel"]
# lst2 = []
#
# for item in lst1:
#     if type(item) == str:
#         lst2.append(item)
# print(lst2)

lst1 = [1,2,2,4,5,6,9,9,48,48,12,14,14,85,62,328,841,45,963,4521,8556,22,155,22,118,4521]
lst2 = []
summ = 0
for item in lst1:
    if item %2 == 0:
        summ += item
        lst2.append(item)

print("Сумма всех парных чисел:",summ)
print("Вывод всех парных чисел:",lst2)
