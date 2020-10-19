"use strict";

let num = 50; 

switch (num) {
    case 49:
        console.log('NOt good');
        break;
    case 100:
        console.log('NOt good');
        break;
    case 100:
        console.log('NOt good');
        break;
    default:
        console.log('NOt today');
        break;

}

while (num <= 55) {
    console.log(num);
    num++;
}

do {
    console.log(num);
    num++;
}
while (num <= 55);


for (let i =1; i < 8; i++) {
    console.log(num);
    num++;
}

let logg = 'Hello world';
logg = logg.toUpperCase();
//logg = logg.slice(6, 11); //вырезать с символа по
//logg = logg.substring(6, 11); //вырезать с символа по
logg = logg.substr(6, 4); // вырезать с символа, кол-во символов которое нужно вырезать
console.log(logg.length);
console.log(logg.indexOf("RL"));// поиск индекска где начинается наша буква или слово
console.log(logg);

const numb = 12.2;
console.log(Math.round(numb));
const test = "12.2px";
console.log(parseInt(test));
console.log(parseFloat(test));



function learnJS(lang, callback) {
    console.log(`Я учу: ${lang}`);
    callback();
}

learnJS('JavaScript', function() {
    console.log('Я прошел это урок!');
});

function done() {
    console.log('Я прошел это урок!');
}

learnJS('Javascript', done);

const options = {
    name: 'test',
    width: 1024,
    height: 1024,
    colors: {
        border: 'black',
        bg: 'red'
    },
    makeTest: function() {
        console.log('Make test');
    }
};

options.makeTest();

const {border, bg} = options.colors;
console.log(border);
console.log(bg);
console.log(options);
delete options.name;
console.log(options);

//console.dir()

for (let key in options) {
    if (typeof(options[key] === 'object')) {
        for (let i in options[key]) {
            console.log(`Свойство ${key} имеет значение ${options[key][i]}`);
        }
    } else {
        console.log(`Свойство ${key} имеет значение ${options[key]}`);
    }
}
    

console.log(Object.keys(options));
console.log(Object.keys(options).length);


const arr = [1, 2, 3, 4, 6, 8];

function compareNum(a, b) {
    return a -b;
}
arr.sort(compareNum);
console.log(arr);

arr.pop();// удаляет

arr.push(10);// добавляет
console.log(arr);

for (let i = 0; i < arr.length; i++) {
    console.log(arr[i]);
}

for (let value of arr) {
    console.log(value);
}

arr.forEach(function(item, i, arr){
    console.log(`${i}: ${item} внутри массива ${arr}`);
});

const str = prompt("", "");
const products = str.split(', ');
products.sort();
console.log(products);
console.log(products.join(; ));

function copy(mainObj) {
    let objCopy = {};

    let key;
    for (key in mainObj) {
        objCopy[key] = mainObj[key]
    }
    return objCopy;
}

// Dinamic typeisation
//To String
console.log(typeof(String(null)));
console.log(typeof(String(4)));
console.log(typeof(String(null)));

console.log(typeof(null + ''));
const numbe = 5;

console.log("https://vk.com/catalog/" + numbe);

const fonSize = 26 + 'px';

// To Number
console.log(typeof(Number('4')));

console.log(typeof(+'4'));

console.log(typeof(parseInt('15px, 10')));

let asnw = +prompt("Hello", "");

//To boolean
//false
// 0, '', null, undefined, Nan;

//true
//1
let switcher = null;

if (switcher) {
    console.log('Working...');
}

switcher = 1;

if (switcher) {
    console.log('Working...');
}

//2
console.log(typeof(Boolean('4')));

//3
console.log(typeof(!!'444'));
console.log(!!'444');

//-----------------------
//[] + false - null + true;

console.log(typeof([] + false)); //string
console.log(('' + false)); // false
console.log(('' + false)); // false

console.log(typeof([] + false - null)); //number
console.log(([] + false - null)); //NaN
console.log(([] + false - null + true)); //NaN

let y =1;
let x = y = 2;
console.log(x);
alert(x);

console.log([] + 1 + 2); // "12"

console.log("1"[0]); // 1
console.log("41"[0]); // 4

console.log(2 && 1 && null && 0 && undefined); // null И ЗАПИНАЕТСЯ НА ЛЖИ И ВОЗВРАЩАЕТ ЕЁ, НЕ ПРОДОЛЖАЯ ДАЛЬШЕ ПРОВЕРКУ
console.log(!!(1 && 2)=== (1 && 2)); // false

console.log(null || 2 && 3 || 4); // ответ 3 -- и возвращает последнее правдивое значение (3) или запинается на правде, возвращает (3), 3 или 4 и тог и то правда, или запинается на (3) и возвращает 3

const a = [1, 2, 3]; // разные ящики с одинаковым наполнением
const b = [1, 2, 3];

console.log(a == b); // false

console.log(+"Infinity");
console.log(typeof(+"Infinity"));

console.log("Ёжик" > "яблоко"); // false сравнение по таблице символов

console.log(0 || '' || 2 || undefined || true); // или запинается на правде, т.е ответ 2