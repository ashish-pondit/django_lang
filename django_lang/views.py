from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import get_language, activate, gettext_lazy as _


def home_view(request):
    name = 'Ashish'
    translate(language='bn')
    context = {
        'output': _("Hello %(name)s") % {'name': name}
    }
    return render(request, 'django_lang/index.html', context)


def translate(language):
    current_lang = get_language()

    try:
        activate(language)
        print(_("Hello"))

    finally:
        activate(current_lang)



