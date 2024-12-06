import axios from "axios";

const API_URL = "http://localhost:8000/api/v1";

export const apiService = {
  
  async getClients() {
    try {
      const response = await axios.get(`${API_URL}/clients/`);
      return response.data.results;
    } catch (error) {
      console.error("Erro ao buscar os clientes:", error);
      throw error;
    }
  },

  
  async getUsers(params='') {
    try {
      const response = await axios.get(`${API_URL}/users/${params}`);
      return response.data.results;
    } catch (error) {
      console.error("Erro ao buscar os projetos:", error);
      throw error;
    }
  },

  
  async getProjects(params='') {
    try {
      const response = await axios.get(`${API_URL}/projects/${params}`);
      return response.data.results;
    } catch (error) {
      console.error("Erro ao buscar os projetos:", error);
      throw error;
    }
  },
  
  async getTeams() {
    try {
      const response = await axios.get(`${API_URL}/teams/?limit=999`);
      return response.data.results;
    } catch (error) {
      console.error("Erro ao buscar os projetos:", error);
      throw error;
    }
  },

  
  async getTasks(params = '') {
    try {
      const response = await axios.get(`${API_URL}/tasks/${params}`);
      return response.data.results;
    } catch (error) {
      console.error("Erro ao buscar as tarefas:", error);
      throw error;
    }
  },

  
  async getProjectTasks(id) {
    try {
      const response = await axios.get(`${API_URL}/projects/${id}/tasks/`);
      return response.data.results;
    } catch (error) {
      console.error("Erro ao buscar as tarefas:", error);
      throw error;
    }
  },

  
  async createClient(clientData) {
    try {
      const response = await axios.post(`${API_URL}/clients/`, clientData);
      return response.data.results;
    } catch (error) {
      console.error("Erro ao criar cliente:", error);
      throw error;
    }
  },

  
  async createProject(projectData) {
    try {
      const response = await axios.post(`${API_URL}/projects/`, projectData);
      return response.data.results;
    } catch (error) {
      console.error("Erro ao criar projeto:", error);
      throw error;
    }
  },

  async createTeam(teamData) {
    try {
      const response = await axios.post(`${API_URL}/teams/`, teamData);
      return response.data.results;
    } catch (error) {
      console.error("Erro ao criar usuário:", error);
      throw error;
    }
  },

  
  async createTask(taskData) {
    try {
      const response = await axios.post(`${API_URL}/tasks/`, taskData);
      return response.data.results;
    } catch (error) {
      console.error("Erro ao criar tarefa:", error);
      throw error;
    }
  },

  
  async updateClient(clientId, clientData) {
    try {
      const response = await axios.put(`${API_URL}/clients/${clientId}/`, clientData);
      return response.data.results;
    } catch (error) {
      console.error("Erro ao atualizar cliente:", error);
      throw error;
    }
  },

  
  async updateProject(projectId, projectData) {
    try {
      const response = await axios.put(`${API_URL}/projects/${projectId}/`, projectData);
      return response.data.results;
    } catch (error) {
      console.error("Erro ao atualizar projeto:", error);
      throw error;
    }
  },

  async updateTeam(teamId, teamData) {
    try {
      const response = await axios.put(`${API_URL}/teams/${teamId}/`, teamData);
      return response.data;
    } catch (error) {
      console.error("Erro ao atualizar o time:", error);
      throw error;
    }
  }
,   

  

  
  async updateTask(taskId, taskData) {
    try {
      const response = await axios.put(`${API_URL}/tasks/${taskId}/`, taskData);
      return response.data.results;
    } catch (error) {
      console.error("Erro ao atualizar tarefa:", error);
      throw error;
    }
  },

  
  async deleteClient(clientId) {
    try {
      const response = await axios.delete(`${API_URL}/clients/${clientId}/`);
      return response.data.results;
    } catch (error) {
      console.error("Erro ao deletar cliente:", error);
      throw error;
    }
  },

  
  async deleteProject(projectId) {
    try {
      const response = await axios.delete(`${API_URL}/projects/${projectId}/`);
      return response.data.results;
    } catch (error) {
      console.error("Erro ao deletar projeto:", error);
      throw error;
    }
  },

  
  async deleteTask(taskId) {
    try {
      const response = await axios.delete(`${API_URL}/tasks/${taskId}/`);
      return response.data.results;
    } catch (error) {
      console.error("Erro ao deletar tarefa:", error);
      throw error;
    }
  },
};
