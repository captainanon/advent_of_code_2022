from aocd import get_data
data = [int(x) for x in get_data(day=1, year=2021).split('\n')]
print(data)