<template>
    <div class="w-48 h-48 shadow-md rounded-md p-4">
       <p> {{ title }} </p>
    </div>
</template>

<script setup lang="ts">
defineProps<{
    title?: string
}>()
</script>