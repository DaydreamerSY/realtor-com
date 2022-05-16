from django.db import models
from django.utils import timezone

# Create your models here.

class Member(models.Model):
  username = models.CharField(max_length=50, unique=True)
  password = models.CharField(max_length=50)
  full_name = models.CharField(max_length=100, blank=True, null=True)
  date_of_birth = models.DateTimeField(default=timezone.now, editable=True, blank=True)
  email = models.EmailField(max_length=50, blank=True, null=True)
  created_date = models.DateTimeField(default=timezone.now, editable=False, blank=True)
  lastUpdatedAt = models.DateTimeField(default=timezone.now, editable=False, blank=True)
  
  def __str__(self):
    return self.username


class Region(models.Model):
  region_name = models.CharField(max_length=100)
  region_description = models.CharField(max_length=255)

  def __str__(self):
    return self.region_name

DIRECTIONS = [
        ('North', 'North'),
        ('East', 'East'),
        ('South', 'South'),
        ('West', 'West')
        ]
  
# lets us explicitly set upload path and filename
def upload_to(instance, filename):
  return 'images/{filename}'.format(filename=filename)

class RealEstatePost(models.Model):
  region = models.ForeignKey(Region, related_name='real_estate_posts', on_delete=models.CASCADE, default=None)
  created_by = models.ForeignKey(Member, related_name='real_estate_posts', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  title = models.CharField(max_length=200)
  description = models.CharField(max_length=255)
  image_url = models.ImageField(upload_to=upload_to, default=None, blank=True, null=True) # URL IMAGES
  contact_phone_number = models.CharField(max_length=12)
  area_by_m2 = models.CharField(max_length=10)              # by m2
  width_of_facade = models.IntegerField()                   # by meters
  width_of_road = models.IntegerField()                     # by meters
  direction = models.CharField(max_length=15, choices=DIRECTIONS)
  is_legal = models.BooleanField(default=False)
  price = models.CharField(max_length=10)                   # by milion .000.000đ
  rank = models.IntegerField(default=1)

  def __str__(self):
    return self.title

class Comment(models.Model):
  member = models.ForeignKey(Member, related_name='comments', on_delete=models.CASCADE)
  realEstatePost = models.ForeignKey(RealEstatePost, related_name='comments', on_delete=models.CASCADE)
  comment_text = models.CharField(max_length=255)

  def __str__(self):
    return self.comment_text
