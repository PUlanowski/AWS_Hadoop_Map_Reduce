import sys

def map(lines):
    '''
    This mapper takes line by line from input file, then splits it to words and extract required data
    i.e. year and amount. for output we add 1 as counter for average calculations in reducer.
    :return: handle by hadoop
    '''
    for line in lines:
        words = line.split(",")
        year = words[0].split("/")[0]
        amount = words[7].replace('$','').strip()
        print("{0}\t{1};{2}".format(year,amount,1))

if __name__=="__main__":
    map(sys.stdin)

