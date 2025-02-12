"""Serilizers for recipe apis."""

from core.models import Recipe
from rest_framework import serializers


class RecipeSerializer(serializers.ModelSerializer):
    """Create a serializer for recipe."""

    class Meta:
        """Set up the meta class."""

        model = Recipe
        fields = ["id", "title", "time_minutes", "price"]
        read_only_fields = [
            "id",
        ]


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail view."""

    class Meta(RecipeSerializer.Meta):
        """Create a meta class."""

        fields = RecipeSerializer.Meta.fields + [
            "description",
        ]
