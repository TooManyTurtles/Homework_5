# Завдання 1
# У списку цілих, заповненому випадковими числами обчислити:
# ■ Суму негативних чисел;
# ■ Суму парних чисел;
# ■ Суму непарних чисел;
# ■ Добуток елементів з кратними індексами 3;
# ■ Добуток елементів між мінімальним та максимальним елементом;
# ■ Суму елементів, що знаходяться між першим та останнім позитивними елементами.

# Завдання 2
# Є список цілих, заповнений випадковими числами.
# На підставі даних цього масиву потрібно:
# ■ Створити список цілих, що містить лише парні числа з першого списку;
# ■ Створити список цілих, що містить лише непарні числа з першого списку;
# ■ Створити список цілих, що містить лише негативні числа з першого списку;
# ■ Створити список цілих, що містить лише позитивні числа з першого списку.

# 1
import random
try:
    NUM_SIZE = 10
    numbers = []
    num_summ1, num_summ2, num_summ3, num_summ4, num_summ5,  = 0, 0, 0, 0, 0
    for i in range(NUM_SIZE):
        numbers.append(random.randint(-10, 10))
    print(numbers)

# negative
    for num in numbers:
        if num < 0:
            num_summ1 += num
    print("Суму негативних чисел:", num_summ1)
# pair
    for num in numbers:
        if num % 2 == 0:
            num_summ2 += num
    print("Сума парних чисел:", num_summ2)

# not pair
    for num in numbers:
        if num % 2 != 0:
            num_summ3 += num
    print("Сума непарних чисел:", num_summ3)

# % 3
    for num in numbers:
        if numbers.index(num) % 3 == 0:
            num_summ4 += num
    print("Добуток елементів з кратними індексами 3:", num_summ4)

# min+max
    print(f"Добуток елементів між мінімальним та максимальним елементом:", min(numbers) + max(numbers))

# Суму елементів, що знаходяться між першим та останнім позитивними елементами.
    positive_start = 0
    positive_end = 0
    for num in numbers:
        if num > 0:
            positive_start = numbers.index(num)
            break
    for num in numbers:
        if num > 0:
            positive_end = numbers.index(num)
    for num in range(positive_start, positive_end + 1):
        num_summ5 += numbers[num]
    print("Суму елементів, що знаходяться між першим та останнім позитивними елементами:", num_summ5)

except Exception as e:
    print(e)

# 2


