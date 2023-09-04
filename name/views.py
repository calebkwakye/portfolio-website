from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Portfolio
from django.core.mail import send_mail
from django.http import JsonResponse

def index(request):

    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    # Skills
    categories = Category.objects.all()

    # Portfolio
    portfolios = Portfolio.objects.all()
    

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios
    }


    return render(request, 'index.html', context)




def submit_form(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        user_message = request.POST.get('user_message')

        if not all([user_name, user_email, user_message]):
            return JsonResponse({'error': 'All fields are required!'})

        # Send an email with the submitted information
        subject = 'New contact form submission'
        message = f"Name: {user_name}\nEmail: {user_email}\n\nMessage:\n{user_message}"
        from_email = 'kaylebparker232@gmail.com'
        to_email = 'caleb.kwakye@richmond.edu'

        try:
            send_mail(subject, message, from_email, [to_email])
            return JsonResponse({'success': 'Your message has been sent successfully! Please go back to the homepage'})
        except Exception as e:
            print(e)
            return JsonResponse({'error': 'There was a problem sending your message. Please try again.'})

    return JsonResponse({'error': 'Invalid form submission.'})
