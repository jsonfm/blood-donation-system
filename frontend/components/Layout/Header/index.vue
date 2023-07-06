<template>
    <header class="w-full h-16 px-4 fixed top-0 left-0 shadow-md md:shadow-sm bg-secondary">
        <nav class="w-full h-full flex justify-between items-center">
            <NuxtLink to="/">
                <p class="text-white md:text-xl"><b>One</b>Blood</p>
            </NuxtLink>
            <div @click="toggleShowMenu" class="md:hidden text-white/60 z-[1000] cursor-pointer hover:scale-105 duration-200">
                <template v-if="showMenu">
                    <Icon size="24px" name = "nimbus:align-right" /> 
                </template>
                <template v-else="showMenu">
                    <Icon size="28px" name = "ci:close-big" /> 
                </template>
            </div>
            <div 
                class="w-full h-screen md:w-auto md:h-auto flex flex-col md:flex-row items-center gap-4 fixed md:static top-0 left-0 text-white duration-200 bg-secondary z-[999] pt-32 md:pt-0"
                :class="[showMenu ? showMenuClassName : '']"
            >
                <h4 class="text-xl mb-8 md:hidden"><b>One</b>Blood</h4>
                <NuxtLink to="/">Home</NuxtLink>
                <NuxtLink to="/">About</NuxtLink>
                <NuxtLink to="/">Contact</NuxtLink>
                <NuxtLink to="/login" class="btn">Login</NuxtLink>
                <Button variant="primary">
                    <NuxtLink to="/">Sign up</NuxtLink>
                </Button>
            </div>
        </nav>
    </header>
</template>

<script setup lang="ts">
const showMenu = ref(false);
const toggleShowMenu = () => showMenu.value = !showMenu.value;
const showMenuClassName = ref("left-full");
</script>