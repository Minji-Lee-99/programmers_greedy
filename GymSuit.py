"""
name: Lee Minji
date :2022.06.01
problem: programmers greed GymSuit
explain: index를 활용하여 문제에 접근했다. 체육복을 잃어버린 사람의 수를 m, 빌려줄 수 있는 사람의 수를 v, 총 명수를 n이라고 했을 때,
빅오 노테이션으로 나타내면 O(n)이다.
"""



def solution(n, lost, reserve):
    total = [0] * n
    count = 0#체육복을 잃어버린 학생 중에서 체육복을 빌릴 수 있는 학생의 수
    #체육복을 잃어버린 학생들의 위치를 인덱스를 통해서 표시(+1)
    for i in range(len(lost)):#O(m)
        total[lost[i] - 1] += 1
    #여분의 체육복을 가진 학생들의 위치를 인덱스를 통해서 표시(+2)
    for j in range(len(reserve)):#O(v)
        total[reserve[j] - 1] += 2
        #값이 3인 인덱스의 학생은 여분의 체육복을 가졌지만, 잃어버린 학생이므로 다시 0으로 변경
        if total[reserve[j] - 1] == 3:
            total[reserve[j] - 1] = 0
            count += 1
    #각 인덱스를 살펴보면서 1로 표시된 학생이 있는 경우(잃어버린 학생), 앞 뒤로 체육복을 빌려줄 수 있는 학생이 있는지 확인
    for k in range(n):#O(n)
        try:
            if total[k] == 1:
                if (k >= 1) and (total[k-1]==2):
                    count += 1
                    total[k-1] = 0 #있다면 빌려준 학생을 다시 0으로 만들어서, 중복으로 빌려주는 일이 없도록 함
                elif total[k+1]==2:
                    count+=1
                    total[k + 1] = 0
        except:#마지막 인덱스에서 (+1)을 했을 때, 에러가 발생하는 것을 대비해서 예외를 처리
            break
    answer = n - len(lost) + count #O(1)
    return answer


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
print(solution(5, [1, 2, 4], [2, 4, 5]))
