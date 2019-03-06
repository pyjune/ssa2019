파일에서 입력 (디버깅용)

import sys

sys.stdin = open('input.txt', 'r') // 제출시 주석 처리
 한 줄에 변수 개수만큼 정수 입력

N = int(input())
N, M = map(int, input().split())
 정수 1차원 배열

arr = list(map(int, input().split())
 N줄에 걸친 정수 2차원 배열

arr = [ list(map(int, input().split())) for i in range N]
 12345처럼 이어진 숫자를 한 자리씩 나눠서 리스트에 저장

arr = list(map(int, input()))
12345
>>> arr
[1, 2, 3, 4, 5]
 123처럼 이어진 숫자를 한 자리씩 나눠서 리스트에 문자열로 저장

>>> arr = list(input())
123
>>> arr
['1', '2', '3']
 문자열 abc를 한 글자씩 나눠서 리스트에 저장

>>> arr = list(input())
abc
>>> arr
['a', 'b', 'c']
