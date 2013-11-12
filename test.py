import sys

def main():
  cmd = sys.argv[1]
  if cmd == 'add':
     nums = sys.argv[2:]
     total = sum(map(float,nums))
  if cmd == 'mult':
     nums = sys.argv[2:]
     total = reduce(lambda a, b: a * b, map(float,nums))
  print total 

if __name__ == '__main__':
  main()
