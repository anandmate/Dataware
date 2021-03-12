from django.shortcuts import render
from django.contrib import messages
from .models import *
from itertools import chain
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    return render(request, 'application/home.html')


def rating(request):
    return render(request, 'application/rating.html')


def calc(request):
    global var_fe, var_ds
    if request.method == 'GET':
        request.session['php'] = int(request.GET.get('p'))
        request.session['html'] = int(request.GET.get('h'))
        request.session['css'] = int(request.GET.get('c'))
        request.session['wpress'] = int(request.GET.get('w'))
        request.session['bstrap'] = int(request.GET.get('b'))
        request.session['r'] = int(request.GET.get('r'))
        request.session['py'] = int(request.GET.get('py'))
        request.session['stat'] = int(request.GET.get('stat'))
        request.session['mcl'] = int(request.GET.get('ml'))
        var_fe = request.session['php'] + request.session['html'] + request.session['css'] + request.session['wpress'] + \
                 request.session['bstrap']
        var_ds = request.session['r'] + request.session['py'] + request.session['stat'] + request.session['mcl']
        php = request.session['php']*10
        html = request.session['html']*10
        css = request.session['css']*10
        wp = request.session['wpress']*10
        bs = request.session['bstrap']*10
        r = request.session['r']*10
        py = request.session['py']*10
        st = request.session['stat']*10
        ml = request.session['mcl']*10
        if var_fe < 20 and var_ds < 16:
            messages.success(request, "You need to improve your skills")
            return render(request, 'application/result.html', {'php': php, 'html': html, 'css': css, 'wp': wp, 'bs': bs,
                                                               'r': r, 'py': py, 'st': st, 'ml': ml})
        if var_fe < 20 and var_ds >= 16 and var_fe < var_ds:
            if request.session['r'] >= 4 and request.session['py'] >= 5 and request.session['stat'] >= 4 and \
                    request.session['mcl'] >= 4:
                messages.success(request, "You can be a Data Scientist")
                return render(request, 'application/result.html', {'php': php, 'html': html, 'css': css, 'wp': wp,
                                                                   'bs': bs, 'r': r, 'py': py, 'st': st, 'ml': ml})
            else:
                messages.success(request, "You need to improve your Data Science skills")
                return render(request, 'application/result.html', {'php': php, 'html': html, 'css': css, 'wp': wp,
                                                                   'bs': bs, 'r': r, 'py': py, 'st': st, 'ml': ml})
        if var_ds < 16 and var_fe >= 20 and var_ds < var_fe:
            if request.session['html'] >= 5 and request.session['css'] >= 5 and request.session['wpress'] >= 4 and \
                    request.session['bstrap'] >= 5 and request.session['php'] >= 4:
                messages.success(request, "You can be a FrontEnd Developer")
                return render(request, 'application/result.html', {'php': php, 'html': html, 'css': css, 'wp': wp,
                                                                   'bs': bs, 'r': r, 'py': py, 'st': st, 'ml': ml})
            if request.session['php'] >= 5 and request.session['html'] >= 4 and request.session['css'] >= 4 and \
                    request.session['wpress'] >= 5 and request.session['bstrap'] >= 4:
                messages.success(request, "You can be a BackEnd Developer")
                return render(request, 'application/result.html', {'php': php, 'html': html, 'css': css, 'wp': wp,
                                                                   'bs': bs, 'r': r, 'py': py, 'st': st, 'ml': ml})
            if request.session['php'] >= 5 and request.session['html'] >= 5 and request.session['css'] >= 5 and \
                    request.session['wpress'] >= 5 and request.session['bstrap'] >= 5:
                messages.success(request, "You can be a Good Web Developer")
                return render(request, 'application/result.html', {'php': php, 'html': html, 'css': css, 'wp': wp,
                                                                   'bs': bs, 'r': r, 'py': py, 'st': st, 'ml': ml})
            else:
                messages.success(request, "You need to improve your Web Development skills")
                return render(request, 'application/result.html', {'php': php, 'html': html, 'css': css, 'wp': wp,
                                                                   'bs': bs, 'r': r, 'py': py, 'st': st, 'ml': ml})
        if 16 <= var_ds < var_fe and var_fe >= 20:
            if request.session['html'] >= 5 and request.session['css'] >= 5 and request.session['wpress'] >= 4 and \
                    request.session['bstrap'] >= 5 and request.session['php'] >= 4:
                messages.success(request, "You can be a FrontEnd Developer")
                return render(request, 'application/result.html', {'php': php, 'html': html, 'css': css, 'wp': wp,
                                                                   'bs': bs, 'r': r, 'py': py, 'st': st, 'ml': ml})
            if request.session['php'] >= 5 and request.session['html'] >= 4 and request.session['css'] >= 4 and \
                    request.session['wpress'] >= 5 and request.session['bstrap'] >= 4:
                messages.success(request, "You can be a BackEnd Developer")
                return render(request, 'application/result.html', {'php': php, 'html': html, 'css': css, 'wp': wp,
                                                                   'bs': bs, 'r': r, 'py': py, 'st': st, 'ml': ml})
            if request.session['php'] >= 5 and request.session['html'] >= 5 and request.session['css'] >= 5 and \
                    request.session['wpress'] >= 5 and request.session['bstrap'] >= 5:
                messages.success(request, "You can be a Good Web Developer")
                return render(request, 'application/result.html', {'php': php, 'html': html, 'css': css, 'wp': wp,
                                                                   'bs': bs, 'r': r, 'py': py, 'st': st, 'ml': ml})
            else:
                messages.success(request, "You need to improve your Web Development skills")
                return render(request, 'application/result.html', {'php': php, 'html': html, 'css': css, 'wp': wp,
                                                                   'bs': bs, 'r': r, 'py': py, 'st': st, 'ml': ml})
        if 20 <= var_fe < var_ds and var_ds >= 16:
            messages.success(request, "You can be a Data Scientist")
            return render(request, 'application/result.html', {'php': php, 'html': html, 'css': css, 'wp': wp,
                                                               'bs': bs, 'r': r, 'py': py, 'st': st, 'ml': ml})
        if var_ds == var_fe:
            messages.success(request, "You can be a Data Scientist or Web Developer")
            return render(request, 'application/result.html', {'php': php, 'html': html, 'css': css, 'wp': wp,
                                                               'bs': bs, 'r': r, 'py': py, 'st': st, 'ml': ml})

        else:
            pass
    return render(request, 'application/result.html', {'php': php, 'html': html, 'css': css, 'wp': wp, 'bs': bs,
                                                       'r': r, 'py': py, 'st': st, 'ml': ml})


