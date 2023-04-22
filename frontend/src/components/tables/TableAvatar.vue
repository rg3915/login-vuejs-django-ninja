<template>
  <div class="w-full mb-8 overflow-hidden rounded-lg shadow-xs">
    <div class="w-full overflow-x-auto">
      <table class="w-full whitespace-no-wrap">
        <thead>
          <tr class="text-xs font-semibold tracking-wide text-left text-gray-500 uppercase border-b dark:border-gray-700 bg-gray-50 dark:text-gray-400 dark:bg-gray-800">
            <th class="px-4 py-3">Client</th>
            <th class="px-4 py-3">Amount</th>
            <th class="px-4 py-3">Status</th>
            <th class="px-4 py-3">Date</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y dark:divide-gray-700 dark:bg-gray-800">
          <TableRow
            v-for="person in people"
            :key="person.name"
            :person="person"
          />
        </tbody>
      </table>
    </div>

    <div class="grid px-4 py-3 text-xs font-semibold tracking-wide text-gray-500 uppercase border-t dark:border-gray-700 bg-gray-50 sm:grid-cols-9 dark:text-gray-400 dark:bg-gray-800">
      <span class="flex items-center col-span-3">
        Showing 1-{{ people.length }} of {{ people.length }}
      </span>
      <span class="col-span-2"></span>
      <Pagination />
    </div>
  </div>
</template>

<script setup  lang='ts'>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import TableRow from '@/components/tables/TableRow.vue'
import Pagination from '@/components/Pagination.vue'

const people = ref([])

onMounted(async () => {
  axios.get('http://localhost:3000/people')
    .then((response) => {
      people.value = response.data
    })
})
</script>