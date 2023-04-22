<template>
  <main>
    <CTA />

    <div class="grid gap-6 mb-8 md:grid-cols-2 xl:grid-cols-4">
      <!-- Card -->
      <Card>
        <div class="flex items-center">
          <div class="p-4 mr-4 text-orange-500 bg-orange-100 rounded-lg dark:text-orange-100 dark:bg-orange-500">
            <UserGroupIcon class="w-6" />
          </div>
          <div>
            <p class="mb-2 text-sm font-medium text-gray-600 dark:text-gray-400">
              Total clients
            </p>
            <p class="text-lg font-semibold text-gray-700 dark:text-gray-200">
              6389
            </p>
          </div>
        </div>
      </Card>

      <Card>
        <div class="flex items-center">
          <div class="p-4 mr-4 text-green-500 bg-green-100 rounded-lg dark:text-green-100 dark:bg-green-500">
            <CashIcon class="w-6" />
          </div>
          <div>
            <p class="mb-2 text-sm font-medium text-gray-600 dark:text-gray-400">
              Account Balance
            </p>
            <p class="text-lg font-semibold text-gray-700 dark:text-gray-200">
              $46,760.89
            </p>
          </div>
        </div>
      </Card>

      <!-- Card -->
      <Card>
        <div class="flex items-center">
          <div class="p-4 mr-4 text-blue-500 bg-blue-100 rounded-lg dark:text-blue-100 dark:bg-blue-500">
            <ShoppingCartIcon class="w-6" />
          </div>
          <div>
            <p class="mb-2 text-sm font-medium text-gray-600 dark:text-gray-400">
              New sales
            </p>
            <p class="text-lg font-semibold text-gray-700 dark:text-gray-200">
              376
            </p>
          </div>
        </div>
      </Card>
      <!-- Card -->
      <Card>
        <div class="flex items-center">
          <div class="p-4 mr-4 text-teal-500 bg-teal-100 rounded-lg dark:text-teal-100 dark:bg-teal-500">
            <ChatIcon class="w-6" />
          </div>
          <div>
            <p class="mb-2 text-sm font-medium text-gray-600 dark:text-gray-400">
              Pending contacts
            </p>
            <p class="text-lg font-semibold text-gray-700 dark:text-gray-200">
              35
            </p>
          </div>
        </div>
      </Card>
    </div>

    <TableAvatar />

  </main>
</template>

<script setup lang="ts">
import CTA from '@/components/CTA.vue';
import Card from "@/components/Card.vue";
import TableAvatar from "@/components/tables/TableAvatar.vue";
import { UserGroupIcon, CashIcon, ShoppingCartIcon, ChatIcon } from '@heroicons/vue/outline';
</script>
