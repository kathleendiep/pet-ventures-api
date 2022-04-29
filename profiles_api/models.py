from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Dweet(models.Model):
    user = models.ForeignKey(
        User, related_name="dweets", on_delete=models.DO_NOTHING
    )
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    petname = models.CharField(max_length=32, default="")
    category = models.CharField(max_length=32, default="")
    breed = models.CharField(max_length=32, default="")
    city = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=100, default="")
    img = models.CharField(max_length=2000, default="")
    # function to return the items
    def __str__(self):
        return (
            f"{self.user.username} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.body[:30]}..."
            f"{self.petname[:30]}..."
            f"{self.category[:30]}..."
            f"{self.breed[:30]}..."
        )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="followed_by",
        blank=True
    )
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.profile)
        user_profile.save()
        return user_profile

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return profiles

# def profile(request, pk):       
#     profile = Profile.objects.get(pk=pk)
#     if request.method == "POST":
#         current_user_profile = request.user.profile
#         data = request.POST
#         action = data.get("follow")
#         if action == "follow":
#             current_user_profile.follows.add(profile)
#         elif action == "unfollow":
#             current_user_profile.follows.remove(profile)
#         current_user_profile.save()
