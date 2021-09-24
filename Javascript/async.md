비동기 처리 : 특정 코드의 실행이 완료될 때까지 기다리지 않고
다음 코드를 먼저 수행하는 자바스크립트의 특성.

```
console.log('Hello');

setTimeout(function(){
    console.log('bye');

}, 3000);

console.log("hello again");
```

위는 간단한 예제다. 출력해보면 Hello -> hello again -> bye순으로 출력이 된다.

setTimeout 함수는 비동기 방식으로 실행되기 때문에 setTimeout을 실행하고 나서 다음 코드인 hello again으로 넘어갔다.

하지만 비동기 방식으로는 야기될 수 있는 문제가 여러 있는데
이를 방지하기 위해 callback 함수가 있다.

callback함수는 함수를 파라미터로 전달해주는 함수다.

콜백함수를 계속 무는 형식으로 코딩하게 되면 -> 콜백 지옥에 빠지게 된다. 이를 해결하기 위해 Promise나 Async를 사용한다.




