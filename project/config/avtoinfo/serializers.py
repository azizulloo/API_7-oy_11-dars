from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        # fields = ['id','car_name']
        # exclude=['engine']
        # depth=1
        # read_only_fields=['color']



# class CarSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     car_name=serializers.CharField(max_length=50)
#     year=serializers.IntegerField()
#     price=serializers.DecimalField(max_digits=10, decimal_places=2)
#     color=serializers.CharField(max_length=50)
#     max_speed=serializers.IntegerField()
#     engine=serializers.CharField(max_length=50)    
    
#     brand_id=serializers.IntegerField()
    
    
#     def create(self, validated_data):
#         return Car.objects.create(**validated_data)
    
    
#     def update(self, instance, validated_data):
#         for key, value in validated_data.items():
#             setattr(instance, key,value)
#         instance.save()
#         return instance