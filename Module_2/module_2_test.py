def correct_pass(n):
    if n < 3 or n > 20:
        return print("Число должно быть от 3 до 20!")
    result = ""
    for i in range(1, n):
        for k in range(2, n):
            if k <= i:
                continue
            if n % (i + k) == 0:
                result += str(i) + str(k)
    return print(result)

n = int(input("Введите число от 3 до 20: "))

correct_pass(n)

