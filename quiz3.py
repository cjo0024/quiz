import time

# TODO: 
# 로또 6/45는 1에서 45까지의 숫자 6개를 선택하는 게임(이하 로또게임)입니다.
# '자동게임'은 로또게임 시 숫자를 기계가 자동으로 선택하는 방식입니다.

# 로또게임 100회를 6개의 숫자를 '자동게임'으로 시행하는 코드를 구성해 주세요. 
# 100회의 게임에서 선택된 숫자들를 각각 한 줄로 구성하여'data/quiz3.txt'에 저장해 주세요.
# 게임당 선택된 6개의 숫자는 띄어쓰기로 구분합니다.

# 제약 조건 
#   모듈 또는 라이브러리를 추가로 로드하지 않습니다. 
#   파이썬 코드 파일을 추가로 생성하지 않습니다. 
#   하단의 코드는 수정하지 않습니다.

# {코드 작성 시작}
def select_random():
    t = time.time()

    return 1


select_random()
selected_nums = []
for i in range(6):
    selected_nums.append( select_random() )

#f = open('data/quiz3.txt', mode='w')
#f.write(selected_nums[0]+" "+selected_nums[1]+" "+selected_nums[2]+" "+selected_nums[3] +" "
#        selected_nums[4]+ " "+selected_nums[5]+" "+ selected_nums[6])



# {코드 작성 완료}

f = open('data/quiz3.txt', mode='r')
print(f.read())
f.close()