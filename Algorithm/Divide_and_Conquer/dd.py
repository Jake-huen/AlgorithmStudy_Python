# 높이 n개의 계단을 올라가는 방법을 리턴한다
def staircase(stairs, possible_steps):
    # 코드를 쓰세요
    d=[0]*(stairs+1)
    d[0]=1
    d[1]=1
    for i in range(2,stairs+1):
        step=0
        for j in range(len(possible_steps)):
            if i>=possible_steps[j]:
                step+=d[i-possible_steps[j]]
        d[i]=step
    return d[stairs]
print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))