# 사용자에게 명령어를 입력받아서 터틀그래픽의 제어를 해보자. 즉 사용자가 'left' 를 입력
# 하면 왼쪽으로 회전하게 되고 사용자가 'right' 를 입력했다면 오른쪽으로 회전하게 하는
# 프로그램 만들기

# import turtle
# t = turtle.Turtle()
# # 반복문을 무한루프 돌려서 if 구문을 이용해 방향을 제어하는 코드
#
# while True:
#     inputs = input('방향을 입력하세요.')
#     if inputs == 'left':
#         t.left(60)
#         t.forward(100)
#     elif inputs == 'right':
#         t.right(60)
#         t.forward(100)

import turtle
t = turtle.Turtle()
t.shape('turtle')
# 반복문을 무한루프 돌려서 if 구문을 이용해 방향을 제어
# 무한루프를 프로그래밍 했다면 반드시 루프를 탈출하는 코드가 반드시 있어야 한다.
while True:
    direction = input('왼쪽 = left, 오른쪽 = right, 종료 = quit 입력 : ')
    # break 는 무한루프를 빠져나가라는 키워드이다. 무한루프에 무조건 있어야 한다.
    if direction == 'quit':
        print('종료되었습니다.')
        break
    if direction == 'left':
        print('left 를 입력하셨습니다.')
        t.left(60)
        t.forward(50)
    if direction == 'right':
        print('right 를 입력하셨습니다.')
        t.right(60)
        t.forward(50)

# 터틀 그래픽 창이 클릭이 되어야 화면에서 사라지게 하는 코드
turtle.exitonclick()
