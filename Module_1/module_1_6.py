my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print("Dictionary:", my_dict)
print("Existing value:", my_dict['Masha'])
print("Not existing value:", my_dict.get('Dmitrii'))
my_dict.update({'Kamila': 1981, 'Artem': 1972})
deleted_value = my_dict.pop('Egor')
print("Deleted Value:", deleted_value)
print("Modified dictionary:", my_dict)



my_set = {1, 'Строка', 4.75, 3, 4.75, 'Строка', 3, 1}
print("Set:", my_set)
my_set.add('Яблоко')
my_set.add(5)
my_set.remove('Строка')
print("Modified Set:", my_set)
