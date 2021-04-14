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
    #lines = ['1975\t3000.00;1', '1975\t4000.00;1', '1975\t5000.00;1','1965\t200.00;1',
    #         '1965\t40.00;1', '1969\t500.00;1', '1900\t0.00;1'] #for testing purposes only
    prevYear = None
    sum = 0
    clock = 0
    for line in lines:
        year, amount, count = re.split("\t|;",line)
        year = int(year)
        amount = float(amount)
        count = int(count)

        if year != prevYear and prevYear != None:
            print("{0}\t{1}".format(prevYear, (sum / clock) if clock != 0 else amount))
            sum = 0
            clock = 0

        sum += amount
        clock += count


        prevYear = year

if __name__=="__main__":
    reduce(sys.stdin)