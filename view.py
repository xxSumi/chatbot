from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'chatbot3/index.html')


import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from chatterbot import ChatBot
from django.core import serializers



class ChatterBotAppView(TemplateView):
    template_name = 'app.html'


class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = ChatBot("bot123")

    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.

        * The JSON data should contain a 'text' attribute.
        """

        input_data = json.loads(request.body.decode('utf-8'))
        print (input_data)

        response = {
            'output': [
                {
                'type' : 'text',
                'value' : '「' + input_data['text'] + '」ですね！'
                }
            ]
        }

        return JsonResponse(response, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """

        text = request.GET['text']
        print(text)
        callback = request.GET['callback']
        print(callback)


        response = {
            'output': [
                {
                'type' : 'text',
                'value' : '「' + text + '」ですね！'
                }
            ]
        }

        responseText = callback + '(' + json.dumps(response) + ')'
        print(responseText)
        return HttpResponse( responseText , content_type = "application/javascript")
