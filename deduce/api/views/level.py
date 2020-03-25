from rest_framework.generics import RetrieveAPIView

from api.models import Level
from api.serializers import QuestionSerializer


class QuestionView(RetrieveAPIView):
    """Retrieve question based on current user level."""

    serializer_class = QuestionSerializer

    def get_queryset(self):
        user_level = self.request.user.level
        return Level.objects.filter(level_number=user_level)

    def get_object(self):
        """Get question object."""
        return self.get_queryset().first()
