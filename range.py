#range:적정범위 숫자, 연속된 숫자(정수)
#0~10 정수 만들기
print(range(10)) # range(0, 10)
# 10은 포함되지 않음 

#range=>list로 변환하여 출력
print(list(range(10)))   #[0,1,2,3,4,5,6,7,8,9]
print(list(range(1,10))) #[1,2,3,4,5,6,7,8,9]1부터 10미만(즉 9)

print(list(range(1,11)))   #[1,2,3,4,5,6,7,8,9,10]
print(list(range(2,10,2))) #[2,4,6,8]2부터 10미만 2씩 증가

#list, turpie(고정), 딕셔너리