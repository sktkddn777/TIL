# Mongo DB
Mongo DB는 NoSQL로, 스키마로 짜지 않고 SQL 데이터베이스에 비해 보다 자유로운 형태로 데이터를 저장할 수 있습니다.

1. 데이터의 구조가 거의 또는 전혀 없는 대용량의 데이터를 저장하는 경우,
2. 클라우드 컴퓨팅 및 저장공간을 최대한 활용하는 경우,
3. 빠르게 서비스를 구축하고 데이터 구조를 자주 업데이트 하는 경우에 NoSQL을 사용합니다.

Document
 - 필드 - 값 쌍으로 저장된 데이터

Field
 - 데이터포인트를 위한 고유한 식별자

Value
 - 주어진 식별자와 관계된 데이터

Collection

 - MongoDB의 도큐먼트로 구성된 저장소로 일반적으로 도큐먼트 간의 공통 필드가 있습니다. 데이터베이스 당 많은 컬렉션이 있고 컬렉션 당 많은 도큐먼트가 있을 수 있습니다.

 - 도큐먼트는 json 형태로 저장되어야한다. json은 읽기 쉽지만 파싱이 느리고 메모리사용에 있어서 비효율적이다. 그리고 json은 사용할 수 있는 타입에 제한이 있다. 이러한 문제를 해결하기 위해 bson형식을 사용한다.

 - 먼저 JSON 형식으로 데이터를 가져오고 내보내기 위한 명령어인 mongoimport와 mongoexport가 있고,

 - BSON 형식으로 가져오고 내보내기 위한 명령어 mongorestore와 mongodump가 있습니다.

## cli
 - create , read , update , delete