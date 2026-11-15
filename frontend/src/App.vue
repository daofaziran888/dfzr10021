<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">生态研学营地运营综合管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向自然生态研学营地的营期策划、师资调配、物资筹备、学员接待、户外活动执行与安全应急的一体化管理后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "营地档案", path: "/camp" }, { label: "营期策划", path: "/season" }, { label: "师资调配", path: "/teacher" }, { label: "课程设计", path: "/course" }, { label: "物资筹备", path: "/material" }, { label: "学员接待", path: "/student" }, { label: "住宿安排", path: "/accommodation" }, { label: "餐饮管理", path: "/dining" }, { label: "户外活动", path: "/outdoor" }, { label: "日程执行", path: "/schedule" }, { label: "自然观察", path: "/observation" }, { label: "安全应急", path: "/safety" }, { label: "医疗救护", path: "/firstaid" }, { label: "交通调度", path: "/transport" }, { label: "家长反馈", path: "/feedback" }, { label: "营期评价", path: "/evaluation" }, { label: "影像记录", path: "/photo" }]
</script>
