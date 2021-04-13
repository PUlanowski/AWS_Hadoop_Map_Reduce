import sys
import re

def reduce(lines):
    '''
    This reducer consumes mapper output in format [year /t amount ; 1]/ This line is split by regex spliter to year
    which is our key, amount and 1. Reducer then aggregating amounts and calculates how many keys of the same kind went
    into (variable clock). If during processing key (year) is changed then reducer print year and average
    (sum of amounts/clock) and start working on the next key resetting clock and sum.
    :return: handle by hadoop
    '''
    prevYear = None
    sum = 0
    clock = 0
    for line in lines:
        year, amount, count = re.split("\t|;",line)

        if year != prevYear:
            print("{0}\t{1}".format(year, (sum/clock))
            sum = 0
            clock = 0

        sum += int(float(amount))
        clock += int(count)


        prevYear = year

if __name__=="__main__":
    reduce(sys.stdin)