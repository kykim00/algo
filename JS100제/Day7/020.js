let [a, b] = prompt().split(' ');

a = +a;
b = +b;
console.log(Math.floor(a/b), a%b);