temperature_data = [2.4, 6.7, 45, 67, 23.4, 22.1, 21.8, 24.0, 23.9, 22.5, 21.7, 32.5, 30.0, 29.8]

# Categorizing temperatures
for temp in temperature_data:
    if temp < 10:
        print("Cold")
    elif 10 <= temp <= 25:
        print("Mild")
    else:
        print("High")

"""
Rather that using else, you can use an additional 
condition to categorize temperatures as "High" if they are above 25 degrees.
"""

# Categorizing temperatures
for temp in temperature_data:
    if temp < 10:
        print("Cold")
    elif 10 <= temp <= 25:
        print("Mild")
    elif temp > 25:
        print("High")
