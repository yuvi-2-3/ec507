def growth_rate(current, previous):
    if previous == 0:
        return None
    return (current - previous) / previous * 100

print(growth_rate(120, 100))  # Example usage