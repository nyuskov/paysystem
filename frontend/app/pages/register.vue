<script setup>
definePageMeta({
  layout: "default", // Чистый макет без сайдбара
});

const { login } = useAuth();
const email = ref("");
const password = ref("");
const companyName = ref("");
const loading = ref(false);
const errorMessage = ref("");

async function handleRegister() {
  loading.value = true;
  errorMessage.value = "";

  try {
    // 1. Отправляем запрос на регистрацию в FastAPI Users
    await $fetch("/api/v1/auth/register", {
      method: "POST",
      body: {
        email: email.value,
        password: password.value,
        company_name: companyName.value,
      },
    });

    // 2. После успешной регистрации сразу авторизуем пользователя
    await login(email.value, password.value);
  } catch (err) {
    console.error(err);
    errorMessage.value = "Ошибка регистрации. Возможно, этот Email уже занят.";
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
          Регистрация мерчанта
        </h3>
      </template>

      <form @submit.prevent="handleRegister" class="space-y-4">
        <div>
          <label class="block text-sm font-medium mb-1"
            >Название компании</label
          >
          <UInput
            v-model="companyName"
            type="text"
            placeholder="ООО Рога и Копыта"
            required
            w-full
          />
        </div>

        <div>
          <label class="block text-sm font-medium mb-1">Email</label>
          <UInput
            v-model="email"
            type="email"
            placeholder="ceo@company.com"
            required
            w-full
          />
        </div>

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

        <p v-if="errorMessage" class="text-sm text-red-500 text-center">
          {{ errorMessage }}
        </p>

        <UButton
          type="submit"
          label="Создать аккаунт"
          color="neutral"
          variant="solid"
          class="w-full justify-center"
          :loading="loading"
        />

        <p
          class="text-sm text-center text-neutral-600 dark:text-neutral-400 mt-4"
        >
          Уже есть аккаунт?
          <NuxtLink to="/login" class="text-primary hover:underline"
            >Войти</NuxtLink
          >
        </p>
      </form>
    </UCard>
  </div>
</template>
