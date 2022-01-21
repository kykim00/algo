function solution(numbers) {
  let answer = [];
  let temp = 0;
  for (let i = 0; i < numbers.length - 1; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      temp = numbers[i] + numbers[j];
      if (!answer.includes(temp)) answer = [...answer, temp];
    }
  }
  return answer.sort((a, b) => a - b);
}
