"""
이 메소드는 문자열을 최소 몇 자리 이상을 가진 문자열로 변환시켜줍니다.
이때 만약 모자란 부분은 왼쪽에 “0”을 채워주는데요.
예를 들어 만약 "1".zfill(2)을 하면 "01"을 리턴합니다.
그리고 설정된 자릿수보다 이미 더 긴 문자열이라면 그 문자열을 그대로 출력합니다.
그러니까 "333".zfill(2) 와 같이 하면 문자열 그대로 “333”을 리턴합니다.
아래 코드를 보면 더 쉽게 이해할 수 있습니다.
이 메소드는 문자열을 예쁘고 통일감있게 출력하고자 할 때 자주 사용되니까 꼭 기억해주세요.
"""
print("1".zfill(6))#000001
print("333".zfill(2))#333
print("a".zfill(8))#0000000a
print("ab".zfill(8))#000000ab
print("abc".zfill(8))#00000abc