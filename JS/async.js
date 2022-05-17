// async를 function 앞에 붙이면 항상 promise를 반환한다.

// async function f() {
//     return 1;
// }

// f().then(console.log('hello promise'));

// async function f2() {
//     return Promise.resolve(1);
// }

// f2().then(console.log('hello promise2'));

async function f() {
    let promise = new Promise((resolve, reject) => {
        setTimeout(() => resolve('done!'), 1000);
    })

    let result = await promise;
    console.log(result);
}

f()

