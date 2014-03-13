
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
# this script imports the sys module, and returns fib(<argument[1]>)
# the if statement can kind of be seen as the main function
# by the way, sys contains everything you enter in console, including
# <arguments>, which is assigned to argv (which is a list?).

# notice this allows you to use the file as an importable module, and
# as executable script

