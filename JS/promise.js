
// executer 리턴값은 무시
const ret = new Promise((resolve, reject) => {
    return 'returned';
});
ret
    .then(() => console.log('ret success'))
    .catch(() => console.log('ret catched'));

function startAsync(age) {
    return new Promise((resolve, reject) => {
        if (age > 20) {
            return resolve(`${age} success`);
        }
        return reject(new Error(`${age} is not over 20`));
    })
}

startAsync(23);
startAsync(10);