<script setup>
// Отключаем боковое меню админки для главной страницы
definePageMeta({
  layout: "default",
});
</script>

<template>
  <div>
    <!-- Эффектный главный баннер платежки (SaaS компонент) -->
    <ULandingHero
      title="Принимайте платежи по всему миру"
      description="Интеграция шлюза за 15 минут. Поддержка карт, СБП и криптовалют без скрытых комиссий."
      :links="[
        {
          label: 'Подключить бесплатно',
          color: 'primary',
          size: 'lg',
          to: '/dashboard',
        },
      ]"
    />

    <!-- Блок преимуществ (SaaS компонент) -->
    <ULandingSection title="Почему выбирают наш процессинг?">
      <UPageGrid>
        <ULandingCard
          title="Безопасность PCI DSS"
          description="Максимальный уровень защиты данных ваших клиентов."
          icon="i-heroicons-shield-check"
        />
        <ULandingCard
          title="Умный Антифрод"
          description="Автоматическая блокировка мошеннических транзакций."
          icon="i-heroicons-cpu-chip"
        />
        <ULandingCard
          title="Быстрый вывод"
          description="Деньги поступают на ваш расчетный счет на следующий день."
          icon="i-heroicons-banknotes"
        />
      </UPageGrid>
    </ULandingSection>

    <!-- Сетка тарифов (SaaS компонент) -->
    <ULandingSection title="Прозрачные тарифы">
      <UPricingGrid>
        <UPricingCard
          title="Старт"
          price="2.5%"
          description="Для начинающего бизнеса"
          :features="['Прием карт', 'Техподдержка 24/7', 'Вывод раз в неделю']"
        />
        <UPricingCard
          title="Бизнес"
          price="1.9%"
          description="При обороте от 1 млн руб"
          :features="[
            'Все фичи Старта',
            'Персональный менеджер',
            'Ежедневный вывод',
          ]"
          highlight
        />
      </UPricingGrid>
    </ULandingSection>
  </div>
</template>
