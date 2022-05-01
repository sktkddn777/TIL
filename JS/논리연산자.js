"use strict";

// Assignment1
alert( null || 2 || undefined ); // 2

// Assignment2
alert( alert(1) || 2 || alert(3) ); // 1, 2  alert 메서드는 값을 반환하지 않습니다. 즉, undefined를 반환하죠.

// Assignment3
alert( 1 && null && 2 ); // null

// Assignment4
alert( alert(1) && alert(2) ); //1, undefined

// Assignment5
alert( null || 2 && 3 || 4 ); //3

// Assignment6
if (age >= 14 && age <= 90) {
    alert("age");
}

// Assignment7
if (!(age >= 14 && age <= 90)) {

}

if (age < 14 || age > 90) {

}

// Assignment8
if (-1 || 0) alert( 'first' ); //first
if (-1 && 0) alert( 'second' ); // x
if (null || -1 && 1) alert( 'third' ); //third

// Assignment9
