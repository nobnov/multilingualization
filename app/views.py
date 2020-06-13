from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language


def index(request):
    language_code = get_language()
    display_text = _('国際化')
    context = {'display_text': display_text, 'language_code': language_code}

    return render(request, 'index.html', context)
