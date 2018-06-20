#!/usr/bin/env python
# coding=utf-8

import sys


def parse(filename):
    fp = open_arff_file()

    for data in open(filename):
        line = data.rstrip('\n').split(",")
        d_line = discretize_line(line)
        fp.write(d_line)
    fp.close()


def open_arff_file():
    fp = open('glass_data.arff', "w")
    fp.write('''@RELATION GlassCSInvestigation

@ATTRIBUTE RI {1, 0}
@ATTRIBUTE NA {1, 0}
@ATTRIBUTE MG {1, 0}
@ATTRIBUTE AL {1, 0}
@ATTRIBUTE SI {1, 0}
@ATTRIBUTE K {1, 0}
@ATTRIBUTE CA {1, 0}
@ATTRIBUTE BA {1, 0}
@ATTRIBUTE FE {1, 0}
@ATTRIBUTE TYPE {1, 2, 3, 4, 5, 6, 7}


@DATA
''')
    return fp


def discretize_line(line):
    d_line = [str(1)] * 10
    for i in range(1, 11):
        if float(line[i]) == 0:
            d_line[i - 1] = str(0)
        elif i == 10:
            d_line[i - 1] = str(int(line[i]))
    d_line = ','.join(d_line) + '\n'
    return d_line


def main():
    parse(sys.argv[1])


if __name__ == '__main__':
    main()
