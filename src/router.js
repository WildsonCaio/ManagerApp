import { createRouter, createWebHistory } from "vue-router";
import ProjectsPage from "./pages/ProjectsPage.vue";
import DetailProjectPage from "./pages/DetailProjectPage.vue";
import HomePage from "./pages/HomePage.vue";
import TasksPage from "./pages/TasksPage.vue";
import TeamsPage from "./pages/TeamsPage.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: HomePage,
  },
  {
    path: "/projects",
    name: "Projects",
    component: ProjectsPage,
  },
  {
    path: "/project/:id",
    name: "ProjectTasks",
    component: DetailProjectPage,
    props: true, 
  },
  {
    path: "/tasks",
    name: "Tasks",
    component: TasksPage,
    props: true, 
  },

  {
    path: "/teams",
    name: "Teams",
    component: TeamsPage,
    props: true, 
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
