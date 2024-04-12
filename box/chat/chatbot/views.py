from django.shortcuts import render
from django.http import JsonResponse
from .models import Conversation
import random

def chat(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        bot_response = generate_response(user_input)
        Conversation.objects.create(user_input=user_input, bot_response=bot_response)
        return JsonResponse({'bot_response': bot_response})
    return render(request, 'chatbot/chat.html')

def generate_response(user_input):
    # Example responses
    greetings = ['Hi!', 'Hello!', 'Hey there!']
    goodbyes = ['Goodbye!', 'See you later!', 'Bye!']
    thanks = ['You\'re welcome!', 'No problem!', 'Anytime!']
    
    # Check user input and generate appropriate response
    if any(word in user_input.lower() for word in ['hello', 'hi', 'hey']):
        return random.choice(greetings)
    elif any(word in user_input.lower() for word in ['goodbye    ', 'bye']):
        return random.choice(goodbyes)
    elif 'thank' in user_input.lower():
        return random.choice(thanks)
    else:
        return "I'm sorry, I don't understand that."