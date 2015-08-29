from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django import forms
from coleyoungmark.settings import MEDIA_ROOT, BASE_DIR
from django.core.context_processors import csrf


def landingpage(request):
    t = get_template('twenty1/index.html')
    c = RequestContext(request)
    html = t.render()
    return HttpResponse(html)
