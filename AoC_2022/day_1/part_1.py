with open("day_1/input.txt", "r") as f:
    #part 1
    calories_per_elf = [calorie.split("\n") for calorie in f.read().split("\n\n")]
    max_calories = max([sum(map(int,elf)) for elf in calories_per_elf])
    #part 2
    maxes = []
    total_calories = [sum(map(int,elf)) for elf in calories_per_elf]
    for i in range(3):
        current_max = max(total_calories)
        maxes.append(current_max)
        total_calories.remove(current_max)
    top_three_calories = sum(maxes)
    
    print(max_calories, top_three_calories)
