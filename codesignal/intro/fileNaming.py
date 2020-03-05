# Codesignal>Arcade>Intro #57 Problem
# This is not a good answer. But that's the answer I can give you now. 20/03/05
# When I finish all Arcade, I can give a good answer.

def fileNaming(s):
  for i in range(len(s)):
    #s[i] 이전까지의 값을 체크해서 중복된 값이 있는지 확인
    if s[i] in s[:i]:
      #중복된 값이 있다면 뒤에 (1) 를 붙여줌
      c = 1
      #만약 이미 (1)이 뒤에 있다면 c의 값을 더해줌
      while s[i] + "(" + str(c) + ")" in s[:i]:
        c += 1
      #뒤에 (c)를 붙여줌
      s[i] += "(" + str(c) + ")"

  return s
#[출처] [python] codeSignal 문제풀이 (55~57)|작성자 Jun
