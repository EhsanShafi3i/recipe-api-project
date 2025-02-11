"""URL Mappings for the recipe app."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from recipe import views

router = DefaultRouter()
router.register("recipes", views.RecipeVeiwSet)

app_name = "recipe"
urlpatterns = [
    path("", include(router.urls)),
]
