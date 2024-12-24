def calculate_structure_sum(*args):
    numbers = 0
    for item_ in args:
        if isinstance(item_, list):
            numbers += calculate_structure_sum(*item_)
        elif isinstance(item_, dict):
            numbers += calculate_structure_sum(*tuple(item_.items()))
        elif isinstance(item_, tuple):
            numbers += calculate_structure_sum(*item_)
        elif isinstance(item_, str):
            numbers += len(item_)
        elif isinstance(item_, set):
            numbers += calculate_structure_sum(*item_)
        elif isinstance(item_, int):
            numbers += item_
    return numbers

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
