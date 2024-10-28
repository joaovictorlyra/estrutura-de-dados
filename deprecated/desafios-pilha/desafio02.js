function Stack() {
    var _pilha = []

    this.isEmpty = function() {
        return _pilha.length === 0;
    }

    this.push = function(element) {
        _pilha.push(element);
    }
}

let pilha = new Stack();

pilha.push(1);
pilha.push(2);
pilha.push(3);
pilha.push(4);
pilha.push(5);

console.log(pilha.isEmpty());