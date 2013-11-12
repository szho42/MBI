import sys

def main():
  cmd = sys.argv[1]
  nums = sys.argv[2:]
  if cmd == 'add':
     total = sum(map(float,nums))
  if cmd == 'mult':
     total = reduce(lambda a, b: a * b, map(float,nums))
  print total 

if __name__ == '__main__':
  main()
