immutable_var = (1, 2, 'a', 'b', [1, 2, 3])
print(immutable_var)
# immutable_var[0] = 2 - в кортежах нельзя изменить индексные значения,
# если только это не элемент списка внутри кортежа
# например immutable_var[4][0] = 2 выполнится без ошибок и изменит сам список


mutable_list = [0, 2, 'a', 'b', 'Unmodified']
print(mutable_list)
mutable_list[4] = 'Modified'
mutable_list[0] = 1
print(mutable_list)
