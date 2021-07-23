## Keyword
`crawling`

## Crawling이란?
 - 돌아다니면서 원하는 정보를 수집하는 행위를 의미한다.
 - 웹 상에 존재하는 정보들이 크롤링의 대상들이다.
 - 크롤링은 정적 크롤링과 동적 크롤링으로 나누어 질 수 있다.

## 정적 크롤링
1. 특정 URL을 통해 데이터 수집이 가능하다.
2. 속도가 빠르다.
3. 새로고침을 하지 않으면 페이지 안의 데이터가 변하지 않는다.
4. 라이브러리 : request, beautifulsoup 

## 동적 크롤링
1. 속도가 느리다.
2. 수집 대상에 한계가 거의 존재하지 않는다.
3. 라이브러리 : selenium


## 방법
 - HTML 소스를 가져와서 원하는 정보를 사용할 수 있다.
 - 오픈 API를 활용해서 받은 데이터중 필요한 데이터만 사용하는 방법
 - 브라우저를 조적해 원하는 정보를 사용하는 방법.


## 파이썬 가상환경 세팅하기
```
python -m venv (virtualenv)

(Window) virtualenv\Scripts\activate
(Linux) source virtualenv/bin/activate
```
