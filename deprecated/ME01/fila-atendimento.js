function Queue() {
    let pacientes = [];
    let condicaoGrave = false;
    
    this.push = (paciente) => {
        let pacienteObj = {};
        pacienteObj.paciente = paciente;
        pacienteObj.condicaoGrave = condicaoGrave;
        return pacientes.push(pacienteObj);
    }

    this.shift = () => {
        return pacientes.shift();
    }
    
    this.pacienteGraveInicioDaFila = (paciente) => {
        let indexPacienteEncontrado = pacientes.findIndex(p => p.paciente === paciente && p.condicaoGrave === true);

        if (indexPacienteEncontrado !== -1) {
            console.log(`Adicionando paciente ${paciente} na primeira posição`);
            let pacienteGrave = pacientes.splice(indexPacienteEncontrado, 1)[0]; // Remove o paciente do array
            pacientes.unshift(pacienteGrave); // Adiciona no início da fila
        }  else {
        console.log("Paciente não encontrado ou não está em condição grave.");
            }
    }

    this.proximoPacienteParaSerAtendido = () => {
        return pacientes[1];
    }

    this.mudandoCondicaoGrave = (paciente) => {
        let pacienteEncontrado = pacientes.find(p => p.paciente === paciente);
        if (pacienteEncontrado) {
            pacienteEncontrado.condicaoGrave = true;
        } else {
            console.log("Paciente não encontrado.");
        }
    }

    this.print = () => {
        console.log(pacientes);
    }
  
}

// Instânciando a fila
let filaPacientes = new Queue();

// adicionando pacientes
filaPacientes.push("Kaio");
filaPacientes.push("William");

// Mudando a condição do paciente
filaPacientes.mudandoCondicaoGrave("William");
// Colocando paciente com condição grave no início da fila
filaPacientes.pacienteGraveInicioDaFila("William");

// Mostrando a fila no console
filaPacientes.print();

/*Adicionando paciente William na primeira posição
[
  { paciente: 'William', condicaoGrave: true },
  { paciente: 'Kaio', condicaoGrave: false }
]
*/

// Removendo paciente 
filaPacientes.shift();

filaPacientes.proximoPacienteParaSerAtendido();
// [ { paciente: 'Kaio', condicaoGrave: false } ]

// Mostrando a fila no console
filaPacientes.print();