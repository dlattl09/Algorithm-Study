# 첫째 줄에 숫자 N이 주어진다. N은 10,000보다 작거나 같은 자연수이다.

n = int(input())

num = 666
nth = 0
while(1):
  if n == nth:
    print(num-1)
    break
  elif '666' in str(num):
    nth+=1
  num+=1
