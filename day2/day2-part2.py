def convert_to_ID(sub_ID, num_repeats):
    return int(str(sub_ID) * num_repeats)

def is_inrange(ID, start, end):
    if ID >= start and ID <= end:
        return True, None
    elif ID < start:
        return False, 'lower'
    else:
        return False, 'higher'

def process_range(start, end):
    invalid_IDs = set()
    start_length = len(str(start))
    end_length = len(str(end))

    # Check all possible number lengths in the range
    for num_length in range(start_length, end_length + 1):
        # check all possible pattern lengths
        for pattern_length in range(1, num_length // 2 + 1):
            if num_length % pattern_length == 0:
                num_repeats = num_length // pattern_length
                if num_repeats >= 2:
                    
                    min_sub_ID = 10**(pattern_length - 1)
                    max_sub_ID = 10**pattern_length - 1
                    
                    curr_sub_ID = min_sub_ID
                    while curr_sub_ID <= max_sub_ID:
                        curr_ID = convert_to_ID(curr_sub_ID, num_repeats)
                        res, dir = is_inrange(curr_ID, start, end)
                        if res:
                            if curr_ID not in invalid_IDs:
                                invalid_IDs.add(curr_ID)
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