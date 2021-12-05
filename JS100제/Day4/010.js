const n = prompt();
let answer = '';

for (let i = 0; i < n; i++) {
    let star = '';
    star += ' '.repeat(n - 1 - i);
    for (let j = 0; j < i*2 + 1; j++) {
        star += '*';
    }
    answer += star + '\n';
}
console.log(answer)