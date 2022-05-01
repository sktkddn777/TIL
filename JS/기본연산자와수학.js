"use strict";

// Assignment1
let a1 = 1, b = 1;

let c = ++a1; // 2
let d = b++; // 1

// Assignment2
let a = 2;

let x = 1 + (a *= 2);

// a = 4
// x = 5

// Assignment3
"" + 1 + 0 // 10
"" - 1 + 0 // -1
true + false // true
6 / "3" // 2
"2" * "3" // 6
4 + 5 + "px" // 9px
"$" + 4 + 5 // $45
"4" - 2 // 2
"4px" - 2 // NaN
7 / 0 // Infinity
"  -9  " + 5 // "  -9  5"
"  -9  " - 5 // -14
null + 1 // 1
undefined + 1 // NaN
" \t \n" - 2 // -2

// Assignment4
let num1 = prompt("덧셈할 첫 번째 숫자를 입력해주세요.", 1);
let num2 = prompt("덧셈할 두 번째 숫자를 입력해주세요.", 2);
alert(Number(num1) + Number(num2))