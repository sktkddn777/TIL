


- Node.js, Go와 비슷한 수준으로 빠른 성능을 자랑한다.
- 개발 속도가 200%~300% 빨라진다.
- 코드 버그가 40% 감소한다.
- 쉽게 사용할 수 있다.

wsgi
일반적으로 웹 서버는 python으로 되어 있지 않다. 그래서 python으로 되어있는 웹 프레임워크인 django와 소통해줄 중간 개체가 필요하다.

- WSGI는 웹 서버와 웹 프레임워크간의 구현에 구애받지 않는 인터페이스로 만들어져 이식가능한 웹 애플리케이션 개발을 할 수 있다.
- 웹소켓을 사용할 수 없다
- 파이썬의 비동기를 사용할 수 없다.

Uvicorn은 초고속 ASGI Web server입니다. 단일 프로세스에서 uvloop기반 비동기 Python code를 실행합니다.

Starlette는 비동기적으로 실행할 수있는 Web application server 입니다. Starlette는 Uvicorn 위에서 실행됩니다.

asgi로 
FastAPI 안에서 많은 비동기 처리를 수행할 수 있습니다.
빈틈없는 공식 문서와 별다른 Serializer 없이 Pydantic을 통한 Json 데이터 서빙
OpenAPI 지원으로 API Swagger 자동생성

