<template>
    <header class="w-full h-16 px-4 fixed top-0 left-0 shadow-md md:shadow-sm">
        <nav class="w-full h-full flex justify-between items-center">
            <NuxtLink to="/">
                <p class="text-rose-500"><b>B</b>loody</p>
            </NuxtLink>
            <div @click="toggleShowMenu" class="md:hidden">
                <template v-if="showMenu">
                    <Icon size="24px" name = "iconamoon:menu-burger-horizontal" /> 
                </template>
                <template v-else="showMenu">
                    <Icon size="24px" name = "ci:close-big" /> 
                </template>
            </div>
            <div class="flex items-center gap-4">
                <NuxtLink to="/">Home</NuxtLink>
                <NuxtLink to="/">About</NuxtLink>
                <NuxtLink to="/">Contact</NuxtLink>
                <NuxtLink to="/login" class="btn">Login</NuxtLink>
            </div>
        </nav>
    </header>
</template>

<script setup>
const showMenu = ref(false);
const toggleShowMenu = () => showMenu.value = !showMenu.value;

</script>