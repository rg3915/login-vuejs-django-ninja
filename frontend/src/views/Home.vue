<template>
  <div>
    <h1>Home</h1>
    <table>
      <tbody>
        <template v-for="todo in todos" :key="todo.id">
          <tr>
            <td>{{ todo.id }}</td>
            <td>{{ todo.task }}</td>
          </tr>
        </template>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '../plugins/axios'

const todos = ref([])

onMounted(async () => {
  this.$axios.get('about/')
    .then((response) => {
      todos.value = response.data
    })
})
</script>