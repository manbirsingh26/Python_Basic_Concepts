def mean_finder():
    raw_input = list(map(int, input("Enter the list of data: ").split()))
    addition = 0
    for x in raw_input:
        addition = addition + x
    result = addition/len(raw_input)
    print(f"Mean of given data is {result}")
    return result
mean_finder()




