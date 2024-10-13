import random

bool_list: list[bool] = [random.choice([True, False]) for _ in range(3)]

print('all true?', all(bool_list))

print('any true?', any(bool_list))

print('all false', not all(bool_list))

print('one false at least', not any(bool_list))

five_random: list[int] = [random.randint(-2, 2) for _ in range(5)]
print('5 randoms', five_random)

print('all not zero', all(five_random))

print('any not zero', any(five_random))

print('all zeros', not any(five_random))

print('at least one zero', not all(five_random))