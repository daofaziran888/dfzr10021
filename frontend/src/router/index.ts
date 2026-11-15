import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Camp = () => import('@/views/camp/index.vue')
const Season = () => import('@/views/season/index.vue')
const Teacher = () => import('@/views/teacher/index.vue')
const Course = () => import('@/views/course/index.vue')
const Material = () => import('@/views/material/index.vue')
const Student = () => import('@/views/student/index.vue')
const Accommodation = () => import('@/views/accommodation/index.vue')
const Dining = () => import('@/views/dining/index.vue')
const Outdoor = () => import('@/views/outdoor/index.vue')
const Schedule = () => import('@/views/schedule/index.vue')
const Observation = () => import('@/views/observation/index.vue')
const Safety = () => import('@/views/safety/index.vue')
const Firstaid = () => import('@/views/firstaid/index.vue')
const Transport = () => import('@/views/transport/index.vue')
const Feedback = () => import('@/views/feedback/index.vue')
const Evaluation = () => import('@/views/evaluation/index.vue')
const Photo = () => import('@/views/photo/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/camp', name: 'camp', component: Camp },
    { path: '/season', name: 'season', component: Season },
    { path: '/teacher', name: 'teacher', component: Teacher },
    { path: '/course', name: 'course', component: Course },
    { path: '/material', name: 'material', component: Material },
    { path: '/student', name: 'student', component: Student },
    { path: '/accommodation', name: 'accommodation', component: Accommodation },
    { path: '/dining', name: 'dining', component: Dining },
    { path: '/outdoor', name: 'outdoor', component: Outdoor },
    { path: '/schedule', name: 'schedule', component: Schedule },
    { path: '/observation', name: 'observation', component: Observation },
    { path: '/safety', name: 'safety', component: Safety },
    { path: '/firstaid', name: 'firstaid', component: Firstaid },
    { path: '/transport', name: 'transport', component: Transport },
    { path: '/feedback', name: 'feedback', component: Feedback },
    { path: '/evaluation', name: 'evaluation', component: Evaluation },
    { path: '/photo', name: 'photo', component: Photo },
  ],
})

export default router
