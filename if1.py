# num=int(input("정수를 입력하시오:"))

# if num % 2==0:
#     print("짝수입니다.")
# else:
#     print("홀수입니다")


year=int(input("연도를 입력하시오: "))
if((year % 4 ==0 and year % 100 != 0)or(year % 400 == 0)):
  print(year, "년은 윤년입니다.")
else : 
  print(year, "년은 윤년이 아닙니다.")

  #윤년이 되는 조건
  #연도가 4의 배수이면서 ==
  #100의 배수가 아니거나 !=
  #또는 400의 배수이면
  #해당 연도는 윤년임 
