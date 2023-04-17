from django.shortcuts import render

import openai, os
from django.conf import settings

# Create your views here.

def chatbot(request):
    chatbot_response = None
    if api_key is not None and request.method == 'POST':
        user_input = request.POST.get('user_input')
        response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt = user_input,
            max_tokens = 256,
            temperature = 0.5,
        )
        chatbot_response = response['choices'][0]['text']
    return render( request, 'promptai/main.html', {'response': chatbot_response})
