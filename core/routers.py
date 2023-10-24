from rest_framework_nested import routers

from core.user.viewsets import UserViewSet
from core.auth.viewsets import (
    RegisterViewSet,
    LoginViewSet,
    RefreshViewSet,
    LogoutViewSet,
)
from core.product.viewsets import ProductViewSet

router = routers.SimpleRouter()

# ##################################################################### #
# ################### AUTH                       ###################### #
# ##################################################################### #
router.register(r"auth/register", RegisterViewSet, basename="auth-register")
router.register(r"auth/login", LoginViewSet, basename="auth-login")
router.register(r"auth/refresh", RefreshViewSet, basename="auth-refresh")
router.register(r"auth/logout", LogoutViewSet, basename="auth-logout")


# ##################################################################### #
# ################### USER                       ###################### #
# ##################################################################### #
router.register(r"user", UserViewSet, basename="user")


# ##################################################################### #
# ################### PRODUCT                    ###################### #
# ##################################################################### #
router.register(r"product", ProductViewSet, basename="product")


urlpatterns = [*router.urls]
