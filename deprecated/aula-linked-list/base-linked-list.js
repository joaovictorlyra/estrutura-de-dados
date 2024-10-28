function LinkedList() {
    var Node = function(element) {
        this.element = element;
        this.next = null;
    }

    var length = 0;
    var head = null;

    this.append = function(element) {
        // Adiciona um elemento no final da lista
        var node = new Node(element);
        var current;

        if (head === null) {
            head = node;
        } else {
            current = head;

            while (current.next) {
                current = current.next;
            }
            current.next = node;
        }

        length++;
    }

    this.insert = function(position, element) {
        // Adiciona um elemento em uma posição específica da lista
        if (position >= 0 && position <= length) {
            var node = new Node(element),
                current = head,
                previous,
                index = 0;

            if (position === 0) {
                node.next = head;
                head = node;
            } else {
                while (index++ < position) {
                    previous = current;
                    current = current.next;
                }
                node.next = current;
                previous.next = node;
            }

            length++;
            
            return true;
        } else {
            return false;
        }
    }

    this.removeAt = function(position) {
        // Remove o elemento de uma posição específica
        if (position >= 0 && position < length) {
            var current = head,
                previous,
                index = 0;

            if (position === 0) {
                head = current.next;
            } else {
                while (index++ < position) {
                    previous = current;
                    current = current.next;
                }
                previous.next = current.next;
            }

            length--;
            return current.element;
        } else {
            return null;
        }
    }

    this.remove = function(element) {
        // Remove o elemento da lista (não pela posição)
        var index = this.indexOf(element);
        return this.removeAt(index);
    }

    this.indexOf = function(element) {
        // Retorna a posição do elemento
        var current = head,
            index = 0;

        while (current) {
            if (current.element === element) {
                return index;
            }
            index++;
            current = current.next;
        }

        return -1;
    }

    this.isEmpty = function() {
        // Verifica se a lista está vazia
        return length === 0;
    }

    this.size = function() {
        // Retorna o tamanho da lista
        return length;
    }

    this.getHead = function() {
        // Retorna o primeiro elemento (head)
        return head;
    }

    this.toString = function() {
        // Converte a lista em uma string
        let current = head, string = '';
        while (current) {
            string += current.element + ' ';
            current = current.next;
        }
        return string.trim();
    }

    this.print = function() {
        // Imprime a lista no console
        console.log(this.toString());
    }
}

// teste
let ll = new LinkedList();
ll.append('Pedro');
ll.append('Ana');
ll.append('Maria');

ll.print(); // Saída: "Pedro Ana Maria"

console.log('Index de Ana:', ll.indexOf('Ana')); // Saída: 1
ll.removeAt(1); // Remove "Ana"
ll.print(); // Saída: "Pedro Maria"
console.log('Tamanho:', ll.size()); // Saída: 2

ll.insert(2, "Carlos");
ll.print()