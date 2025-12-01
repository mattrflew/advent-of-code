# Read input
with open("input.txt", "r") as f:
    instructions = [line.strip() for line in f]


# --------------------
# Part 1
# --------------------
position = 50 # starting position
cnt_p1 = 0

for rotation in instructions:
    # Parse the direction and magnitude from instructions
    direction = rotation[0]
    move = int(rotation[1:])
    if direction == "L":
        move = -move
        
    # Perform the move
    position += move
    
    # Adjust position to be on the number wheel
    position = position % 100 
    
    # Check if landed on zero
    if position == 0:
        cnt_p1 += 1

print(f"Part 1: {cnt_p1}")

# --------------------
# Part 2
# --------------------
position = 50
cnt_p2 = 0

for rotation in instructions:
    # Parse the direction and magnitude from instructions
    direction = rotation[0]
    move = int(rotation[1:])
    if direction == "L":
        move = -move
    
    # Intermediate steps
    last_position = position
    temp_position = last_position + move
    
    # Count number of crosses or lands on zero in the range (the number of multiples of 100)
    if move > 0:
        # Move to the right
        # Number is within range (last_position, temp_position]
        hits = temp_position // 100 - last_position // 100
        
    else:
        # Move to the left
        # Number is within range [temp_position, last_position)
        hits = (last_position - 1) // 100 - (temp_position - 1) // 100

    # Add to counter
    cnt_p2 += hits
    
    # Adjust position to be on the number wheel
    position = temp_position % 100

print(f"Part 2: {cnt_p2}")