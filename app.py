def factorial(n):
    if n < 0:
        return "Факториал не определен для отрицательных чисел."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Запрос числа у пользователя
number = int(input("Введите число для вычисления его факториала: "))
print(f"Факториал {number} равен {factorial(number)}.")