def test(request):
    question_php = Php.objects.all()
    question_html = Html.objects.all()
    question_css = Css.objects.all()
    question_wp = Wordpress.objects.all()
    question_bs = Bootstrap.objects.all()
    question_r = Rtool.objects.all()
    question_py = Python.objects.all()
    question_st = Stat.objects.all()
    question_ml = Machine.objects.all()
    questions = list(
        chain(question_php, question_html, question_css, question_wp, question_bs, question_r, question_py,
              question_st, question_ml))
    return render(request, 'application/test.html', {'questions_all': questions})


def result(request):
    question_php = Php.objects.all()
    question_html = Html.objects.all()
    question_css = Css.objects.all()
    question_wp = Wordpress.objects.all()
    question_bs = Bootstrap.objects.all()
    question_r = Rtool.objects.all()
    question_py = Python.objects.all()
    question_st = Stat.objects.all()
    question_ml = Machine.objects.all()
    total_php = score_php(request, question_php)
    total_html = score_html(request, question_html)
    total_css = score_css(request, question_css)
    total_wp = score_wp(request, question_wp)
    total_bs = score_bs(request, question_bs)
    total_r = score_r(request, question_r)
    total_py = score_py(request, question_py)
    total_st = score_st(request, question_st)
    total_ml = score_ml(request, question_ml)
    total_fe = (total_php + total_html + total_css + total_wp + total_bs)*20
    total_ds = total_r + total_py + total_ml + total_st
    php_val = total_php*20
    html_val = total_html*20
    css_val = total_css*20
    wp_val = total_wp*20
    bs_val = total_bs*20
    r_val = total_r*20
    py_val = total_py*20
    st_val = total_st*20
    ml_val = total_ml*20
    if total_ds <= 8 and total_fe <= 10:
        messages.success(request, "You need to improve your skills")
        return render(request, 'application/result.html', {'php': php_val, 'html': html_val, 'css': css_val, 'wp': wp_val,
                                                           'bs':bs_val, 'r':r_val, 'py':py_val, 'st': st_val, 'ml': ml_val})
    if total_fe <= 10 and total_ds > 8:
        messages.success(request, "You can be a Data Scientist")
        return render(request, 'application/result.html', {'php':php_val, 'html':html_val, 'css':css_val, 'wp':wp_val,
                                                           'bs':bs_val, 'r':r_val, 'py':py_val, 'st':st_val, 'ml':ml_val})
    if total_fe > 10 and total_ds <= 8:
        messages.success(request, "You can be a Web Developer")
        return render(request, 'application/result.html', {'php':php_val, 'html':html_val, 'css':css_val, 'wp':wp_val,
                                                           'bs':bs_val, 'r':r_val, 'py':py_val, 'st':st_val, 'ml':ml_val})
    if total_fe > total_ds > 8:
        messages.success(request, "You can be a Web Developer")
        return render(request, 'application/result.html', {'php':php_val, 'html':html_val, 'css':css_val, 'wp':wp_val,
                                                           'bs':bs_val, 'r':r_val, 'py':py_val, 'st':st_val, 'ml':ml_val})
    if total_ds > total_fe > 10:
        messages.success(request, "You can be a Data Scientist")
        return render(request, 'application/result.html', {'php':php_val, 'html':html_val, 'css':css_val, 'wp':wp_val,
                                                           'bs':bs_val, 'r':r_val, 'py':py_val, 'st':st_val, 'ml':ml_val})


