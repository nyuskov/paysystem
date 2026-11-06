export default defineNuxtRouteMiddleware((to, from) => {
  const token = useCookie("auth_token");

  // Если токена нет и пользователь пытается зайти в личный кабинет — выкидываем на /login
  if (!token.value) {
    return navigateTo("/login");
  }
});
