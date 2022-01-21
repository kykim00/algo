function solution(n) {
  let three = n.toString(3);
  let temp = "";
  for (let i of three) {
    temp = i + temp;
  }
  return parseInt(temp, 3);
}
