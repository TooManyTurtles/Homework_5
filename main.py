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


import random
try:
    NUM_SIZE = 10
    numbers = []
    num_summ1, num_summ2, num_summ3, num_summ4, num_summ5,  = 0, 0, 0, 0, 0
    for i in range(NUM_SIZE):
        numbers.append(random.randint(-10, 10))
    print(numbers)

# 1
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
    print("Сума елементів, що знаходяться між першим та останнім позитивними елементами:", num_summ5)

# 2
#
# Створити список цілих, що містить лише парні числа з першого списку;

    pairs_count = []
    for num in numbers:
        count = 0
        for x in numbers:
            if x == num:
                count += 1
        pairs_count.append(count)
    pairs_set = []
    not_pairs_set = []
    index = 0
    while index < NUM_SIZE:
        if pairs_count[index] != 1:
            pairs_set.append(numbers[index])
        elif pairs_count[index] == 1:
            not_pairs_set.append(numbers[index])
        index += 1
    print("Створити список цілих, що містить лише парні числа з першого списку: ", pairs_set)
    print("Створити список цілих, що містить лише непарні числа з першого списку: ", not_pairs_set)

# Створити список цілих, що містить лише непарні числа з першого списку;

    # pairs_count_1 = []
    # for num in numbers:
    #     count = 0
    #     for x in numbers:
    #         if x == num:
    #             count += 1
    #     pairs_count_1.append(count)
    # not_pairs_set = []
    # index = 0
    # while index < NUM_SIZE:
    #     if pairs_count_1[index] == 1:
    #         not_pairs_set.append(numbers[index])
    #     index += 1
    # print("Створити список цілих, що містить лише непарні числа з першого списку: ", not_pairs_set)

# Створити список цілих, що містить лише негативні числа з першого списку;
# Створити список цілих, що містить лише позитивні числа з першого списку

    pos_num = []
    neg_num = []
    for num in numbers:
        if num < 0:
            neg_num.append(num)
        elif num > 0:
            pos_num.append(num)
    print("Створити список цілих, що містить лише негативні числа з першого списку: ", neg_num)
    print("Створити список цілих, що містить лише позитивні числа з першого списку.:", pos_num)

except Exception as e:
    print(e)



