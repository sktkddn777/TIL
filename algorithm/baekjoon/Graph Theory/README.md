## Graph Theory

## 틀린 문제

## 알게 된 내용
1. 미로탐색
  - 2차원 배열을 초기화할 때 아래와 같이 초기화 해줘야 한다.
 ```  
  arr = [[0] * N for _ in range(M)]
  ```
  - 만약 `arr = [[0] * N] * M` 으로 초기화 할 경우 M개의 [0] * N은 모두 같은 객체로 인식 된다.
  