def score_php(request, question_php):
    total_php = 0
    for i in question_php:
        answer = i.answer
        user_answer = request.POST.get(str(i.answer))
        if user_answer == answer:
            total_php += 1
    return total_php


def score_html(request, question_html):
    total_html = 0
    for i in question_html:
        answer = i.answer
        user_answer = request.POST.get(str(i.answer))
        if user_answer == answer:
            total_html += 1
    return total_html


def score_css(request, question_css):
    total_css = 0
    for i in question_css:
        answer = i.answer
        user_answer = request.POST.get(str(i.answer))
        if user_answer == answer:
            total_css += 1
    return total_css


def score_wp(request, question_wp):
    total_wp = 0
    for i in question_wp:
        answer = i.answer
        user_answer = request.POST.get(str(i.answer))
        if user_answer == answer:
            total_wp += 1
    return total_wp


def score_bs(request, question_bs):
    total_bs = 0
    for i in question_bs:
        answer = i.answer
        user_answer = request.POST.get(str(i.answer))
        if user_answer == answer:
            total_bs += 1
    return total_bs


def score_r(request, question_r):
    total_r = 0
    for i in question_r:
        answer = i.answer
        user_answer = request.POST.get(str(i.answer))
        if user_answer == answer:
            total_r += 1
    return total_r


def score_py(request, question_py):
    total_py = 0
    for i in question_py:
        answer = i.answer
        user_answer = request.POST.get(str(i.answer))
        if user_answer == answer:
            total_py += 1
    return total_py


def score_st(request, question_st):
    total_st = 0
    for i in question_st:
        answer = i.answer
        user_answer = request.POST.get(str(i.answer))
        if user_answer == answer:
            total_st += 1
    return total_st


def score_ml(request, question_ml):
    total_ml = 0
    for i in question_ml:
        answer = i.answer
        user_answer = request.POST.get(str(i.answer))
        if user_answer == answer:
            total_ml += 1
    return total_ml
