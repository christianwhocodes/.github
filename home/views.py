from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse

from base.models import WaksKevin

from .forms import ContactForm
from .models import Fact, Hero, Resume, Skill


def index(request):
    skills_count = Skill.objects.all().count()

    if 3 < skills_count <= 6:
        skill_group_A = "3"
    elif skills_count <= 8:
        skill_group_A = "4"
    elif skills_count <= 10:
        skill_group_A = "5"

    skill_group_B = f"{skill_group_A}:"

    context = {
        "hero": Hero.objects.first(),
        "facts": Fact.objects.first(),
        "skills": Skill.objects.all().order_by("id"),
        "skill_group_A": skill_group_A,
        "skill_group_B": skill_group_B,
        "resume": Resume.objects.first(),
    }

    if request.method == "POST":
        filled_form = ContactForm(request.POST)
        if filled_form.is_valid():
            sender_name = filled_form.cleaned_data["name"]
            sender_email = filled_form.cleaned_data["email"]
            sender_subject = filled_form.cleaned_data["subject"]
            sender_message = filled_form.cleaned_data["message"]
            recipient_email = WaksKevin.objects.first().email

            email_context = {
                "name": sender_name,
                "email": sender_email,
                "subject": sender_subject,
                "message": sender_message,
                "url": request.build_absolute_uri(reverse("index")),
            }

            text_content = render_to_string("home/email/template.txt", email_context)
            html_content = render_to_string("home/email/template.html", email_context)

            msg = EmailMultiAlternatives(
                sender_subject,
                text_content,
                sender_email,
                [recipient_email],
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            messages.success(request, "Your message has been sent. Thank you!")
            context["contactform"] = ContactForm()
        else:
            messages.error(request, "There was an error sending the message")
            context["contactform"] = ContactForm(request.POST)
    else:
        context["contactform"] = ContactForm()

    return render(request, "home/index.html", context)
