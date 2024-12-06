<template>
  <div class="home">
    
    <div class="stats">
      <div class="stat-card" v-for="stat in stats" :key="stat.label">
        <h3>{{ stat.value }}</h3>
        <p>{{ stat.label }}</p>
      </div>
    </div>

    
    <h2>Last Projects</h2>
    <div class="projects-list">
      <div class="project-item" v-for="project in projects" :key="project.id" @click="viewTasks(project.id)" >
        <div class="project-info">
          <h3>{{ project.name }}</h3>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "../services/apiService";

export default {
  name: "HomePage",
  methods:{
    async viewTasks(projectId) {
      try {
        this.$router.push(`/project/${projectId}`);
      } catch (error) {
        console.error("Erro ao navegar para os detalhes da tarefa:", error);
      }
    },
  },
  data() {
    return {
      stats: [],
      projects: [],
    };
  },
  async created() {
    try {
      
      const clients = await apiService.getClients();
      const projects = await apiService.getProjects('?limit=5');
      const tasks = await apiService.getTasks('?status=COMPLETED');

      
      this.stats = [
        { label: "Total Projects", value: projects.length },
        { label: "Total Tasks", value: tasks.length },
        { label: "Clients", value: clients.length },
        { label: "Completed Taks", value: tasks.length},
      ];

      
      this.projects = projects;
    } catch (error) {
      console.error("Erro ao carregar os dados:", error);
    }
  },
};
</script>

<style scoped>



.stats {
  display: flex;
  gap: 16px;
  margin-bottom: 32px;
}

.stat-card {
  background: linear-gradient(45deg, #6a11cb, #2575fc);
  color: white;
  padding: 16px;
  border-radius: 8px;
  text-align: center;
  flex: 1;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.stat-card:hover {
  transform: scale(1.05);
}


.projects-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
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
  cursor: pointer;
}

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

.status.open {
  background: #f44336; 
}

.status.in_progress {
  background: #ffc107; 
}

.status.completed {
  background: #4caf50; 
}
</style>
