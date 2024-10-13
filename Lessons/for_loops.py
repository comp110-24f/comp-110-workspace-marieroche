"""Practice with for loops"""

pets: list[str] = ["Louie", "Bo", "Bear"]
# tell every pet they're a good boy
for elem in pets:
    print(f"Good boy, {elem}!")

"""Range practice"""

names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0, len(names)):
    # print(str(idx) + ": " + names[idx])
    print(f"{idx}: {names[idx]}")
