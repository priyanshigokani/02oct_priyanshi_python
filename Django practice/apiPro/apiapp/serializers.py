from rest_framework import serializers
from .models import *

class inf(serializers.ModelSerializer):
    class Meta:
        model=info
        fields = "__all__"
        