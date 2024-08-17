from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random
from .categories_data import categories

def generate_prompt(request):
    context = {'categories': categories, 'prompt': ''}
    return render(request, 'prompt_generator.html', context)

def build_prompt(selected_items, character_name):
    prompt_parts = []
    subject_parts = []

    if 'Subject' in selected_items:
        for item in selected_items['Subject']:
            subcat, value = item.split(":")
            subject_parts.append(value.lower())

    if character_name:
        subject_parts.insert(0, character_name)

    if subject_parts:
        prompt_parts.append(" ".join(subject_parts))

    for category, items in selected_items.items():
        if category != 'Subject':
            for item in items:
                if ":" in item:
                    subcat, value = item.split(":")
                    prompt_parts.append(value.lower()) 
                else:
                    prompt_parts.append(item.lower()) 

    return ", ".join(prompt_parts) + "."

@csrf_exempt
def ajax_generate_prompt(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        selected_items = data.get('selected_items', {})
        character_name = data.get('character_name')
        prompt = build_prompt(selected_items, character_name)
        return JsonResponse({'prompt': prompt})
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)