from django.db import models

class WaitlistSignup(models.Model):
    # Your existing fields
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    farm_size = models.CharField(max_length=100)

    # NEW FIELD
    FARMING_CHOICES = [
        ('crop', 'Crop Farming'),
        ('livestock', 'Livestock Farming'),
        ('mixed', 'Mixed Farming'),
        ('other', 'Other'),
    ]
    farming_type = models.CharField(
        max_length=50, 
        choices=FARMING_CHOICES, 
        default='crop'
    )
