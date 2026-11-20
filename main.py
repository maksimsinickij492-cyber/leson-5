# 1. try-except
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Не можна ділити на нуль!")


# 2. ValueError
try:
    number = int(input("Введіть число: "))
except ValueError:
    print("Потрібно ввести число!")


# 3. TypeError
try:
    print("10" + 5)
except TypeError:
    print("Помилка типу даних!")


# 4. IndexError
try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("Такого індексу немає!")


# 5. finally
try:
    print(10 / 2)
except ZeroDivisionError:
    print("Помилка!")
finally:
    print("Програма завершена.")


# 6. raise
age = -5

if age < 0:
    raise ValueError("Вік не може бути від'ємним!")
