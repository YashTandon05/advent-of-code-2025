def process_line(curr_num, line):
    dir, num = str(line[0]), int(line[1:])
    if dir == 'R':
        remainder_sum = (curr_num + (num % 100)) >= 100
        curr_num += num
    elif dir == 'L':
        remainder_sum = ((curr_num - (num % 100)) <= 0) and (curr_num != 0)
        curr_num -= num

    return curr_num % 100, ((abs(num) // 100) + int(remainder_sum))

def main():
    curr_num = 50
    total_zeroes = 0
    
    with open('day1-input.txt', 'r') as file:
        for line in file:
            curr_num, curr_zeroes = process_line(curr_num, line)
            total_zeroes += curr_zeroes
    
    print("Number of Zeroes: ", total_zeroes)

if __name__ == "__main__":
    main()
