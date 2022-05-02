## OAuth
- 자신이 소유한 리소스에 소프트웨어 어플리케이션이 접근할수 있도록 허용해줌으로써 접근 권한을 위임해주는 개방형 표준 프로토콜

## 탄생 배경
- OAuth이 등장하기 전에 A 사이트에서 B 사이트의 리소스를 가져오기 위해서는 다른 사이트의 ID와 Password를 직접 입력 받아 저장하여 필요할 때마다 불러와서 사용을 해야했다. 위와 같은 방식을 사용하게되면 다음과 같은 문제가 발생한다.

    - 사용자 : A 사이트에 B사이트의 ID와 Password를 넘겨주는 것에 대해 신뢰할 수 없다.
    - A 사이트 : ID와 Password를 받았기 때문에 보안 문제가 생기는 경우 모든 책임을 져야한다.
    - B 사이트 : A 사이트를 신뢰할 수 없다.


## 용어
- Resource Server	OAuth2.0 서비스를 제공하고 자원을 관리하는 서버
(보통 google, naver 같은 다른 사이트)
- Resource Owner(자원 소유자)	Resource Server의 계정을 소유하고 있는 사용자
(사용자)
- Client	Resource Server의 API를 사용하여 데이터를 가져오려고 하는 사이트
(개발 사이트)
- Authorization Server(권한 서버)	Client가 Resource Server의 서비스를 사용할 수 있게 인증하고 토큰을 발생해주는 서버
(인증 서버, google, naver)
- Access Token	자원 서버에 자원을 요청할 수 있는 토큰
- Refresh Token	권한 서버에 접근 토큰을 요청할 수 있는 토큰


reference : [oauth2란?](https://velog.io/@undefcat/OAuth-2.0-%EA%B0%84%EB%8B%A8%EC%A0%95%EB%A6%AC)