import time 

lotto : str = None
f = open('data/quiz4.txt', mode='r')
lotto = f.read()
f.close()

print(lotto)

# TODO: 
# 오늘자 로또 6/45의 당첨번호가 'data/quiz4.txt'에 띄어쓰기로 구분되어 들어 있습니다.
# (코딩 테스트용도 이므로 보너스 번호는 사용하지 않습니다.)

# 등수의 기준은 아래와 같습니다.
#  5등 - 3개 번호 일치
#  4등 - 4개 번호 일치
#  3등 - 5개 번호 일치
#  2등 - 5개 번호 + 보너스 번호 일치 
#  1등 - 6개 번호 일치 

# quiz3.py 에서 생성된 로또게임 100회의 숫자가 'data/quiz3.txt'에 있습니다.
# 모든 로또게임의 등수를 확인하고 각 게임별 등수가
#   5등이면 선택된 번호 모두 더하기
#   4등이면 4번째 번호를 나머지 번호는 더한 값에 빼기
#   3등이면 3번째 번호를 나머지 번호를 더한 값에 곱하기
#   2등이면 2번째 번호를 나머지 번호를 더한 값게 나누기
#   1등이면 모든 번호를 곱하고 오늘 일자로 나누기 
# 연산한 결과(계산 값)를 등수와 함께 아래의 구성으로 'data/quiz5.txt'에 기록합니다.
# 구성(게임당 한줄 사용)
# {등수} {계산 값} {로또번호 6자리} 

# 제약 조건 
#   모듈 또는 라이브러리를 추가로 로드하지 않습니다. 
#   파이썬 코드 파일을 추가로 생성하지 않습니다. 
#   상하단의 코드는 수정하지 않습니다.

# {코드 작성 시작}

def number_check(array):
    nums_str = array.split(" ")
    nums_int = [ int(v) for v in nums_str ]
    lotto_cnt = [0 for _ in range(46)]
    for num in nums_int:
        lotto_cnt[num] += 1
    max_count = max(lotto_cnt)

    award = -1
    if max_count == 3:
        award = 5
    elif max_count == 4:
        award = 4
    elif max_count == 5:
        award = 3
    elif max_count == 6:
        award = 1

    return award, nums_int

def get_result(award, int_nums):
    return_value = -1

    if award == 5 :
        value = 0
        for v in int_nums:
            value += v

    elif award == 4 :
        value = 0
        for idx, v in enumerate(int_nums):
            if idx != 3:
                value += v
        return_value = value - int_nums[3]

    elif award == 3:
        value = 0
        for idx, v in enumerate(int_nums):
            if idx != 2:
                value += v
        return_value = value * int_nums[2]

    elif award == 1:
        value = 1
        for idx, v in enumerate(int_nums):
            value *= v
        day = int(time.strftime('%d', time.localtime(time.time())))
        return_value = value / float(day)

    return return_value

award, int_nums = number_check(lotto)
return_value = get_result(award, int_nums)

award_str = ""
ret_valu_str = ""

if return_value != -1:
    ret_valu_str = str(return_value)

if award != -1 :
    award_str = str(award)

f = open('./data/quiz5.txt', mode='w')
f.write(award_str +" " + ret_valu_str + " "+ str(lotto) )

# {코드 작성 완료}


f = open('data/quiz5.txt', mode='r')
print(f.read())
f.close()
