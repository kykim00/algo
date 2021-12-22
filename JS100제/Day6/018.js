let [a, b, c] = prompt().split(' ');
// a, b, c를 반복문 없이 한번에 바꿀 수 없을까
a = +a;
b = +b;
c = +c;
console.log((a+b+c)/3);