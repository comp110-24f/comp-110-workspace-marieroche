"""Basic syntax of lists"""

names: list[str]

my_numbers: list[float] = list()  # constructor
my_numbers: list[float] = []  # literal

# add an item to the list
my_numbers.append(1.5)
my_numbers.append(1.5)

print(my_numbers)

# create an already populated list
game_points: list[int] = [102, 86, 94]

# subscription notation/indexing
print(game_points[2])

game_points[1] = 72
print(len(game_points))
y: int = len(game_points)
# print(y) stores y as a variable

game_points.pop(1)
print(game_points)

# write a function called display
# input: list[int]
# rv: none
# loop over the input and print every value
# try calling it on game_points


def display(value: list[int]) -> None:
    idx: int = 0
    while idx < len(value):
        print(value[idx])
        idx += 1


display(value=game_points)
