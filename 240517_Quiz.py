def is_valid_number(number):
    # 주민등록번호 형식 확인 (하이픈 제외)
    if len(number) != 13 or not number.isdigit():
        return False

    # 각 자리수에 해당하는 가중치
    weights = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

    # 가중치와 주민등록번호 각 자리수를 곱한 합
    total = sum(int(number[i]) * weights[i] for i in range(12))

    # 합을 11로 나눈 나머지
    remainder = total % 11

    # 11에서 나머지를 뺀 값의 10으로 나눈 나머지
    check_digit = (11 - remainder) % 10

    # 계산된 값과 실제 주민등록번호의 13번째 자리 비교
    return check_digit == int(number[12])

user_number = input("주민등록번호를 입력하세요: ")

if is_valid_number(user_number) :
    print("유효한 주민등록번호입니다.")
else :
    print("유효하지않은 주민등록번호입니다.")