<template>
  <div class="container grid px-6 mx-auto">
    <h2 class="my-6 text-2xl font-semibold text-gray-700 dark:text-gray-200">
      Tables
    </h2>

    <CTA />

    <!-- With avatar -->
    <h4 class="mb-4 text-lg font-semibold text-gray-600 dark:text-gray-300">
      Table with avatars
    </h4>

    <TableAvatar />
  </div>
</template>

<script setup lang="ts">
import CTA from "@/components/CTA.vue";
import TableAvatar from "@/components/tables/TableAvatar.vue";
</script>
