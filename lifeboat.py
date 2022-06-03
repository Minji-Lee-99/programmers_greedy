"""
name: Lee Minji
date :2022.06.03
problem: programmers greed life boat
explain: 가장 무거운 사람과 태울 수 있는 사람들을 태우고, 그 다음 무거운 사람과 태울 수 있는 사람들을 태우는 방식으로 문제를 해결하였습니다.
먼저 정렬한 후, 인덱스를 활용하여 문제를 해결하였습니다.
people의 길이를 n이라고 했을 때, 바깥의 루프는 최악의 경우 n번을 돈다. 안쪽의 루프 역시 최악의 경우 n-1번을 실행할 것이다. 그러나, 안쪽 루프를 여러번 도는 만큼 바깥 쪽 루프가 도는 횟수가 줄어들기 때문에 최종적인 효율성은 O(n)이라고 보아도 될 것 같다.
"""


def solution(people, limit):
    people.sort(reverse=True)
    count = 0
    back = len(people) - 1
    front = 0
    while True:
        weight = people[front]
        if front < back:
            count += 1
        elif front == back:  # front, back이 같은 경우는 중간에 한명만 남은 경우이므로, count에 1을 더해주고, 반복문을 종료시킨다.
            count += 1
            break
        else:  # front가 back보다 커지는 [80 70 50 50], 100처럼 연속으로 위치한 두개의 숫자가 한 보트에 타게 되는 경우 숫자가 역전이 된다. 그런 경우는 반복문을 종료시킨다.
            break
        while True:
            weight = weight + people[back]
            if weight <= limit:
                back -= 1
                if front == back:   #두개의 인덱스가 같아지면 더 이상 확인할 필요가 없으므로, 반복문을 종료한다.
                    break
            else:  # 무게가 제한을 넘기면 반복문을 탈출한다.
                break
        front += 1
    answer = count
    return answer


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
print(solution([70, 50, 80, 50, 90, 40], 240))
print(solution([40, 50, 150, 160], 200))
print(solution([100, 500, 500, 900, 950], 1000))
