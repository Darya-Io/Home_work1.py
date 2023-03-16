# Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

volue = int(input('Введите трёхзначное число: '))
number1 = volue % 10
number2 = volue % 100 // 10
number3 = volue // 100
print(number1 + number2 + number3)
