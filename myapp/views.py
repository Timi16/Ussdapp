from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from africastalking import *

@csrf_exempt
def callback(request):
    # Get the user's input
    session_id = request.POST.get('sessionId')
    service_code = request.POST.get('serviceCode')
    phone_number = request.POST.get('phoneNumber')
    text = request.POST.get('text')

    # Process the user's input
    response = ""

    if text == "":
        # Initial USSD screen
        response = "CON Welcome to The number 1 App!\n"
        response += "1. Stand a chance to Win a Smart phone click 1 to Apply\n"
        response += "2. Exit"

    elif text == "1":
        # Deduct airtime
        africastalking = AfricasTalking(username='timilehinolowu46@gmail.com', api_key='de826c4c9391c5760460e7e3430a2d5836b9b0f5c18f34fe53dd8b009fae8a40')
        airtime_amount = 10  # Adjust the amount as per your requirement
        airtime_recipient = phone_number

        try:
            # Deduct airtime using the Africa's Talking API
            africastalking.airtime.send(airtime_recipient, airtime_amount)

            # Airtime deducted successfully
            response = "END Airtime deducted successfully."
        except Exception as e:
            # Error deducting airtime
            response = "END Error deducting airtime."

    elif text == "2":
        # Exit the USSD session
        response = "END Thank you for using My USSD App."

    # Return the USSD response
    return HttpResponse(response, content_type='text/plain')
