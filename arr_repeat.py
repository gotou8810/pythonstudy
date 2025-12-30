def print_names(l):
    for index,name in enumerate(l,start=1):
        print(f'{index}. {name}')

print_names(['上田', '田仲', '堀田'])

def square(l):
    return list(map(lambda x:x**2, l))

squared_numbers = square([5, 7, 10])
print(squared_numbers)

def select_even_numbers(l):
    return list (filter(lambda x:x%2==0, l))

even_numbers = select_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(even_numbers)