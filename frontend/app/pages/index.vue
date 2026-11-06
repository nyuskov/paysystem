<script setup>
const { data: response, error, pending } = await useFetch("/api/v1/home/");

definePageMeta({
  layout: "default",
});
</script>

<template>
  <div class="saas-landing-page">
    <div>
      {{ response.message }}
    </div>
    <!-- В v4 Hero-блок собирается из базовых компонентов -->
    <UContainer class="max-w-3xl mx-auto text-center">
      <h1
        class="text-5xl font-bold tracking-tight text-neutral-900 dark:text-white sm:text-6xl"
      >
        Принимайте платежи по всему миру
      </h1>
      <p class="mt-6 text-lg leading-8 text-neutral-600 dark:text-neutral-400">
        Интеграция шлюза за 15 минут. Поддержка карт, СБП и криптовалют без
        скрытых комиссий.
      </p>
      <div class="mt-10 flex items-center justify-center gap-x-6">
        <UButton
          label="Войти в личный кабинет"
          size="xl"
          color="neutral"
          variant="solid"
          to="/customers"
        />
      </div>
    </UContainer>

    <!-- Сетка карточек преимуществ (В v4 используются обычные UCard) -->
    <UContainer class="mt-24 max-w-5xl mx-auto">
      <div class="grid grid-cols-1 gap-8 sm:grid-cols-3 text-left">
        <UCard>
          <template #header>
            <div
              class="flex items-center gap-x-3 font-semibold text-neutral-900 dark:text-white"
            >
              <UIcon
                name="i-lucide-shield-check"
                class="h-6 w-6 text-primary"
              />
              Безопасность PCI DSS
            </div>
          </template>
          <p class="text-sm text-neutral-600 dark:text-neutral-400">
            Максимальный уровень защиты данных ваших клиентов и шифрования
            транзакций.
          </p>
        </UCard>

        <UCard>
          <template #header>
            <div
              class="flex items-center gap-x-3 font-semibold text-neutral-900 dark:text-white"
            >
              <UIcon name="i-lucide-cpu" class="h-6 w-6 text-primary" />
              Умный Антифрод
            </div>
          </template>
          <p class="text-sm text-neutral-600 dark:text-neutral-400">
            Автоматическая блокировка мошеннических операций на основе ИИ.
          </p>
        </UCard>

        <UCard>
          <template #header>
            <div
              class="flex items-center gap-x-3 font-semibold text-neutral-900 dark:text-white"
            >
              <UIcon name="i-lucide-banknotes" class="h-6 w-6 text-primary" />
              Быстрый вывод
            </div>
          </template>
          <p class="text-sm text-neutral-600 dark:text-neutral-400">
            Деньги поступают на ваш расчетный счет на следующий рабочий день.
          </p>
        </UCard>
      </div>
    </UContainer>
  </div>
</template>

<style scoped>
.saas-landing-page {
  /* Растягиваем контейнер на всю высоту экрана за вычетом шапки */
  min-height: calc(100vh - 80px);

  /* Включаем Flexbox для выравнивания */
  display: flex;
  flex-direction: column;

  /* Центрируем все внутренние контейнеры по вертикали и горизонтали */
  justify-content: center;
  align-items: center;

  /* Добавляем внутренние отступы, чтобы контент не лип к краям на планшетах */
  padding-top: 3rem;
  padding-bottom: 3rem;
  padding-left: 1rem;
  padding-right: 1rem;
}
</style>
