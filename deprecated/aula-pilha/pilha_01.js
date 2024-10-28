function Stack() {
    var items = []

    this.push = function(element) {
        // Adiciona um item na pilha
        items.push(2)
    }

    this.pop = function() {
        // Remove um item do topo da pilha
        return items.pop();
    }

    this.peek = function() {
        // Devolve item do topo da pilha
        return items[items.length - 1];
    }

    this.isEmpty = function() {
        // Retorna se a função é vazia
        return items.length === 0;
    }

    this.clear = function() {
        // Limpa a pilha
        items = [];
    }

    this.size = function() {
        // Retorna o tamanho da pilha

    }

    this.print = function() {
        // Imprime a pilha
        console.log(items.toString);
    }
}

var pilha = new Stack();

pilha.push(2);
pilha.push(3);
pilha.push(5);
pilha.push(6);
pilha.push(10);

pilha.pop(10);


