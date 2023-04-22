<template>
  <div class="flex h-screen bg-gray-50 dark:bg-gray-900">
    <Sidebar :isSideMenuOpen="isSideMenuOpen" @close-side-menu="isSideMenuOpen = false" v-show="showSidebar" />

    <div class="flex flex-col flex-1 w-full">
      <Navigation @open-side-menu="isSideMenuOpen = !isSideMenuOpen" v-show="showNavigation" />
      <div class="p-6 dark:text-white">
        <RouterView />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from "vue"
import "@/assets/main.min.css"

import { RouterView } from 'vue-router'
import Sidebar from './components/Sidebar.vue'
import Navigation from './components/Navigation.vue'

import {useRoute} from 'vue-router'
const route = useRoute()
const currentRoute = computed(() => route.path)

const showSidebar = computed(() => currentRoute.value !== '/login' && currentRoute.value !== '/register' && currentRoute.value !== '/forgot-password')
const showNavigation = computed(() => currentRoute.value !== '/login' && currentRoute.value !== '/register' && currentRoute.value !== '/forgot-password')
</script>
