<template>
  <div class="tasks-page">
    <h1 class="page-title">Tasks</h1>
    <div class="tasks-board">
      
      <div v-for="status in taskStatuses" :key="status" class="tasks-column">
        <div class="tasks-column-header">
          <h2>{{ statusLabels[status] }}</h2>
          <button
            v-if="status === 'PENDING'"
            class="add-task-button"
            @click="openModal"
          >
            +
          </button>
        </div>
        <div class="tasks-column-content">
          
          <div
            v-for="task in tasksByStatus[status]"
            :key="task.id"
            class="task-card"
          >
            <h3 class="task-title">{{ task.name }}</h3>
            <p class="task-description">{{ task.description }}</p>
            <div class="task-meta">
              <span>Created in: {{ new Date(task.created_at).toLocaleDateString() }}</span>
            </div>

            
            <div class="task-actions" v-if="status !== 'COMPLETED'">
              <button
                class="options-button"
                @click="toggleDropdown(task.id)"
              >
                ...
              </button>
              <div
                v-if="task.showDropdown"
                class="dropdown-menu"
              >
                <button
                  v-if="status === 'PENDING'"
                  class="dropdown-item"
                  @click="startTask(task)"
                >
                  Start
                </button>
                <button
                  v-if="status !== 'COMPLETED'"
                  class="dropdown-item"
                  @click="completeTask(task)"
                >
                  Complete
                </button>
                <button
                  v-if="status === 'IN_EXECUTION'"
                  class="dropdown-item"
                  @click="stopTask(task)"
                >
                  Stop
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    
    <div v-if="showModal" class="modal-overlay" @click.self="closeModal">
      <div class="modal">
        <div class="modal-header">
          <h2>Adicionar Tarefa</h2>
          <button class="modal-close" @click="closeModal">×</button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="handleAddTask">
            <div class="form-group">
              <label for="task-name">Title</label>
              <input
                id="task-name"
                type="text"
                v-model="newTask.name"
                placeholder="Ex.: Create new navbar"
                required
              />
            </div>
            <div class="form-group">
              <label for="task-desc">Description</label>
              <textarea
                id="task-desc"
                v-model="newTask.description"
                placeholder="Ex.: Navbar responsive"
                required
              ></textarea>
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button class="cancel-button" @click="closeModal">Cancelar</button>
          <button class="add-button" @click="handleAddTask">Adicionar</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "../services/apiService";
import { useRoute } from "vue-router";

export default {
  name: "TasksPage",
  data() {
    return {
      tasks: [],
      newTask: {
        name: "",
        description: "",
      },
      showModal: false,
      taskStatuses: ["PENDING", "IN_EXECUTION", "COMPLETED"],
      statusLabels: {
        PENDING: "To Do",
        IN_EXECUTION: "In Progress",
        COMPLETED: "Done",
      },
      tasksByStatus: {
        PENDING: [],
        IN_EXECUTION: [],
        COMPLETED: [],
      },
    };
  },
  methods: {
    async fetchTasks() {
      try {
        const projectId = this.route.params.id;
        const allTasks = await apiService.getProjectTasks(projectId);
        this.tasks = allTasks;

        
        this.tasksByStatus = {
          PENDING: allTasks.filter((task) => task.status === "PENDING"),
          IN_EXECUTION: allTasks.filter((task) => task.status === "IN_EXECUTION"),
          COMPLETED: allTasks.filter((task) => task.status === "COMPLETED"),
        };

        
        this.tasks.forEach((task) => {
          task.showDropdown = false;
        });
      } catch (error) {
        console.error("Erro ao carregar as tarefas:", error);
      }
    },
    toggleDropdown(taskId) {
      this.tasks.forEach((task) => {
        if (task.id === taskId) {
          task.showDropdown = !task.showDropdown;
        } else {
          task.showDropdown = false;
        }
      });
    },
    async startTask(task) {
      try {
        task.status = "IN_EXECUTION";
        await apiService.updateTask(task.id, task);
        this.name, this.description = ''
        this.fetchTasks();
      } catch (error) {
        console.error("Erro ao iniciar a tarefa:", error);
      }
    },
    async stopTask(task) {
      try {
        task.status = "PENDING";
        await apiService.updateTask(task.id, task);
        this.fetchTasks();
      } catch (error) {
        console.error("Erro ao parar a tarefa:", error);
      }
    },
    async completeTask(task) {
      try {
        task.status = "COMPLETED";
        await apiService.updateTask(task.id, task);
        this.fetchTasks();
      } catch (error) {
        console.error("Erro ao finalizar a tarefa:", error);
      }
    },
    openModal() {
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
    },
    async handleAddTask() {
      try {
        const projectId = this.route.params.id;
        const taskData = { ...this.newTask, status: "PENDING", project: projectId };
        await apiService.createTask(taskData);
        this.closeModal();
        this.fetchTasks();
        this.newTask.name = ""
        this.newTask.description = ""
      } catch (error) {
        console.error("Erro ao adicionar tarefa:", error);
      }
    },
  },
  async created() {
    await this.fetchTasks();
  },
  setup() {
    const route = useRoute();
    return { route };
  },
};
</script>




