let str = prompt();

// 1.
let temp = '';
for (let c of str) {
    temp = c + temp;
}
console.log(temp);

// 2. split : 문자열 메서드. 문자열 -> 배열
//    reverse : 배열 메서드. 배열을 순서를 거꾸로
//    join : 배열 메서드. 배열 -> 문자열
temp = str.split('').reverse().join('');
console.log(temp);