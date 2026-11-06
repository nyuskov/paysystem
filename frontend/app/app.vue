<script setup>
const { fetchUser, token } = useAuth();

// Если в куках есть токен, восстанавливаем профиль пользователя до рендеринга страниц
if (token.value) {
  await fetchUser();
}
</script>

<template>
  <div>
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>
