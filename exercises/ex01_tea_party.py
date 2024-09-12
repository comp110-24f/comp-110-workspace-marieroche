"""Write a Program to Help Plan a Cozy Tea Party"""

__author__ = "730466510"


def main_planner(guests: int) -> None:
    """Amount of Tea and Treats Needed and Total Cost"""
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # remember to change the type of guests
    print(
        "Tea Bags: " + str(tea_bags(people=guests))
    )  # need to call tea_bags/treats within the function, guests can't be the argument
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Number of tea bags needed based on the number of people"""
    return people * 2


tea_bags(people=3)


def treats(people: int) -> int:
    """How many treats to have based on how many teas people are expected to drink"""
    return int(
        tea_bags(people=people) * 1.5
    )  # need to embed tea_bags within the treat function


def cost(tea_count: int, treat_count: int) -> float:
    """Cost of tea bags and treats combined"""
    return (tea_count * 0.5) + (treat_count * 0.75)


cost(tea_count=6, treat_count=9)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
