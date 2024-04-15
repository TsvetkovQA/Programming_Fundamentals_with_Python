fire_cells_input = input().split("#")
water = int(input())

valid_cells = []
total_effort = 0

for cell_info in fire_cells_input:
    cell_data = cell_info.split(" = ")
    fire_type = cell_data[0]
    cell_value = int(cell_data[1])

    if (fire_type == "High" and 81 <= cell_value <= 125) or \
       (fire_type == "Medium" and 51 <= cell_value <= 80) or \
       (fire_type == "Low" and 1 <= cell_value <= 50):
        if water >= cell_value:
            valid_cells.append(cell_value)
            total_effort += cell_value * 0.25
            water -= cell_value

print("Cells:")
for cell in valid_cells:
    print(f" - {cell}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {sum(valid_cells)}")
