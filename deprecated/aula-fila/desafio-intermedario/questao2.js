function isInOrder(queue) {
    // Verifica se a fila está vazia ou tem apenas um elemento
    if (queue.length <= 1) {
      return true;
    }
  
    // Percorre a fila e verifica se está em ordem crescente
    for (let i = 0; i < queue.length - 1; i++) {
      if (queue[i] > queue[i + 1]) {
        return false; // Se encontrar um elemento fora de ordem, retorna false
      }
    }
  
    return true; // Se nenhum elemento estiver fora de ordem, retorna true
  }
  
  // Exemplo de uso:
  const queue = ["A", "B", "C", "D"];
  console.log(isInOrder(queue)); // true
  
  const queue2 = ["A", "C", "B", "D"];
  console.log(isInOrder(queue2)); // false
  