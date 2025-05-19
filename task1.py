# Часть 1: Алгоритмы
# Синтаксис Python и структуры данных

# Напишите программу на Python, которая выполняет следующие задачи:
# • Читает список чисел от пользователя и выводит только четные числа.
# • Находит и выводит максимальное и минимальное число из списка.
# • Сортирует список в порядке возрастания без использования встроенной функции sorted().
# Пример ввода: 1, 3, 4, 7, 8, 10
# Пример вывода:
# Четные числа: [4, 8, 10]
# Максимальное число: 10
# Минимальное число: 1
# Отсортированный список: [1, 3, 4, 7, 8, 10]


# Чтение списка чисел от пользователя
input_str = input("Введите список чисел через запятую: ")
numbers = [int(num.strip()) for num in input_str.split(",")]

# Отбор чётных чисел
even_numbers = [num for num in numbers if num % 2 == 0]

# Поиск максимального и минимального числа
maximum = numbers[0]
minimum = numbers[0]

for num in numbers[1:]:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

# Сортировка списка без использования sorted()
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Меняем элементы местами
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

sorted_numbers = bubble_sort(numbers.copy())

# Вывод результатов
print("Четные числа:", even_numbers)
print("Максимальное число:", maximum)
print("Минимальное число:", minimum)
print("Отсортированный список:", sorted_numbers)
