def convert_to_ID(sub_ID):
    return int(str(sub_ID) + str(sub_ID))

def is_inrange(sub_ID, start, end):
    ID = convert_to_ID(sub_ID)
    if ID >= start and ID <= end:
        return True, None
    elif ID < start:
        return False, 'lower'
    else:
        return False, 'higher'

def process_range(start, end):
    invalid_IDs = []
    start_length = len(str(start))
    end_length = len(str(end))

    possible_lengths = [(l//2) for l in range(start_length, end_length + 1) if l % 2 == 0]

    for length in possible_lengths:
        curr_sub_ID = 10**(length-1)
        while True:
            res, dir = is_inrange(curr_sub_ID, start, end)
            if res:
                invalid_IDs.append(convert_to_ID(curr_sub_ID))
                curr_sub_ID += 1
            else:
                if dir == 'lower':
                    curr_sub_ID += 1
                elif dir == 'higher':
                    break

    return invalid_IDs

def main():
    ID_sum = 0
    with open('day2-input.txt', 'r') as file:
        content = file.read()
        ranges = list(content.strip().split(','))
        
        for r in ranges:
            start, end = r.split('-')
            ID_sum += sum(process_range(int(start), int(end)))

    print("ID Sum: ", ID_sum)

if __name__ == "__main__":
    main()