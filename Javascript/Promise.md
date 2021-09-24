프로미스는 자바스크립트 비동기 처리에 사용되는 객체이다.

프로미스는 주로 서버에서 받아온 데이터를 화면에 표시할 때 사용한다.

프로미스 상태: 프로미스의 처리 과정
new Promise() : 프로미스를 생성. 3가지 상태를 가짐.
1. Pending 대기 : 비동기 처리 로직이 아직 완료되지 않은 상태
2. Fulfilled(이행) : 비동기 처리가 완료되어 프로미스가 결과 값을 반환해준 상태
3. Rejected(실패) : 비동기 처리가 실패하거나 오류가 발생한 상태