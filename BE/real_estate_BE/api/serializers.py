from rest_framework import serializers
from .models import Member, Region, RealEstatePost

class MemberSerializer(serializers.ModelSerializer):
	class Meta:
		model = Member
		fields = ['id','username','full_name', 'date_of_birth', 'email', 'real_estate_posts']

class RegionSerializer(serializers.ModelSerializer):
  real_estate_posts = serializers.SlugRelatedField(many=True, read_only=True,
        slug_field='title')
				
  class Meta:
    model = Region
    fields = ['id','region_name', 'region_description', 'real_estate_posts']

class RealEstatePostSerializer(serializers.ModelSerializer):
	class Meta:
		model = RealEstatePost
		fields ='__all__'
