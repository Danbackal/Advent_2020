#!/usr/bin/env python3

def main(txtFile):
    f = open(txtFile, 'r')
    txtlist = f.read().split()
    crashes = 0
    tree = '#'
    counter = 0
    for i in txtlist:
        space = i[counter]
        if space == tree:
            crashes += 1
        counter += 3
        overshot = counter - len(i)
        if overshot >= 0:
            counter = overshot
    f.close()
    print("You will hit {} trees".format(crashes))
    return 0


if __name__ == "__main__":
    main("C:\\Users\\Backal\\Python_tests\\2020_day3_advent.txt")
