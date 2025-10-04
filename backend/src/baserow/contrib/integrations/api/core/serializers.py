from rest_framework import serializers

from baserow.contrib.integrations.core.models import CoreRouterServiceEdge
from baserow.core.formula.serializers import FormulaSerializerField


class CoreRouterServiceEdgeSerializer(serializers.ModelSerializer):
    condition = FormulaSerializerField(allow_blank=True)

    class Meta:
        model = CoreRouterServiceEdge
        fields = ("uid", "label", "order", "condition")
