from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import get_language, activate, gettext_lazy as _, ngettext


def home_view(request):
    name = 'Ashish'
    # translate(language='bn')

    # pluralization
    count = 5
    data = ngettext(
        'there is %(count)d object',
        'there is %(count)d objects',
        count
    ) % {
        'count': count,
    }

    if request.LANGUAGE_CODE == 'ar':
        direction = 'rtl'
    else:
        direction = 'ltr'

    context = {
        'output': _("Hello %(name)s") % {'name': name},
        'data': data,
        'direction': direction
    }
    return render(request, 'django_lang/index.html', context)


def translate(language):
    current_lang = get_language()

    try:
        activate(language)
        print(_("Hello"))

    finally:
        activate(current_lang)
