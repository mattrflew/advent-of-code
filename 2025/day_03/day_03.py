# https://adventofcode.com/2025/day/3

# Read input
with open("input.txt", "r") as f:
    banks = [line.strip() for line in f]

# --------------------
# Part 1
# --------------------
joltages = []

for bank in banks:
    values = [int(num) for num in list(bank)]
    max_value = max(values[:-1])
    idx_max_value = values[:-1].index(max_value)
    second_digit = max(values[idx_max_value+1:])

    joltage = int(str(max_value) + str(second_digit))    
    joltages.append(joltage)


print(f"Part 1: {sum(joltages)}")


# --------------------
# Part 2
# --------------------
def get_joltage(bank_str, num_batteries):
    num_in_bank = len(bank_str)

    bank_values = [int(n) for n in bank_str]
    idx_list = list(range(num_in_bank))

    joltage = ''
    split_idx = -1
    
    # Loop and try to find each digit
    for i in range(num_batteries):
        num_digits_remaining = num_batteries - (i+1)
        
        # Special case for last digit
        if i == (num_batteries - 1):
            temp_values = bank_values[(split_idx+1):]
            temp_idx_list = idx_list[(split_idx+1):]
        else:
            temp_values = bank_values[(split_idx+1):-num_digits_remaining]
            temp_idx_list = idx_list[(split_idx+1):-num_digits_remaining]
        
        max_value = max(temp_values)
        idx_max_loc = temp_values.index(max_value)
        split_idx = idx_list[temp_idx_list[idx_max_loc]]
        
        joltage += str(max_value)

    return int(joltage)


joltages = []
num_batteries = 12

for bank in banks:
    joltage = get_joltage(bank, num_batteries)
    joltages.append(joltage)

print(f"Part 2: {sum(joltages)}")
