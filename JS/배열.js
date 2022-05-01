"use strict"

// Assignment1
let fruits = ["사과", "배", "오렌지"];

// 배열을 '복사'한 후, push 메서드를 이용해 새로운 값을 추가합니다.
let shoppingCart = fruits;
shoppingCart.push("바나나");

// fruits에 어떤 값이 들어 있을까요?
alert( fruits.length ); // 4

// Assignment2
let styles = ["Jazz", "Blues"];
styles.push("Rock-n-Roll");
styles[Math.floor((styles.length-1) / 2)] =  "Classics";
console.log(styles.shift());
styles.unshift("RAP", "Reggae");

// Assignment3
let arr = ["a", "b"];

arr.push(function() {
  alert( this );
})

arr[2](); // this -> arr을 참조. arr배열을 출력한다.

// Assignment4
function sumInput() {
    let numbers = [];

    while (true) {
        let num = prompt("enter num");
        if (num === '' || num === null || isFinite(num))
            break;
        numbers.push(num);
    }
    let sum = 0;
    for (let number of numbers) {
        sum += number;
    }
    return sum;
}

// Assignment5
function getMaxSubSum(lst) {
    let maxSum = 0;
    let partSum = 0;
    for (let l in lst) {
        partSum += l;
        maxSum = Math.max(maxSum, partSum);
        if (partSum < 0) partSum = 0;
    }
    return maxSum;
}

// Assignment6
function camelize(str) {
    let splitStr = str.split('-');
    splitStr.map((word, index) => index == 0 ? word : word[0].toUpperCase() + word.slice(1))
    splitStr.join('');
}

camelize("background-color") == 'backgroundColor';
camelize("list-style-image") == 'listStyleImage';
camelize("-webkit-transition") == 'WebkitTransition';

// Assignment7
function filterRange(arr, a, b) {
    let newArr = arr.filter(item => (a <= item && item <= b));
    return newArr;
}

// Assignment8
function filterRangeInPlace(arr, a, b) {
    for (let i = 0; i<arr.length; i++) {
        if (arr[i] < a || arr[i] > b) {
            arr.splice(i, 1);
            i--;
        }
    }
}

// Assignment9
let arr2 = [5, 2, 1, -10, 8];

arr2.sort((a, b) => (b-a));
// 요소를 내림차순으로 정렬해주는 코드를 여기에 작성해보세요.

alert( arr2 ); // 8, 5, 2, 1, -10

// Assignment10
let arr3 = ["HTML", "JavaScript", "CSS"];

let sorted = copySorted(arr);

function copySorted(arr) {
    let newArr = arr.slice().sort();
    return newArr;
}

alert( sorted ); // CSS, HTML, JavaScript
alert( arr3 ); 