def calculate_joltage(line):
    max_tens_digit = 1
    max_ones_digit = 1

    for i, num in enumerate(line):
        num = int(num)
        if (num > max_tens_digit) and (i != len(line) - 1):
            max_tens_digit = num
            max_ones_digit = 1
        elif num > max_ones_digit:
            max_ones_digit = num
    
    return max_tens_digit * 10 + max_ones_digit
            

def main():
    joltage_sum = 0

    with open('day3-input.txt', 'r') as file:
        for line in file:
            joltage = calculate_joltage(line.strip())
            print(joltage)
            joltage_sum += joltage

    print("Total Output Joltage: ", joltage_sum)

if __name__ == "__main__":
    main()