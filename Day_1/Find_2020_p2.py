#!/usr/bin/env python3

def main(txtFile):
    f = open(txtFile, 'r')
    txtlist = [int(x) for x in f.read().split()]
    for i in range(len(txtlist)-1):
        num = txtlist[i]
        for j in range(i, len(txtlist)-1):
            num2 = txtlist[j]
            if num2+num < 2020:
                for h in range(j, len(txtlist)-1):
                    num3 = txtlist[h]
                    if (num+num2+num3 == 2020):
                        print(num*num2*num3)
                        return num*num2*num3
    f.close()
    return -1

if __name__ == "__main__":
    main("C:\\Users\\Backal\\Python_tests\\2020_day1_advent.txt")
