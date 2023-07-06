<template>
    <button class="btn" :class="variantClassName">
        <slot/>
    </button>
</template>


<script setup lang="ts">

const { variant = "primary" } = defineProps < {
    variant?: "primary" | "secondary" | "light"
}>()


const variants = {
    "primary": "btn-primary",
    "secondary": "btn-secondary",
    "light": "btn-light",
}

const variantClassName = ref(variants[variant]);

</script>