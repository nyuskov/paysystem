<!-- frontend/pages/login.vue -->
<script setup>
definePageMeta({
  layout: "default", // Чистый макет без сайдбара админки
});

const { login } = useAuth();

const email = ref("");
const password = ref("");
const loading = ref(false);
const errorMessage = ref("");

async function handleLogin() {
  loading.value = true;
  errorMessage.value = "";
  try {
    await login(email.value, password.value);
  } catch (err) {
    errorMessage.value = "Неверный email или пароль";
  } finally {
    loading.value = false;
  }
}
</script>

<template>
  <div
    class="min-h-screen flex items-center justify-center bg-neutral-50 dark:bg-neutral-950 px-4"
  >
    <UCard class="w-full max-w-md p-6">
      <template #header>
        <h3
          class="text-xl font-bold text-center text-neutral-900 dark:text-white"
        >
          Вход в кабинет мерчанта
        </h3>
      </template>

      <form @submit.prevent="handleLogin" class="space-y-4">
        <!-- Поле Email -->
        <div>
          <label class="block text-sm font-medium mb-1">Email</label>
          <UInput
            v-model="email"
            type="email"
            placeholder="name@company.com"
            required
            w-full
          />
        </div>

        <!-- Поле Пароль -->
        <div>
          <label class="block text-sm font-medium mb-1">Пароль</label>
          <UInput
            v-model="password"
            type="password"
            placeholder="••••••••"
            required
            w-full
          />
        </div>

        <!-- Вывод ошибки -->
        <p v-if="errorMessage" class="text-sm text-red-500 text-center">
          {{ errorMessage }}
        </p>

        <!-- Кнопка отправки -->
        <UButton
          type="submit"
          label="Войти"
          color="neutral"
          variant="solid"
          class="w-full justify-center"
          :loading="loading"
        />

        <!-- Ссылка на регистрацию (Добавляем этот блок) -->
        <p
          class="text-sm text-center text-neutral-600 dark:text-neutral-400 mt-4"
        >
          Ещё не зарегистрированы?
          <NuxtLink
            to="/register"
            class="text-neutral-900 dark:text-white font-medium hover:underline ml-1"
          >
            Создать аккаунт
          </NuxtLink>
        </p>
      </form>
    </UCard>
  </div>
</template>
