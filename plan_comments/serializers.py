from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import PlanComment


class PlanCommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the PlanComment model
    Adds three extra fields when returning a list of PlanComment instances
    """

    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = PlanComment
        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_image",
            "plan",
            "created_at",
            "updated_at",
            "content",
        ]


class PlanCommentDetailSerializer(PlanCommentSerializer):
    """
    Serializer for the PlanComment model used in Detail view
    Plan is a read only field so that we dont have to set it on each update
    """

    plan = serializers.ReadOnlyField(source="plan.id")
