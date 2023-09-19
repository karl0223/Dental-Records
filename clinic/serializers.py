from rest_framework import serializers

class PackageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    package_type = serializers.CharField(max_length=1)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)