/**
 * @param {number} x
 * @return {number}
 */
const max = Math.pow(2,31) -1 ;
const min = Math.pow(2,31) * -1;

var reverse = function(x) {
    var isNegative = (x < 0);
    var numArray = x.toString().split('');
    if(isNegative){
        numArray = numArray.slice(1);
    }

    //reverse the digit
    numArray = numArray.reverse();

    if(isNegative){
        numArray.unshift("-");
    }

    var reversedNum = parseInt(numArray.join(''));

    if(reversedNum < min || reversedNum > max){
        return 0;
    }
    else{
        return reversedNum;
    }
};