"use strict";

// Assignment1
function checkAge(age) {
    if (age > 18) {
      return true;
    }
    // ...
    return confirm('보호자의 동의를 받으셨나요?');
  }

// Assignment2
function checkAge(age) {
    return (age > 18) ? true : confirm('보호자의 동의를 받으셨나요?');
}


// Assignment3
function min(a, b) {
    return (a>b)?b:a;
}

// Assignment4
function pow(x, n) {
    let res = 1;
    while (n > 0) {
        res *= x;
        n--;
    }
    return res;
}