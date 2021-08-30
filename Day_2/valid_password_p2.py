#!/usr/bin/env python3

def main(txtFile):
    valid = 0
    with open(txtFile) as f:
        for line in f:
            info = line.split()
            pos = [int(x)-1 for x in info[0].split('-')]
            letter = info[1][0]
            password = info[2]
            if (password[pos[0]] == letter and password[pos[1]] != letter) or (password[pos[0]] != letter and password[pos[1]] == letter):
                valid += 1
    f.close()
    print("Total invalid passwords are {}".format(valid))
    return 0

if __name__ == "__main__":
    main("C:\\Users\\Backal\\Python_tests\\2020_day2_advent.txt")