def time(s):
    h = s//3600
    m = (s%3600)//60
    s -= 3600 * h + 60 * m
    print(f'{h}:{m}:{s}')

time(4550)