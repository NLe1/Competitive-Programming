/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    var stack = [];
    //iterating over characters in string s
    for (var i = 0; i <s.length; i++){
        //if character is opening bracket push into the stack
        if(s.charAt(i) === '{' || s.charAt(i) === '[' || s.charAt(i) === '('){
            stack.push(s.charAt(i))
        }
        //if character is closing bracket, check the stack
        if(s.charAt(i) === '}' || s.charAt(i) === ']' || s.charAt(i) === ')'){
            if(getOpeningTag(s.charAt(i)) === stack.pop()){
                //if true, pop the element out of the stack
                continue;
            }else{
                return false;
            }
        }
    }

    if(stack.length === 0)
        return true;
    else{
        return false;
    }
};

var getOpeningTag = function(s) {
    switch (s) {
           case '}':
            return '{';
        case ']':
            return '[';
        case ')':
            return '(';
        default:
            return '';
    }
}