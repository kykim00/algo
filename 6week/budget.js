function solution(d, budget) {
  d.sort((a, b) => a - b);
  let sum = 0;
  let result = 0;
  for (const i of d) {
    sum += i;
    if (sum > budget) {
      return result;
    }
    result += 1;
  }
  return result;
}
