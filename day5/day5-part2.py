def merge_intervals(intervals):
    sorted_intervals = sorted(intervals, key=lambda x:x[0])
    merged_intervals = []

    for i, interval in enumerate(sorted_intervals):
        start, end = interval[0], interval[1]

        if i == 0:
            merged_intervals.append([start, end])
            continue
        
        prev_start, prev_end = merged_intervals[-1][0], merged_intervals[-1][1]
        if prev_end >= start:
            merged_intervals[-1][1] = max(prev_end, end)
        else:
            merged_intervals.append([start, end])
        
    return merged_intervals

def count_total(start, end):
    return end-start + 1

def main():
    intervals = []
    all_id_count = 0
    
    with open('day5-input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line == '':
                break
            else:
                intervals.append([int(line.split('-')[0]), int(line.split('-')[1])])
    
    merged_intervals = merge_intervals(intervals)
    for interval in merged_intervals:
        all_id_count += count_total(interval[0], interval[1])
        
    print("Number of Fresh IDs: ", all_id_count)

if __name__ == "__main__":
    main()