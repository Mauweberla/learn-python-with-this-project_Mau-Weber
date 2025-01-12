print("Welcome to the Building Material Cost Estimator")

# Room dimensions:
length = float(input("Enter the length"))
width = float(input("Enter the width"))

# Room area:
area = length * width
print(f"\nThe total area of the room is {area} m2\n")

# Material list:
print("Choose a material:")
print("1. Wood: $10")
print("2. Porcelain: $15")
print("3. Brick: $8")
print("4. Concrete: $18")
print("5. Metal: $25")

choice = int(input("Enter your material choice (1/2/3/4/5):"))

# Cost per material m2:
if choice == 1:
    material = "Wood"
    cost = 10
elif choice == 2:
    material = "Porcelain"
    cost = 15
elif choice == 3:
    material = "Brick"
    cost = 8
elif choice == 4:
    material = "Concrete"
    cost = 18
elif choice == 5:
    material = "Metal"
    cost = 25
else:
    print("Invalid choice! Please restart the program.")
    exit()

print(f"\nYou chose {material} costing ${cost} per m2")

# Total cost:
total_cost = area * cost
print(f"The total cost for the floor is: ${total_cost}\n")

# Material waste:
waste_percentage = float(input("Enter the percentage of material waste"))
waste_area = area * (waste_percentage / 100)
total_waste_area= area + waste_area
print(f"With {waste_percentage}{total_waste_area} m2\n")

# Save project details:
save = input("Do you want to save this project? (yes/no): ").strip().lower()

if save == "yes":
    project_details = (
        f"Room Dimensions: {length}x{width} m\n"
        f"Room area: {area} m2\n"
        f"Flooring material: {material} (${cost} per m2)\n"
        f"Total cost: ${total_cost}\n"
        f"Material waste: ${waste_percentage}% waste, the total area to be covered is {total_waste_area} m2\n"
    )
    
    with open("Project details_Mau Weber.txt", "a") as file:
        file.write(project_details)
    print("Project saved in: Project details_Mau Weber")

print("\nThank you for using the estimator!")