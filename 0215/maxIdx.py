# 가장 큰 수는 왼쪽부터 몇 번째 숫자인가?
# 같은 숫자가 있는 경우 오른쪽 숫자를 선택한다.
# 다음의 경우 6번째
arr = [7, 2, 4, 3, 4, 7, 2]

maxIdx = 0
for i in range(1, len(arr)):
    if(arr[maxIdx] <= arr[i]):
        maxIdx = i
print(maxIdx+1)
