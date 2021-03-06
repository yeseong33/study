## 조건문의 구조
# 문제를 해결할 때 어떤 조건에 따라서 두 개 또는 여러개의 실행 경로 가운데 하나를
# 선택해야 하는 경우가 종종 있다. 예를 들면 아래 그림과 같다.

# 프로그램에서도 외부에서 들어오는 정보에 따라서 많은 선택을 하게 된다. 이런 식으로
# 조건에 따라 결정을 내리는 문장을 조건문이라고 한다.

# if-else 문에서는 조건을 수식으로 표현하는데 이것을 '조건식' 이라고 한다. 하여
# 조건식의 결과는 참이나 거짓으로 표현되어야 한다.

# if-else 구문은 딱 '모'아니면 '도'라는 형태라 50%의 확률을 지닐 수 있다
# 따라서 때에 따라 else문은 생략이 가능하다.

# 조건식에 비교연산자를 사용해 if - else 구문을 실행한다.
# 조건식에는 변수를 사용할 수 있다.


## 부울 변수
# 조건식의 결과는 참 아니면 거짓이다. 따라서 참과 거짓을 저장하는 변수를 만들 수 있는데
# 이러한 변수를 부울(bool)변수라고 칭한다.
# 부울 변수는 프로그래밍에서 플래그(flag) 변수로 많이 사용된다.


## 순서도


## 블록
# if 문 아래 코드는 동일한 개수의 공백을 가지고 있어야 한다.
# 소스의 가독성을 높이려면 들여쓰기 할 때 일관된 방법을 사용하는 것이 좋다. 즉 TAP 키를 사용했다면
# 프로그램의 나머지 부분에서 TAP 키를 사용해 블록의 공간을 똑같이 해주는 것이 편리하다.


## 논리연산자**
# and = x와 y가 모두 참이면 참, 그렇지 않으면 거짓
# or = x나 y중에 하나만 참이면 참, 모두 거짓이면 거짓
# not = not 연산


# if ~ elif
# 조건에 따라 다중으로 분기되는 결정을 해야 하는 경우에 사용됨.
# if~elif 구문에서는 다중 조건 중 하나만 만족하게 된다면 그 이후는 실행되지 않는다.
# 이를 사용 할 경우 마지막 조건이면 cpu 가 모든 경우를 참조 한다.
# 따라서 if 구문은 플레그로써 사용하는 것이 바람직하고 다중 조건에 경우 if ~ elif 구문을
# 사용하는 것이 좋다.
# else: 이후에는 조건식을 사용하지 않는다., 없어도 된다.


# 중첩 if~ else 문
# 여러개의 if~else 구문이 포할될 수 있으며 들여쓰기로 중첩의 수준을 알 수 있다.
# 이러한 구조는 자칫하면 프로그래밍을 한 자신도 못 알아볼 수 있으니, 많이 사용하지 않는 것이 바람직하다.
# 통상적으로 2개의 if ~ else 구문 정도로만 해도 문제는 해결 될 수 있다.
# 조건을 잘 설정해야 한다.


# 문자열과 순자의 저장 구조
# 진수변환(2,8,16 ...) 잘 할 줄 알아야 한다.

