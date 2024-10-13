
details: str = "michelle from tel aviv"

print('len', len(details))

print('upper', details.upper())

print('lower', details.lower())

print('starts with michelle', details.startswith('michelle'))

print('ends with tel aviv', details.endswith('tel aviv'))

splitted: list[str] = details.split()

stars_michelle = details.replace(' ', '*')
print(details.replace(' ', '*'))
print(stars_michelle)

print('center', details.center(50,'='))

print('4 on', details[4::])

print('until 4', details[:4:])

print('even', details[::2])

print('title', details.title())