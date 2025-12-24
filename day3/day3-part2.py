NUM_BATTERIES = 12

def calculate_joltage(sub_line, k):
    if k == 1:
        return max([int(num) for num in sub_line])

    max_digit = 1
    max_digit_index = 0

    for i, num in enumerate(sub_line[:-k + 1]):
        num = int(num)
        if num > max_digit:
            max_digit = num
            max_digit_index = i
    
    return max_digit * 10**(k-1) + calculate_joltage(sub_line[max_digit_index + 1:], k-1)
        
            

def main():
    joltage_sum = 0

    with open('day3-input.txt', 'r') as file:
        for line in file:
            joltage = calculate_joltage(line.strip(), NUM_BATTERIES)
            print(joltage)
            joltage_sum += joltage

    print("Total Output Joltage: ", joltage_sum)

if __name__ == "__main__":
    main()