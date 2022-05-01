"use strict";

// Assignment1
let num1 = +prompt("input num1:");
let num2 = +prompt("input num2:");
alert((num1 + num2))

// Assignment2
alert( 6.35.toFixed(1) ); // 6.3 -> 2진법 무한소수이기에. 정밀도 손실 발생
alert( Math.round(6.35 * 10) / 10);

// Assignment3
function readNumber() {
    let num;
    do {
        num = prompt("enter num");
    } while (!isFinite(num));

    if (num === null || num === '') return null;
    return  +num;
}

// Assignment4
let i = 0;
while (i != 10) {
  i += 0.2;
} // 무한루프. 0.2씩 더하면 정밀도 손실 발생.

// Assignment5
function random(min, max) {
    return m(min + Math.random() * (max - min));
}

// Assignment6
function randomInteger(min, max) {
    return Math.floor((min + Math.random() * (max - min + 1)))
}