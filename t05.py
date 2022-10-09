length = float(input('Foundation length (m): '))
width = float(input('Foundation width (m): '))
foundation_height = float(input('Foundation height (m): '))
wall_height = float(input('height (m): '))
concrete_price = float(input('Cost of concrete ($/m^3): '))
brick_price = float(input('of bricks ($/m^2): '))

concrete_needed = length * width * foundation_height
concrete_cost = concrete_needed * concrete_price
bricks_needed = 2 * (width * wall_height) + 2 * (length * wall_height)
bricks_cost = bricks_needed * brick_price
total_cost = bricks_cost + concrete_cost

print()
print(f"Concrete needed for foundation (m^3): {concrete_needed:,.2f}")
print(f"Cost of concrete: ${concrete_cost:,.2f}")
print(f"Bricks needed for walls (m^2): {bricks_needed:,.2f}")
print(f"Cost of bricks: ${bricks_cost:,.2f}")
print(f"Total cost: ${total_cost:,.2f}")
