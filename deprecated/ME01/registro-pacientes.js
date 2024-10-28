function Paciente(nome) {
    this.nome = nome;      // Nome do paciente
    this.next = null;      // Próximo nó (paciente) na lista
}


function LinkedList() {
    this.head = null;      // Início da lista
    this.tail = null;      // Final da lista

    
    this.adicionarPaciente = (nome) =>  {
        let novoPaciente = new Paciente(nome);
        
        if (this.head === null) {
            // Se a lista estiver vazia, o novo paciente será o primeiro
            this.head = novoPaciente; // inicio
            this.tail = novoPaciente; // fim
        } else {
            // Adiciona o novo paciente no final da lista
            this.tail.next = novoPaciente;
            this.tail = novoPaciente;
        }
        console.log(`Paciente ${nome} adicionado à lista.`);
    }

    this.listarPacientes = () => {
        if (this.head === null) {
            console.log("Nenhum paciente na lista.");
            return;
        }
        
        let atual = this.head;
        console.log("Pacientes na lista:");
        while (atual !== null) {
            console.log(`- ${atual.nome}`);
            atual = atual.next;
        }
    }
}

// Exemplo de uso:
let listaPacientes = new LinkedList();

// Adicionando pacientes
listaPacientes.adicionarPaciente("João");
listaPacientes.adicionarPaciente("Maria");
listaPacientes.adicionarPaciente("Carlos");

/* 
Paciente João adicionado à lista.
Paciente Maria adicionado à lista.
Paciente Carlos adicionado à lista.
*/

// Mostrando pacientes no console
listaPacientes.listarPacientes();

/* 
Pacientes na lista:
- João
- Maria
- Carlos
*/