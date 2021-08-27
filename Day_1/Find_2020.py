#!/usr/bin/env python3

def main(txtFile):
    f = open(txtFile, 'r')
    txtlist = f.read().split()
    try:
        numbers = [int(x) for x in txtlist]
    except:
        print("Error converting list to ints")
        return -1
    for i in range(len(numbers)-1):
        ans = 2020 - numbers[i]
        for j in range(i, len(numbers)-1):
            if numbers[j] == ans:
                print("The answer is {}".format(ans * numbers[i]))
                return ans * numbers[i]

    return -1


if __name__ == "__main__":
    main("C:\\Users\\Backal\\Python_tests\\2020_day1_advent.txt")