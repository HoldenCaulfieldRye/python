import time
if __name__ == '__main__':
  t = time.clock()
  l = [i**2 for i in range(40000000)]
  print time.clock() - t, 'seconds to crunch through that'
