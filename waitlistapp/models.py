from django.db import models

class WaitlistSignup(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    farm_size = models.CharField(max_length=100)

    
    FARMING_CHOICES = [
        ('crop_farming', 'Crop Farming'),
        ('poultry', 'Poultry'),
        ('livestock', 'Livestock'),
        ('fish_farming', 'Fish Farming'),
        ('mixed', 'Mixed Farming'),
    ]
    
    farming_type = models.CharField(
        max_length=100,
        choices=FARMING_CHOICES, 
        default='crop_farming'
    )

  
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.full_name} - {self.farming_type}"
