function Queue() { //funcao
    var items = [] //array vazio 

    //metodos
    this.enqueue = function(element) {
        // add um novo item
        items.push(element)
    }

    this.dequeue = function() {
        //remove um item
        return items.shift()
    }

    this.front = function() {
        //retorno o 1º elemento da fila
        return items[0]
    }

    this.isEmpty = function() {
        //verificar se a fila está vazia ou não
        if (items.length === 0) {
            console.log("A fila está vazia");
        } else {
            console.log("A fila tem elementos");
        }
    }

    this.size = function() {
        //retorna o tamanho da fila 
        return items.length
    }

    this.print = function() {
        //imprimir a fila no console
        console.log(items.toString())
    }

    this.end = function() {
        //retorna o último elemento da fila
        return items[items.length - 1];
    }

    
}

// QUESTÃO 1:
var fila = new Queue();

fila.enqueue('Carlos');
fila.enqueue('Ana');
fila.enqueue('Cícero');


fila.dequeue();
fila.print();
console.log(fila.isEmpty());
console.log(fila.size());
console.log(fila.front());

// QUESTÃO 2:
var fila2 = new Queue();
fila2.enqueue('Carlos');
fila2.enqueue('Ana');
fila2.enqueue('Cícero');
fila2.enqueue('Bia');
fila2.enqueue('Diego');

fila2.dequeue();
console.log(fila2.front());
console.log(fila2.size());


//QUESTÃO 3:

fila3.enqueue('Carlos');
fila3.enqueue('Ana');
fila3.enqueue('Cícero');
fila3.enqueue('Bia');
fila3.enqueue('Diego');

fila3.dequeue();
console.log(fila3.size());
console.log(fila3.front());

//QUESTÃO 4:
var fila4 = new Queue();

fila4.enqueue('Carlos');
fila4.enqueue('Ana');
fila4.enqueue('Cícero');
fila4.enqueue('Bia');
fila4.enqueue('Diego');

fila4.isEmpty();

//QUESTÃO 5:
function moveTwoToEnd(queue) {
    if (queue.size() >= 2) {
        let first = queue.dequeue();  // Remove o primeiro elemento
        let second = queue.dequeue(); // Remove o segundo elemento
        queue.enqueue(first);         // Adiciona o primeiro no final
        queue.enqueue(second);        // Adiciona o segundo no final
    }
}

// Testando a Questão 5
var fila5 = new Queue();
fila5.enqueue('Carlos');
fila5.enqueue('Ana');
fila5.enqueue('Cícero');
fila5.enqueue('Bia');
fila5.enqueue('Diego');

console.log("Fila antes de mover os dois primeiros elementos:");
fila5.print();

moveTwoToEnd(fila5);

console.log("Fila depois de mover os dois primeiros elementos para o final:");
fila5.print();




// //QUESTÃO 6:
var fila6 = new Queue();

fila6.enqueue('Carlos');
fila6.enqueue('Ana');
fila6.enqueue('Cícero');
fila6.enqueue('Bia');
fila6.enqueue('Diego');

console.log(fila6.end());




