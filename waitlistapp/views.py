import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import WaitlistSignup

@csrf_exempt
def join_waitlist(request):
    # 1. Only allow POST requests
    if request.method != 'POST':
        return JsonResponse({'error': 'POST request required'}, status=405)

    # 2. Parse the JSON data
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    # 3. Define all required fields 
    required_fields = [
        'full_name', 
        'phone_number', 
        'location', 
        'farm_size', 
        'farming_type'
    ]

    # 4. Check if any fields are missing
    for field in required_fields:
        if not data.get(field):
            return JsonResponse({'error': f'{field} is required'}, status=400)

    # 5. Process farming_type (In case they selected multiple checkboxes)
    farming_data = data.get('farming_type')
    if isinstance(farming_data, list):
        # Converts ['Poultry', 'Fish Farming'] into "Poultry, Fish Farming"
        farming_data = ", ".join(farming_data)

    # 6. Create the database record
    try:
        WaitlistSignup.objects.create(
            full_name=data['full_name'],
            phone_number=data['phone_number'],
            location=data['location'],
            farm_size=data['farm_size'],
            farming_type=farming_data, # Use the processed string here
        )
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

    # 7. Return success
    return JsonResponse({
        'success': True,
        'message': 'You have successfully joined the waitlist'
    }, status=201)
