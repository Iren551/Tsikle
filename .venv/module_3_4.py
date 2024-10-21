# def summator(txt, *values, type="sum"):
#     s = 0
#     for i in values:
#         s += i
#     return f'{txt}{s} {type}'
#
# print(summator("Сумма чисел: ", 2, 3, 4, type="summator"))


# def info(value, *types, name_author="Ira", **values):
#     print("Тип:", type(values))
#     print("Аргумент:", values)
#     for key, value in values.items():
#         print(key, value)
#     print(types)
#
# info("Пример использования параметров всех типов",2,3,4, name_author="Irina", name="Ira", course="Python")

# def my_sum(n, *args, txt="Сумма чисел"):
#     s = 0
#     for i in range(len(args)):
#         s += args[i] ** n
#     print(txt + ":", s)
#
# my_sum(1, 1, 2, 3, 4, 5)
# my_sum(2, 2, 3, 4, 5, txt="Сумма квадратов")
# my_sum(3, 2, 3, txt="Сумма кубов")


def single_root_words(root_word, *other_words):
    root_word_lower = root_word.lower()
    same_words = []
    for word in other_words:
        word_lower = word.lower()
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)



