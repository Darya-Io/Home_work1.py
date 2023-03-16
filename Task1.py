# Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

number = int(input('Введите трёхзначное число: '))
digit1 = number % 10
digit2 = number % 100 // 10
digit3 = number // 100
print(digit1 + digit2 + digit3)
