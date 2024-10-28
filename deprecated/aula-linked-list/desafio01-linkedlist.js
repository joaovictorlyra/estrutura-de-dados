class Node {
    constructor(name) {
        this.name = name;
        this.next = null;
    }

}

class WaittingList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }


    addCustomer(name_) {
        const newNode = new Node(name_);

        if (!this.head) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.tail.next = newNode;
            this.tail = newNode;
        }
        this.length++;
    }

    removeNextCustomer() {
        if (!this.head) {
            return "A fila está vazia";
        }
        const removedCustomer = this.head.name;
        this.head = this.head.next;
        this.lenght--;

        if (!this.head) {
            this.tail = null; // Se a fila ficar vazia, reseta o tail
        }
        return '${removedCustomer} foi chamada';
    }

    listCustomers() {
        if(!this.head) {
            return "A fila está vazia";
        }
        let current = this.head;
        const customers = [];
        while(current) {
            customers.push(current.name);
            current = current.next;
        }
        return "Clientes na fila: " + customers.join(", ");
        
    }
}