## 문법
- IN: 여러 단어들 중에서 일치하는 단어를 찾을 때 IN을 쓸 수 있다.
- WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')

- LIKE: 문자열 부분일치 검색.
  - SELECT * FROM TABLE WHERE NAME LIKE '%ABC%'
  - NAME칼럼 중 ABC라는 문자가 있는 ROW출력
  
  - SELECT * FROM TABLE WHERE NAME LIKE '%ABC%'
  - ABC로 끝나는 문자가 있는 ROW출력

  - SELECT * FROM TABLE WHERE NAME LIKE '_ABC%'
  - 앞에 글자 하나
  - SELECT * FROM TABLE WHERE NAME LIKE '__ABC%'
  - 앞에 글자 두개

- CASE WHEN ~~~  
    THEN ~~    
    ELSE ~~   
    END