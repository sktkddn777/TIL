"use strict"

// find str
let str = "Widget";

if (~str.indexOf("Widget")) {
  alert( '찾았다!' ); // 의도한 대로 동작합니다. -> 추천 X
}


// 문자열 찾기. -> slice만 알아도 무방

// Assignment1
function ucFirst(str) {
    if (!str) return str;

    return str[0].toUpperCase() + str.slice(1);
}
ucFirst("john") == "John";

// Assignment2
function checkSpam(str) {
    let lowerStr = str.toLowerCase();
    return (lowerStr.includes('viagra') || lowerStr.includes('xxx'))   
}

// Assignment3
function truncate(str, maxlength) {
    if (str.length < maxlength)
        return str;
    return str.slice(0, maxlength - 1) + '...';
}

// Assignment4
function extractCurrencyValue(str) {
    return +(str.slice(1));
}