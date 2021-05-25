from rest_framework import serializers
from jobs.models import joboffer


class jobofferSerializer(serializers.ModelSerializer):

    class Meta:
        model=joboffer
        fields='__all__'


