lines: list = []
f = open('data/quiz2.txt', mode='r')
#print(f.read())
for line in f.readlines():
  lines.append(line)
f.close()

# TODO: 
# 위 코드는 'data/quiz2.txt'의 텍스트를 줄 단위로 읽어들이는 코드입니다.
# 아래 조건에 맞추어 정답을 계산하세요.

# 조건 1. 
#  두번째 라인에서 마지막 라인까지의 숫자를 읽어들여
# 조건 2. 
#  직전 라인에서 계산된 최종 값에(첫번째 라인은 계산하지 않음) 
#   - 3의 배수면 곱하기
#   - 10의 배수면 빼기
#   - 소수면 나누기
#   - 그 외의 값은 더하기
#  를 한 결과 값(정답)을 'data/quiz2.txt'에 저장해 주세요.
#  조건 3, 
#   단, 정답은 결과 파일의 첫번째 줄에 위치해야 합니다.

# 제약 조건 
#   모듈 또는 라이브러리를 추가로 로드하지 않습니다. 
#   파이썬 코드 파일을 추가로 생성하지 않습니다. 
#   상단 코드는 하단의 코드로 결과를 확인할 수 있는 한 마음껏 수정하셔도 됩니다.

# {코드 작성 시작}

'''
1
100
20
3
226
'''

#lines_ = f.readlines()
save_results = ""
initial_value = 1
for line_number, line_contents in enumerate(lines):
  value = float(line_contents)

  if line_number == 0 :
    initial_value =value
    #print(line_number, value, "init val")

  else:
    if value % 3 == 0 :
      initial_value = initial_value * value
      #print(line_number, value, "multi")
    elif value % 10 == 0 :
      initial_value = initial_value - value
      #print(line_number, value, "minus")
    elif (value % 2 == 1) and (value % 3 == 1):
      initial_value = initial_value / float(value)
      #print(line_number, value, "div")
    else:
      initial_value = initial_value + value
      #print(line_number, value, "plus")
#print(initial_value)

fw = open('data/quiz2.txt', mode='w')
fw.write(str(initial_value)+'\n')
for line_contents in lines:
  fw.write(line_contents)
fw.close()

# {코드 작성 완료}
f = open('data/quiz2.txt', mode='r')
print(f.read())
f.close()