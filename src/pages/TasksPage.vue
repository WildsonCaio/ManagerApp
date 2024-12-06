<template>
  <div class="projects-page">
    <h1>List Taks</h1>
    <div class="projects-list">
      <div class="project-item" v-for="task in tasks" :key="task.id" @click="viewTasks(task.project)">
        
        <div class="project-info">
          <h3>{{ task.name }}</h3>
          <p>{{ task.project_name.toUpperCase() }}</p>
        </div>

        
        <span :class="'status ' + task.status.toLowerCase()">
          {{ task.status }}
        </span>

      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "../services/apiService";

export default {
  name: "TasksPage",
  data() {
    return {
      tasks: [],
    };
  },
  methods: {
    async viewTasks(projectId) {
      try {
        this.$router.push(`/project/${projectId}`);
      } catch (error) {
        console.error("Erro ao navegar para os detalhes da tarefa:", error);
      }
    },
  },
  async created() {
    try {
      this.tasks = await apiService.getTasks();
    } catch (error) {
      console.error("Erro ao carregar os projetos:", error);
    }
  },
};
</script>

<style scoped>

.projects-page {
  padding: 16px;
}

.projects-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.in_execution{
  background-color: rgb(160, 147, 147);
  padding: 5px 10px;
  border-radius: 4px;
  font-size: 0.9rem;
  font-weight: bold;
  color: white;
}


.project-item {
  
  background: #ffffff;
  padding: 16px;
  border: 1px solid #ddd;
  border-radius: 8px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease-in-out;
  cursor: pointer;
}

.project-item:hover {
  transform: scale(1.02);
background-color: rgba(243, 236, 236, 0.61);}


.project-info h3 {
  margin: 0;
  font-size: 1.2rem;
  color: #333;
}

.project-info p {
  margin: 0;
  font-size: 0.9rem;
  color: #555;
}


.status {
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 0.85rem;
  text-transform: capitalize;
  color: white;
}

.status.pending {
  background: #f44336; 
}

.status.in_progress {
  background: #ffc107; 
}

.status.completed {
  background: #4caf50; 
}


.details-button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 8px 12px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.details-button:hover {
  background-color: #0056b3;
}
</style>
