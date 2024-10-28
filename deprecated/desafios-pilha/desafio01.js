function Stack() {
    var items = [];
    this.push = function(element) {
        items.push(element);
        console.log(items);
    }

    this.pop = function() {
        items.pop();
        console.log(items);
    }
}

let pilha = new Stack();
pilha.push(1);
pilha.push(2);
pilha.push(3);
pilha.push(4);
pilha.push(5);

pilha.pop();