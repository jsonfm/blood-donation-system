<template>
    <section class="w-full min-h-[400px] md:min-h-[600px] flex flex-col items-center justify-center bg-primary text-white rounded-br-[50px] px-4 py-14">
        <div class="container">
            <div class="flex w-full justify-center">
                <div class="w-full md:w-1/2 md:px-12">
                    <div class="flex flex-col">
                        <h4 class="text-4xl mb-4">
                            <span>Donate</span>
                            <p>and give your best.</p>
                        </h4>
                        <p>
                            Donate Blood and join our mission to end Nigeria's severe blood shortage. With over 350.000 pints needed, your selfess act can make all the difference.
                        </p>
                    </div>
                    <div class="flex gap-2 items-center w-full mt-8">
                        <div class="w-1/2">
                             <NuxtLink to="/login" class="w-40 h-40 rounded-full border border-white flex items-center justify-center hover:bg-white hover:text-primary duration-200">
                                Donate Now
                            </NuxtLink>
                        </div>
                        <div class="w-1/2 text-center">
                            <div class="flex gap-2 items-center justify-center">
                                <p>Learn More</p>
                                <Icon name="nimbus:arrow-right"/>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="w-full md:w-1/2 hidden md:flex flex-col">
                    ...
                </div>
            </div>
        </div>
    </section>
    <section class="flex flex-col md:flex-row gap-8 md:gap-12 px-4 py-12 container">
        <div class="md:w-1/2 flex md:justify-center">
            <h4 class="text-3xl md:text-4xl">How it works</h4>
        </div>
        <div class="md:w-1/2 mt-4 flex flex-col gap-8 md:pr-32">
            <div class="flex gap-4">
                <div class="w-1/6">
                    <div class="w-12 h-12 bg-primary rounded-full"></div>
                </div>
                <div class="w-5/6 flex flex-col gap-2">
                    <h5 class="font-bold text-xl">Register</h5>
                    <p class="text-justify">
                        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Illo commodi vel labore rem magnam tempore modi alias nisi, dolores sit!
                    </p>
                </div>
            </div>
            <div class="flex gap-4">
                <div class="w-1/6">
                    <div class="w-12 h-12 bg-primary rounded-full"></div>
                </div>
                <div class="w-5/6 flex flex-col gap-2">
                    <h5 class="font-bold text-xl">Get screened</h5>
                    <p class="text-justify">
                        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Illo commodi vel labore rem magnam tempore modi alias nisi, dolores sit!
                    </p>
                </div>
            </div>
            <div class="flex gap-4">
                <div class="w-1/6">
                    <div class="w-12 h-12 bg-primary rounded-full"></div>
                </div>
                <div class="w-5/6 flex flex-col gap-2">
                    <h5 class="font-bold text-xl">Donate</h5>
                    <p class="text-justify">
                        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Illo commodi vel labore rem magnam tempore modi alias nisi, dolores sit!
                    </p>
                </div>
            </div>
        </div>
    </section>
</template>
