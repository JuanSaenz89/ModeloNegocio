from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage, send_mail
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST': 
        contact_form = ContactForm(data=request.POST) 
        if contact_form.is_valid(): 
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            email = EmailMessage(
                "New contact form submission",
                "Name: {}\nEmail: {}\n\nMessage:\n\n{}".format(name, email, content),
                "no-reply@blabla.com",
                ["maildeprueba@prueba.com"],
                reply_to=[email]
            )
            try:
                email.send(fail_silently=False)
                return redirect(reverse('contact') + '?ok')
            except:
                return redirect(reverse('contact') + '?fail')
            


    return render(request, 'contact/contact.html', {'form': contact_form}) # Pasamos el formulario a la plantilla