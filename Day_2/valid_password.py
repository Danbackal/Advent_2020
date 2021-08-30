#!/usr/bin/env python3

def main(txtFile):
    valid = 0
    with open(txtFile) as f:
        for line in f:
            info = line.split()
            letterRange = info[0].split('-')
            letter = info[1]
            password = info[2]
            letterAmount = password.count(letter[0])
            if int(letterRange[0]) <= letterAmount <= int(letterRange[1]):
                valid += 1
    f.close()
    print("Total invalid passwords are {}".format(valid))
    return 0

if __name__ == "__main__":
    main("C:\\Users\\Backal\\Python_tests\\2020_day2_advent.txt")