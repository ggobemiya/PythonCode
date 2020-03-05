# Codesignal>Arcade>Intro #56 Problem
# This is not a good answer. But that's the answer I can give you now. 20/03/05
# When I finish all Arcade, I can give a good answer.

def digitsProduct(p):
  
  #예외 처리
  if p == 1:
    return 1

  if p == 0:
    return 10

  #약수 구하기
  li = []

  while(1):
    
    for i in range(9,1,-1):
      if p % i == 0:
        p /= i
        li.append(i)
        break
    else:
      return -1
    
    if p == 1:
      break

  #최솟값 구하기
  return int(''.join(map(str,sorted(li))))
#[출처] [python] codeSignal 문제풀이 (55~57)|작성자 Jun

#    if product == 1:
#        return 1
#    elif product == 0:
#        return 10
#
#    dig=[]
#    while :
#        
#
#    if len(dig)==0:
#        return -1
#    
#    
#
#    print(dig)


# def oned(k): #k=[x,y]
#     k2 = []
#     for i in range(len(k)):
#         k1=[]
#         if k[i] <10:
#             k1.append(k[i])
#         else:
#             j = 1
#             while k[i]%j !=0:
#                 j+=2
#                 if k[i]%j == 0:
#                     k1.append(j, k[i]/j) 
#         k2.append(k1)
#     return k2
            
