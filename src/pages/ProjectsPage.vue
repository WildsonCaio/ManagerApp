<template>
  <div class="projects-page">
    <h1 class="page-title">List Project</h1>
    <div class="add-project-button-container">
      <button class="add-project-button" @click="openModal">add Project</button>
    </div>
    <div class="projects-list">
      <div v-for="project in projects" :key="project.id" class="project-card" @click="viewTasks(project.id)">
        <div class="project-details">
          <h3>{{ project.name }}</h3>
          <p>{{ getClientName(project.client) }}</p>
        </div>
        <div class="project-status">
          <span :class="statusClass(project.status)">{{ project.status }}</span>
        </div>
      </div>
    </div>

    <div v-if="showModal" class="modal-overlay" @click.self="closeModal">
      <div class="modal">
        <div class="modal-header">
          <h2>Add Project</h2>
          <button class="modal-close" @click="closeModal">×</button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="handleAddProject">
            <div class="form-group">
              <label for="project-name">Name</label>
              <input
                id="project-name"
                type="text"
                v-model="newProject.name"
                required
              />
            </div>
            <div class="form-group">
              <label for="project-client">Client</label>
              <select id="project-client" v-model="newProject.client" required>
                <option value="" disabled>Select client</option>
                <option v-for="client in clients" :key="client.id" :value="client.id">
                  {{ client.user.username }}
                  
                </option>
              </select>
            </div>
            <div class="form-group">
              <label for="project-team">Team</label>
              <select id="project-team" v-model="newProject.team" required>
                <option value="" disabled>Selecione o time</option>
                <option v-for="team in teams" :key="team.id" :value="team.id">
                  {{ team.name }}
                </option>
              </select>
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button class="cancel-button" @click="closeModal">Cancel</button>
          <button class="add-button" @click="handleAddProject">Add</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "../services/apiService";

export default {
  name: "ProjectsPage",
  data() {
    return {
      projects: [],
      clients: [],
      teams: [],
      showModal: false,
      newProject: {
        name: "",
        client: "",
        team: "",
        start_date: new Date().toISOString().split('T')[0], 
      },
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
    
    async fetchProjects() {
      try {
        this.projects = await apiService.getProjects();
      } catch (error) {
        console.error("Erro ao carregar os projetos:", error);
      }
    },
    async fetchClients() {
      try {
        this.clients = await apiService.getClients();
      } catch (error) {
        console.error("Erro ao carregar os clientes:", error);
      }
    },
    async fetchTeams() {
      try {
        this.teams = await apiService.getTeams();
      } catch (error) {
        console.error("Erro ao carregar os times:", error);
      }
    },
    openModal() {
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
    },
    statusClass(status) {
      return {
        OPEN: "status-open",
        PENDING: "status-in-progress",
        COMPLETED: "status-completed",
      }[status] || "";
    },
    getClientName(clientId) {
      const client = this.clients.find((c) => c.id === clientId);
      return client ? client.name : "Desconhecido";
    },
    async handleAddProject() {
      try {
        await apiService.createProject(this.newProject);
        this.closeModal();
        this.fetchProjects();
      } catch (error) {
        console.error("Erro ao adicionar o projeto:", error);
      }
    },
  },
  async created() {
    await this.fetchProjects();
    await this.fetchClients();
    await this.fetchTeams();
  },
};
</script>

<style scoped>

.projects-page {
  padding: 16px;
}

.page-title {
  font-size: 2rem;
  margin-bottom: 16px;
  color: #333;
  text-align: center;
}

.add-project-button-container {
  text-align: left; 
  margin-bottom: 16px;
}

.add-project-button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.add-project-button:hover {
  background-color: #0056b3;
}

.projects-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.project-card {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #ffffff;
  padding: 16px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  cursor: pointer;
}

.project-details h3 {
  margin: 0;
  font-size: 1.2rem;
  color: #333;
}

.project-details p {
  margin: 4px 0 0;
  font-size: 0.9rem;
  color: #555;
}

.project-status{
  background-color: rgb(160, 147, 147);
  padding: 5px 10px;
  border-radius: 4px;
  font-size: 0.9rem;
  font-weight: bold;
  color: white;
}

.project-status span {
  padding: 5px 10px;
  border-radius: 4px;
  font-size: 0.9rem;
  font-weight: bold;
  color: white;
}

.status-open {
  background-color: #dc3545;
}

.status-in_execution {
  background-color: #ffc107;
  color: #333;
}

.in_execution {
  background-color: #ffc107;
  color: #333;
}

.status-completed {
  background-color: #28a745;
}


.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}


.modal {
  background: white;
  border-radius: 8px;
  padding: 20px;
  width: 400px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.modal-close {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
}

.modal-body .form-group {
  margin-bottom: 15px;
}

.modal-body input,
.modal-body select {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 1rem;
  transition: border-color 0.3s ease;
}

.modal-body input:focus,
.modal-body select:focus {
  border-color: #007bff;
  outline: none;
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}

.cancel-button {
  background: #dc3545;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  cursor: pointer;
}

.add-button {
  background: #007bff;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  cursor: pointer;
}
</style>
