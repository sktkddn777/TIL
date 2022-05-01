"use strict";

// Assignment1
let user = {};
user["name"] = "John";
user["surname"] = "Smith";

user["name"] = "Pete"
delete user.name;
delete user.surname;
// Assignment2
function isEmpty(obj) {
    if (Object.keys(obj).length == 0)
        return true;
    return false;
}

console.log(isEmpty(user));

// Assignment3
// const user = {
//     name: "John"
//   };
//   // 아래 코드는 에러 없이 실행될까요?
//   user.name = "Pete";

// Assignment4

let salaries = {
    John: 100,
    Ann: 160,
    Pete: 130
}

function sumSalaries(obj) {
    let res = 0;
    for (let key in obj) {
        res += obj[key];
    }
    return res;
}

console.log(sumSalaries(salaries));

// Assignment5
let menu = {
    width: 200,
    height: 300,
    title: "My menu"
  };

function multiplyNumeric(obj) {
    for (let key in obj) {
        if (typeof(obj[key]) == 'number')
            obj[key] *= 2;
    }
}

multiplyNumeric(menu);
for (let k in menu) {
    console.log(menu[k]);
}


// Assignment6
function makeUser() {
    return {
      name: "John",
      ref() { return this },
    };
  };
  
  let user6 = makeUser();
  
  console.log( user6.ref().name ); // John

// Assignment7
let calculator = {
    num1 : 0,
    num2 : 0,
    read() {
        this.num1 = prompt("enter num1");
        this.num2 = prompt("enter num2");
    },

    sum() {
        return this.num1 + this.num2;
    },

    mul() {
        return this.num1 * this.num2;
    }
}


calculator.read();
console.log(calculator.sum());
console.log(calculator.mul());

// Assignment8
let ladder = {
    step: 0,
    up() {
      this.step++;
      return this;
    },
    down() {
      this.step--;
      return this;
    },
    showStep() {
      alert( this.step );
      return this;
    }
  }

