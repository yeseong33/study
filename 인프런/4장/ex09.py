# 블록의 중요성에 대한 실습
# 타 언어(java, c, c++ 등)에서는 블록을 중괄호로 감싸서 들여쓰기를 해야된다 라는 문법이
# 없다.

#타 언어 예시
# if (10>5): {
#     print('참입니다.'); print('참입니다.);
# }
# else:{
#     print('거짓입니다.');
# }

# 파이썬에서는 블록을 줄 때, 반드시 공간을 동일하게 줘야 한다.
# 파이썬의 문법에서는 블록(실행 문장이 여러 개일 때)을 만들 때, 들여쓰기를
# 해야하며, 이렇게 해주어야 프로그램의 가독성이 좋아진다.

score = 95
if score >= 95:
    print('합격입니다.')
    print('장학금도 받을 수 있습니다.')
