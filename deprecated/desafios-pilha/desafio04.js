function Delimitadores(str) {
    let stack = [];
    let map = {
       '(' : ')',
       '[' : ']',
       '{' : '}'
    }

    for (let i = 0; i < str.length; i++) {
        let char  = str[i];
        if (char === '(' || char === '[' || char === '{') {
            stack.push(char);
        } else if (char === ')' || char === ']' || char === '}') {
            if (stack.length === 0 || stack.pop() !== map[char]) {
                return false;
            }
        }
    }
    return stack.length === 0;
}

console.log(Delimitadores("{[(}"));
console.log(Delimitadores("{[()]}"));

