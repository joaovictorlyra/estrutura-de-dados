function PriorityQueue() {
    this.queue = []; // Inicializa a fila como uma lista vazia
  }
  
  // Adiciona um elemento à fila com uma prioridade associada
  PriorityQueue.prototype.enqueue = function(element, priority) {
    const item = { element: element, priority: priority };
    this.queue.push(item); // Insere o novo item na fila
  };
  
  // Remove e retorna o elemento com a maior prioridade
  PriorityQueue.prototype.dequeue = function() {
    if (this.isEmpty()) {
      return "A fila está vazia.";
    }
  
    let highestPriorityIndex = 0;
  
    // Encontrar o índice do elemento com a maior prioridade
    for (let i = 1; i < this.queue.length; i++) {
      if (this.queue[i].priority > this.queue[highestPriorityIndex].priority) {
        highestPriorityIndex = i;
      }
    }
  
    // Remove e retorna o elemento de maior prioridade
    const highestPriorityItem = this.queue.splice(highestPriorityIndex, 1);
    return highestPriorityItem[0].element;
  };
  
  // Verifica se a fila está vazia
  PriorityQueue.prototype.isEmpty = function() {
    return this.queue.length === 0;
  };
  
  // Imprime todos os elementos da fila com suas prioridades
  PriorityQueue.prototype.print = function() {
    if (this.isEmpty()) {
      console.log("A fila está vazia.");
    } else {
      for (let i = 0; i < this.queue.length; i++) {
        console.log("Elemento:", this.queue[i].element, ", Prioridade:", this.queue[i].priority);
      }
    }
  };
  
  // Exemplo de uso:
  const pq = new PriorityQueue();
  pq.enqueue("Tarefa 1", 2);
  pq.enqueue("Tarefa 2", 5);
  pq.enqueue("Tarefa 3", 1);
  
  pq.print();  // Imprime os elementos da fila com suas prioridades
  
  console.log("Removido:", pq.dequeue()); // Remove e retorna o elemento de maior prioridade
  pq.print();  // Imprime a fila atualizada
  