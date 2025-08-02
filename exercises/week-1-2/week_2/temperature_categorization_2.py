temp_input = float(input("Enter the temperature: "))
if temp_input < 10:
    print("Cold")
elif 10 <= temp_input <= 25:
    print("Mild")
else:
    print("High")