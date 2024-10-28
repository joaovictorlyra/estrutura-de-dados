class TaskManager {
    constructor() {
      this.tasks = []; // Lista de tarefas
      this.currentId = 1; // ID único para cada tarefa
    }
  
    // Cria uma nova tarefa
    addTask(title, description, status = 'pendente', tags = []) {
      const task = {
        id: this.currentId++,
        title,
        description,
        status,
        tags: new Set(tags) // Usando Set para garantir que as tags não sejam duplicadas
      };
      this.tasks.push(task);
      return task;
    }
  
    // Atualiza uma tarefa existente
    updateTask(id, newTitle, newDescription, newStatus, newTags) {
      const task = this.tasks.find(task => task.id === id);
      if (task) {
        task.title = newTitle || task.title;
        task.description = newDescription || task.description;
        task.status = newStatus || task.status;
        if (newTags) {
          task.tags = new Set(newTags);
        }
        return task;
      }
      return null;
    }
  
    // Remove uma tarefa
    removeTask(id) {
      this.tasks = this.tasks.filter(task => task.id !== id);
    }
  
    // Filtra tarefas por estado
    filterTasksByStatus(status) {
      return this.tasks.filter(task => task.status === status);
    }
  
    // Adiciona tags a uma tarefa
    addTagsToTask(id, tags) {
      const task = this.tasks.find(task => task.id === id);
      if (task) {
        tags.forEach(tag => task.tags.add(tag));
        return task;
      }
      return null;
    }
  
    // Remove tags de uma tarefa
    removeTagsFromTask(id, tags) {
      const task = this.tasks.find(task => task.id === id);
      if (task) {
        tags.forEach(tag => task.tags.delete(tag));
        return task;
      }
      return null;
    }
  
    // Lista todas as tags e as tarefas associadas a cada uma
    listTags() {
      const tagMap = new Map();
      this.tasks.forEach(task => {
        task.tags.forEach(tag => {
          if (!tagMap.has(tag)) {
            tagMap.set(tag, []);
          }
          tagMap.get(tag).push(task);
        });
      });
      return tagMap;
    }
  }
  

  const taskManager = new TaskManager();
  
  taskManager.addTask('Tarefa 1', 'Descrição 1');
  taskManager.addTask('Tarefa 2', 'Descrição 2', 'em progresso', ['urgente']);
  
  taskManager.updateTask(1, 'Tarefa 1 atualizada', null, 'concluída');
  
  console.log(taskManager.filterTasksByStatus('concluída'));
  
  taskManager.addTagsToTask(1, ['importante']);
  taskManager.removeTagsFromTask(2, ['urgente']);
  
  console.log(taskManager.listTags());
  