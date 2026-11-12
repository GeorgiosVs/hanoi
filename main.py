def hanoi(number, apo, pros, voithitiki):
    if number == 0:
        return
    hanoi( number - 1, apo, voithitiki, pros)
    print(f"Δίσκος {number}: {apo} -> {pros}")
    hanoi(number - 1, voithitiki, pros, apo)

hanoi(5, "Α", "Γ", "Β")