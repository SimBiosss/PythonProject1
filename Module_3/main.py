calls = 0

def string_info(string):
    len_string = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    tuple_ = (len_string, upper_case, lower_case)
    count_calls()
    return tuple_

def is_contains(string, list_to_search):
    if string.lower() in (items.lower() for items in list_to_search):
        count_calls()
        return True
    else:
        count_calls()
        return False

def count_calls():
    global calls
    calls += 1

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
