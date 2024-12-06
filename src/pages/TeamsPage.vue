<template>
  <div class="projects-page">
    <h1>Teams</h1>
    <button class="add-team-button" @click="openModal">Add Team</button>
    <div class="projects-list">
      <div class="project-item" v-for="team in teams" :key="team.id" @click="openEditModal(team)">
        <div class="project-info">
          <h3>{{ team.name }}</h3>
          <p>{{ team.users.length }} Users</p>
        </div>
      </div>
    </div>

    <div v-if="showModal" class="modal-overlay" @click.self="closeModal">
      <div class="modal">
        <div class="modal-header">
          <h2>{{ isEditing ? "Editar Time" : "Adicionar Time" }}</h2>
          <button class="modal-close" @click="closeModal">×</button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="handleSaveTeam">
            <div class="form-group">
              <label for="team-name">Name</label>
              <input id="team-name" type="text" v-model="newTeam.name" required />
            </div>
            <div class="form-group">
              <label for="users">Users</label>
              <select id="users" v-model="newTeam.users" multiple class="select-multiple" required>
                <option v-for="user in users" :key="user.id" :value="user.id">
                  {{ user.username }}
                </option>
              </select>


            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button class="cancel-button" @click="closeModal">CAncel</button>
          <button class="add-button" @click="handleSaveTeam">
            {{ isEditing ? "Update team" : "Add" }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "../services/apiService";

export default {
  name: "TeamsPage",
  data() {
    return {
      teams: [],
      users: [],
      showModal: false,
      isEditing: false,
      selectedTeamId: null,
      newTeam: {
        name: "",
        users: [],
      },
    };
  },
  methods: {
    async fetchTeams() {
      try {
        this.teams = await apiService.getTeams();
      } catch (error) {
        console.error("Erro ao carregar os times:", error);
      }
    },
    async fetchUsers() {
      try {
        this.users = await apiService.getUsers();
      } catch (error) {
        console.error("Erro ao carregar os usuários:", error);
      }
    },
    openModal() {
      this.isEditing = false;
      this.selectedTeamId = null;
      this.newTeam = { name: "", users: [] };
      this.showModal = true;
    },
    openEditModal(team) {
      this.isEditing = true;
      this.selectedTeamId = team.id;

      
      this.newTeam = {
        name: team.name,
        users: team.users.map(user => user.id || user), 
      };

      this.showModal = true;
    }

    ,
    closeModal() {
      this.showModal = false;
      this.newTeam = { name: "", users: [] };
    },
    async handleSaveTeam() {
      try {
        if (this.isEditing) {
          await apiService.updateTeam(this.selectedTeamId, this.newTeam);
        } else {
          const data = {
            name: this.newTeam.name,
            users: this.newTeam.users
          }

          console.log(data);

          await apiService.createTeam(data);
        }
        this.closeModal();
        this.fetchTeams();
      } catch (error) {
        console.error("Erro ao salvar o time:", error);
      }
    },
  },
  async created() {
    await this.fetchTeams();
    await this.fetchUsers();
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
  background-color: rgba(243, 236, 236, 0.61);
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


.add-team-button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
  margin-bottom: 16px;
}

.add-team-button:hover {
  background-color: #0056b3;
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
  width: 450px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  z-index: 1100;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.modal-header h2 {
  margin: 0;
  font-size: 1.5rem;
  color: #333;
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

.modal-body label {
  font-weight: bold;
  margin-bottom: 5px;
  display: block;
  font-size: 0.9rem;
  color: #555;
}

.modal-body input,
.modal-body select {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 1rem;
}

.select-multiple {
  height: 120px;
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



@media (max-width: 600px) {
  .modal {
    width: 90%;
  }
}
</style>
