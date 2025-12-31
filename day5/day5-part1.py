def check_if_fresh(intervals, id):
    for interval in intervals:
        start, end = interval[0], interval[1]
        if id >= start and id <= end:
            return True
    return False

def main():
    intervals = []
    ids_to_check = []
    extract_ids = False
    fresh_count = 0
    
    with open('day5-input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line == '':
                extract_ids = True
                continue
            if extract_ids:
                ids_to_check.append(line)
            else:
                intervals.append([int(line.split('-')[0]), int(line.split('-')[1])])
    
    for id in ids_to_check:
        id = int(id)
        if check_if_fresh(intervals, id):
            fresh_count += 1
        
    print("Number of Fresh IDs: ", fresh_count)

if __name__ == "__main__":
    main()