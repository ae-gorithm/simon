"""
탕후루 뭔가 스택 느낌 -> 덱이다
아하.. 두 종류 이하로...
일단 N의 개수가 상당히 많습니다. 
그냥 이거 몇개 빼냐 안빼냐는 따로 안해도 될 것 같다.
가장 긴 두 종류로 가면 되지 않을까?
포인터 두개 슬라이싱하면서, 종류가 두개 이상 되면 빼는게 나을 것 같은데 뭘 어떻게 기록해야할까?
1. 당연히 현재와 지금 어떤 것들을 가지고 있는지. maximum은 가지고 있어야겠지?
2. 그리고 같은게 나오면 cnt를 늘리자! 그래야 다음 슬라이싱이 어디서부터 갈지 알 수 있으니까. 아니다. cnt를 늘리지 말고, 시작 지점을 포인터로 지정해두면 되잖아.

1. 지금 과일이 fruits에 있는지 파악
1-1. 있다면? fruits[s]와 같은 과일인지 파악
1-1-1. 같은 과일이라면? 다음으로 넘어가면 될 듯
1-1-2. 다른 과일이라면? s만 j로 업데이트
1-2. 없다면? fruits에 요소가 몇개인지 파악
1-2-1. 요소가 1개 이하 -> fruits에 넣고, s를 j로 업데이트 
1-2-2. 요소가 2개 -> 이전 과일 S[s]만 남기고 나머지 하나 빼고. i는 s로 옮기고. s는 j로 옮기고. 과일 집어넣고.
"""

N = int(input())
S = tuple(map(int, input().split()))

# 과일 두 개로 이어진 시작점
i = 0
# 마지막 과일이 언제부터 시작되었는지
s = 0
# 현재의 과일
fruits = set([S[0]])
# 최대 길이
maximum = 1

for j in range(1, N):
    fruit = S[j]
    cur_fruit = S[s]
    if fruit in fruits:
        if fruit != cur_fruit:
            s = j
    else:
        if len(fruits) >= 2:
            fruits = set([cur_fruit, fruit])
            i, s = s, j
        else:
            fruits.add(fruit)
            s = j
    maximum = max(maximum, j - i + 1)

print(maximum)
    