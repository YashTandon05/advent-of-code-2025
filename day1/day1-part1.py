def process_line(curr_num, line):
    dir, num = str(line[0]), int(line[1:])
    if dir == 'R':
        curr_num += num
    elif dir == 'L':
        curr_num -= num
    return curr_num % 100

def main():
    curr_num = 50
    curr_zeroes = 0
    
    with open('day1-input.txt', 'r') as file:
        for line in file:
            curr_num = process_line(curr_num, line)
            if curr_num == 0:
                curr_zeroes += 1
    
    print("Number of Zeroes: ", curr_zeroes)

if __name__ == "__main__":
    main()

