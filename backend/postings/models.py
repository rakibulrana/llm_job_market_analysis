from django.db import models


class Posting(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Skill(models.Model):
    name = models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=200, null=True, blank=True)


class PostingSkill(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    confidence = models.FloatField(default=0.0)
