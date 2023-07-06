<template>
    <header class="w-full h-16 relative top-0 left-0 shadow-md md:shadow-sm bg-secondary">
        <nav class="w-full h-full flex justify-between items-center container">
            <NuxtLink to="/">
                <p class="text-white md:text-xl"><b>One</b>Blood</p>
            </NuxtLink>
            <div 
                class="w-full h-screen md:w-auto md:h-auto flex flex-col md:flex-row items-center gap-4 fixed md:static top-0 left-0 text-white duration-200 bg-secondary z-[999] pt-32 md:pt-0"
                :class="[showMenu ? showMenuClassName : '']"
            >
                <h4 class="text-xl mb-8 md:hidden"><b>One</b>Blood</h4>
                <div class="flex flex-col md:flex-row items-center gap-4">
                    <NuxtLink to="/">Home</NuxtLink>
                    <NuxtLink to="/">About</NuxtLink>
                    <NuxtLink to="/">Contact</NuxtLink>
                    <NuxtLink to="/login" class="btn">Login</NuxtLink>
                </div>
    
                <div class="md:hidden">
                    <Button variant="primary">
                        <NuxtLink to="/">Sign up</NuxtLink>
                    </Button>
                </div>
            </div>
            <div class="hidden md:flex">
                <Button variant="primary">
                    <NuxtLink to="/">Sign up</NuxtLink>
                </Button>
            </div>
            <div @click="toggleShowMenu" class="md:hidden text-white/60 z-[1000] cursor-pointer hover:scale-105 duration-200">
                <template v-if="showMenu">
                    <Icon size="24px" name = "nimbus:align-right" /> 
                </template>
                <template v-else>
                    <Icon size="28px" name = "ci:close-big" /> 
                </template>
            </div>

        </nav>
    </header>
</template>

<script setup lang="ts">
const showMenu = ref(true);
const toggleShowMenu = () => showMenu.value = !showMenu.value;
const showMenuClassName = ref("left-full overflow-hidden");
</script>