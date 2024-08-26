function Stack() {
    var _pilha = [];
    
    this.push = function(element) {
        _pilha.push(element);
    }
    
    this.pop = function() {
        return _pilha.pop();
    }

    this.isEmpty = function() {
        return _pilha.length === 0;
    }

    this.reverterString = function(str) {
        return str.split('').reverse().join('');
    }
}

function isPalindrome(str) {
    let pilha = new Stack();
    let stringReversa = pilha.reverterString(str);
    
    return str === stringReversa;
}

let palavra = "radar";
console.log(isPalindrome(palavra)); // true

palavra = "hello";
console.log(isPalindrome(palavra)); // false
