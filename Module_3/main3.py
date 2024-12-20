def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(b = 25) # выполняется с предупреждениями о замене типа
print_params(c = [1,2,3]) # выполняется с предупреждениями о замене типа

values_list = [2, "string", False]
values_dict = {'a': 3, 'b': 'stroka', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
