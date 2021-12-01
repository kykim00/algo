// 배열의 삭제
// 다음 배열에서 400, 500를 삭제하는 code를 입력하세요.

var nums = [100, 200, 300, 400, 500];

// 배열의 뒷부분을 삭제하는 방법
// 1. 배열 길이 지정
function a() {
    nums.length = 3;
}

// 2. pop으로 제거
function b() {
    nums.pop();
    nums.pop();
}

// 배열의 중간을 삭제하는 방법
// 3. array.splice(index, count, items)  >>  index부터 count 만큼의 배열을 삭제하고 items가 있으면 그자리에 추가함.
function c() {
    nums.splice(3, 2);
}

// 4. array.filter(element => element condition) >>  condition에 맞는 요소만 뽑아냄
function d() {
    let filtered = nums.filter((element) => element !== 400 && element !== 500);
}

console.log(nums);
