from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """
    Renders the index page.
    """
    context = {
        'title': 'Home',
        'message': 'Welcome to our food app!'
    }
    return render(request, 'foodapp/index.html', context)

def contact(request):
    """
    Handles GET and POST requests for the contact page.
    """
    if request.method == 'POST':
        # Process form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Validate the form data
        if not name or not email or not subject or not message:
            return render(request, 'foodapp/contact.html', {
                'error': 'All fields are required.',
            })

        # Here, you can add logic to save the data, send an email, etc.
        return render(request, 'foodapp/contact.html', {
            'success': 'Thank you for contacting us! We will get back to you shortly.',
        })

    # Default GET request handling
    return render(request, 'foodapp/contact.html')

def about(request):
    """
    Renders the about page.
    """
    context = {
        'title': 'About Us',
        'description': 'Learn more about our journey and values.',
    }
    return render(request, 'foodapp/about.html', context)