<style scoped>


.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6); 
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}


.modal {
  background: #fff;
  border-radius: 12px;
  padding: 30px 20px;
  width: 450px;
  box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.2); 
  position: relative;
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
  font-weight: bold;
}

.modal-close {
  background: none;
  border: none;
  font-size: 1.5rem;
  color: #888;
  cursor: pointer;
}

.modal-close:hover {
  color: #333; 
}

.modal-body .form-group {
  margin-bottom: 15px;
}

.modal-body .form-group label {
  display: block;
  margin-bottom: 5px;
  font-size: 0.9rem;
  font-weight: bold;
  color: #555;
}

.modal-body .form-group input,
.modal-body .form-group textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 0.95rem;
  transition: border-color 0.3s;
}

.modal-body .form-group input:focus,
.modal-body .form-group textarea:focus {
  border-color: #007bff; 
  outline: none;
}

.modal-body .form-group textarea {
  resize: none; 
  height: 80px;
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 20px;
}

.cancel-button {
  background: #dc3545;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  font-size: 0.9rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.cancel-button:hover {
  background: #b02a37;
}

.add-button {
  background: #007bff;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  font-size: 0.9rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.add-button:hover {
  background: #0056b3;
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
  z-index: 1100;
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



.tasks-page {
  padding: 16px;
}

.page-title {
  font-size: 2rem;
  margin-bottom: 16px;
  color: #333;
  text-align: center;
}


.tasks-board {
  display: flex;
  gap: 16px;
}


.tasks-column {
  flex: 1;
  background: #f8f9fa;
  padding: 16px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.tasks-column-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.tasks-column-header h2 {
  font-size: 1.5rem;
  color: #333;
}

.add-task-button {
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 50%;
  width: 36px;
  height: 36px;
  font-size: 1.5rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.add-task-button:hover {
  background-color: #0056b3;
}


.task-card {
  position: relative;
  background: #ffffff;
  padding: 16px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  margin-bottom: 16px;
}

.task-title {
  font-size: 1.2rem;
  color: #333;
  margin: 0 0 8px;
}

.task-description {
  font-size: 0.9rem;
  color: #555;
  margin-bottom: 8px;
}

.task-meta {
  font-size: 0.85rem;
  color: #888;
  margin-top: 8px;
}


.task-actions {
  position: absolute;
  top: 0;
  right: 10px;
}

.options-button {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  position: relative;
}

.dropdown-menu {
  position: absolute;
  top: 30px;
  right: 10px;
  background: #ffffff;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  z-index: 10;
  padding: 8px;
}

.dropdown-item {
  background: none;
  border: none;
  text-align: left;
  padding: 8px;
  width: 100%;
  cursor: pointer;
  font-size: 0.9rem;
}

.dropdown-item:hover {
  background-color: #f1f1f1;
}
</style>
