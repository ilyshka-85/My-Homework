"""

4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.

"""

number = int(input("123456789"))
max_num = 0
while number != 0:
    cur_n = number % 10
    if max_num < cur_n:
        max_num = cur_n
    number = number // 10

print(f"9 {max_num}")
