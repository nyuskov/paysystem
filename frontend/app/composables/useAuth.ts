// frontend/composables/useAuth.ts
export const useAuth = () => {
  const token = useCookie("auth_token", { maxAge: 3600 }); // Храним токен 1 час
  const user = useState("auth_user", () => null); // Глобальное состояние пользователя

  // 1. Функция Входа (Логин)
  const login = async (email: string, password: string) => {
    try {
      // fastapi-users требует данные авторизации в формате FormData
      const formData = new FormData();
      formData.append("username", email);
      formData.append("password", password);

      const response: any = await $fetch("/api/v1/auth/jwt/login", {
        method: "POST",
        body: formData,
      });

      // Сохраняем токен в куки
      token.value = response.access_token;

      // Сразу запрашиваем профиль пользователя
      await fetchUser();

      // Перенаправляем в личный кабинет
      await navigateTo("/customers");
    } catch (error) {
      console.error("Ошибка входа:", error);
      throw error;
    }
  };

  // 2. Функция получения профиля (Проверка сессии)
  const fetchUser = async () => {
    if (!token.value) return;

    try {
      const response: any = await $fetch("/api/v1/users/me", {
        headers: {
          Authorization: `Bearer ${token.value}`,
        },
      });
      user.value = response;
    } catch (error) {
      console.error("Сессия устарела:", error);
      logout();
    }
  };

  // 3. Выход из аккаунта
  const logout = () => {
    token.value = null;
    user.value = null;
    navigateTo("/");
  };

  return {
    token,
    user,
    login,
    fetchUser,
    logout,
    isAuthenticated: computed(() => !!token.value),
  };
};
