inputs  = [line.strip() for line in open('input.txt')]

calories = []

for elf_calories in '\n'.join(inputs).split('\n\n'):
    calories_for_elf = 0
    for elf_calory in elf_calories.split('\n'):
        calories_for_elf += int(elf_calory)
    calories.append(calories_for_elf)

calories = sorted(calories, reverse=True)
max_calories = calories[0]
max_three_calories = sum(calories[0:3])

print(max_calories)
print(max_three_calories)