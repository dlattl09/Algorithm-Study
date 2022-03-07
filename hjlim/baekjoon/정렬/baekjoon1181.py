#첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 
#둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 
#주어지는 문자열의 길이는 50을 넘지 않는다.

num = int(input())
words = []

for i in range(num):
  words.append(input())

words = list(set(words))
words.sort()
words.sort(key = len)

for i in words:
    print(i)
