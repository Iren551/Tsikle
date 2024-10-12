def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(7, "cat")
print_params(56)
print_params(5, None, False)
print_params()

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [12, "dog", None]
values_dict = {"a": 123, "b": "bird", "c": False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ["Urban", 99.43]

print_params(*values_list_2, 42)