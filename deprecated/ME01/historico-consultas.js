function Stack() {
    let historicoMedico = [];
    let quantidadeDeConsultas = 0;

    this.push = (medico, paciente, especialidadeMedico) => {
        let historicoObj = {};
        historicoObj.medico = medico;
        historicoObj.paciente = paciente;
        historicoObj.especialidadeMedico = especialidadeMedico;
        historicoObj.quantidadeConsultas = quantidadeDeConsultas++;
        historicoObj.horario = new Date();

        return historicoMedico.push(historicoObj);
    }

    this.visualizarHistoricoPorPaciente = (paciente) => {
        const historicoPaciente = historicoMedico.filter(consulta => consulta.paciente === paciente);
        if (historicoPaciente.length === 0) {
            console.log(`Nenhum histórico encontrado para o paciente: ${paciente}`);
        } else {
            console.log(`Histórico do paciente ${paciente}:`, historicoPaciente);
        }
        return historicoPaciente;
    }

    this.print = () => {
        console.log(historicoMedico);
    }

    this.visualizarUtltimaConsulta = () => {
        let ultimaConsulta = historicoMedico[historicoMedico.length - 1];
        console.log(`A última consulta foi:`, ultimaConsulta);
        return ultimaConsulta;
    }

    this.removerUltimaConsulta = () => {
        if (historicoMedico.length > 0) {
            let consultaRemovida = historicoMedico.pop();
            console.log(`Consulta removida:`, consultaRemovida);
            return consultaRemovida;
        } else {
            console.log("Não há consultas para remover.");
        }
    }
}

let pilha = new Stack();

// Adicionando pacientes
pilha.push("Alfredo", "Wagner", "Cardiologista");
pilha.push("Medico 2", "Paciente 3", "Dermatologista");
pilha.push("Medico 3", "Wagner", "Neurologista");

// Visualizando ultima consulta
pilha.visualizarUtltimaConsulta();

/*
A última consulta foi: {
  medico: 'Medico 3',
  paciente: 'Wagner',
  especialidadeMedico: 'Neurologista',
  quantidadeConsultas: 2,
  horario: 2024-09-24T17:06:40.815Z
}
*/

pilha.print();

/* 
[
  {
    medico: 'Alfredo',
    paciente: 'Wagner',
    especialidadeMedico: 'Cardiologista',
    quantidadeConsultas: 0,
    horario: 2024-09-24T17:06:40.815Z
  },
  {
    medico: 'Medico 2',
    paciente: 'Paciente 3',
    especialidadeMedico: 'Dermatologista',
    quantidadeConsultas: 1,
    horario: 2024-09-24T17:06:40.815Z
  },
  {
    medico: 'Medico 3',
    paciente: 'Wagner',
    especialidadeMedico: 'Neurologista',
    quantidadeConsultas: 2,
    horario: 2024-09-24T17:06:40.815Z
  }
]
*/

pilha.visualizarHistoricoPorPaciente("Wagner");
/* 
Histórico do paciente Wagner: [
  {
    medico: 'Alfredo',
    paciente: 'Wagner',
    especialidadeMedico: 'Cardiologista',
    quantidadeConsultas: 0,
    horario: 2024-09-24T17:09:21.954Z
  },
  {
    medico: 'Medico 3',
    paciente: 'Wagner',
    especialidadeMedico: 'Neurologista',
    quantidadeConsultas: 2,
    horario: 2024-09-24T17:09:21.954Z
  }
]
*/

pilha.removerUltimaConsulta("Wagner");

/* 
Consulta removida: {
  medico: 'Medico 3',
  paciente: 'Wagner',
  especialidadeMedico: 'Neurologista',
  quantidadeConsultas: 2,
  horario: 2024-09-24T17:08:05.886Z
}
*/