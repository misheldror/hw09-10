
l1: list[str] = [  fun-day  ]
print('strip', l1.strip())

print('hello'.isalpha())

print('777'.isdigit())

print(' '.isspace())

ninja_str: list[str] = ['N', 'I', 'N', 'J', 'A']
print(''.join(ninja_str))

print(' * '.join(ninja_str))

print("'e'.upper() in 'hElLo'.upeer()", 'e'.upper() in 'hElLo'.upper())

word: str = "P3ython12"
fixed_str: list[str] = [char.upper() for char in word if not char.isdigit()]
print(fixed_str)
word_again = ''.join(fixed_str)
print(word_again)
