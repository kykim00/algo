// 다음 소스 코드를 concat을 사용하여 날짜와 시간을 출력하시오.

var year = '2019';
var month = '04';
var day = '26';
var hour = '11';
var minute = '34';
var second = '27';

// 빈칸을 채워주세요
// str1.concat(str2, str3, str4...) >> str1에 str2, str3, str4를 연결하여 하나의 문자열로 만듦
var result = year.concat('/',month,'/',day,' ',hour,':',minute,':',second)

console.log(result);

// 출력
// 2019/04/26 11:34:27