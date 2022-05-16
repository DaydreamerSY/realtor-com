from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RealEstatePostSerializer, RegionSerializer, MemberSerializer

from .models import RealEstatePost, Region, Member
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/re-post-list/',
		'Detail View':'/re-post-detail/<str:pk>/',
		'Create':'/re-post-create/',
		'Update':'/re-post-update/<str:pk>/',
		'Delete':'/re-post-delete/<str:pk>/',
		}

	return Response(api_urls)

# Member
@api_view(['GET'])
def memberList(request):
	members = Member.objects.all().order_by('-id')
	serializer = MemberSerializer(members, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def memberCreate(request):
	serializer = MemberSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	else:
		return response(data = serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def memberDelete(request, pk):
	member = Member.objects.get(id=pk)

	if member.delete():
		return Response('Member with id:' + pk + ' succsesfully delete!')
	else:
		return Response(data = serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Region
@api_view(['GET'])
def regionList(request):
	regions = Region.objects.all().order_by('-id')
	serializer = RegionSerializer(regions, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def regionCreate(request):
	serializer = RegionSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	
	return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Real Estate
@api_view(['GET'])
def realEstatePostList(request):
	realEstatePosts = RealEstatePost.objects.all().order_by('-id')
	serializer = RealEstatePostSerializer(realEstatePosts, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def realEstatePostDetail(request, pk):
	realEstatePosts = RealEstatePost.objects.get(id=pk)
	serializer = RealEstatePostSerializer(realEstatePosts, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def realEstatePostCreate(request):
	serializer = RealEstatePostSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()
		return response(serializer.data)
	else:
		return response(data = serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def realEstatePostUpdate(request, pk):
	realestatePost = RealEstatePost.objects.get(id=pk)
	serializer = RealEstatePostSerializer(instance=realestatePost, data=request.data)

	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)

	return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def realEstatePostDelete(request, pk):
	realEstatePost = realEstatePost.objects.get(id=pk)
	realEstatePost.delete()

	return Response('Real estate post succsesfully delete!')

# For report real estate post
@api_view(['PATCH'])
def realEstatePostReport(request, pk):
	realEstatePost = RealEstatePost.objects.get(id=pk)
	realEstatePost.rank = realEstatePost.rank - 1
	realEstatePost.save()

	return Response('Real estate post successfully report')

