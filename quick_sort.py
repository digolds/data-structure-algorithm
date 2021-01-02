def quick_sort(data, start, end):
    if start >= end:
        return

    c_index = start
    i = start
    j = end
    while True:
        while i < j:
            if data[i] > data[c_index]:
                break
            i += 1
        
        while i < j:
            if data[j] <= data[c_index]:
                break
            j -= 1
        
        if i >= j:
            break
        else:
            data[i], data[j] = data[j], data[i]
            i += 1
            j -= 1
    if data[c_index] > data[i]:
        data[c_index], data[i] = data[i], data[c_index]
    
    quick_sort(data, start, i - 1)
    quick_sort(data, i + 1, end)


if __name__ == '__main__':
    data = [3,3,6,1,-1,9,8,4,4]
    quick_sort(data, 0, len(data) - 1)
    print(data)