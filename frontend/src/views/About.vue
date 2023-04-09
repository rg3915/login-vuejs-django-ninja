<template>
  <div>
    <h1>About</h1>
    <p>{{ status.status }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '@/plugins/axios.js'

const status = ref([])

onMounted(async () => {
  axios.get('about/')
    .then((response) => {
      status.value = response.data
    })
})
</script>