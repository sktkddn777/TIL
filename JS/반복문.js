"use strict";

// Assignment1
let i = 3;

while (i) {
  alert( i-- ); // 3 2 1
}
// Assignment2
let i2 = 0;
while (++i2 < 5) alert( i2 ); // 4

let i3 = 0;
while (i3++ < 5) alert( i3 ); // 5

// Assignment3

for (let i = 0; i < 5; i++) alert( i ); // 4

for (let i = 0; i < 5; ++i) alert( i ); // 4

// Assignment4

for (let i = 2; i < 11; i++) {
    if (i % 2 == 0)
        alert(i);
}

// Assignment5
let n = 0;

while (n < 3) {
    alert( `number ${n}!` );
    n++;
}

// Assignment6
while (1) {
    let v = prompt("enter num");
    if (v > 100)
        break
}

// Assignment7
let solution = (n) => {
    let arr = Array(n+1).fill(true).fill(false, 0, 2);

    for (let i = 2; i < Number(n ** 0.5)+1 ; i++) {
        if (arr[i]) {
            for (let j = i*i; j <= n; j+= i)
                arr[j] = false;
        }
    }
    return arr;
}