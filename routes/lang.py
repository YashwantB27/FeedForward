from flask import Blueprint, session, redirect, request

lang = Blueprint('lang', __name__, url_prefix='/lang')

SUPPORTED = {'en', 'te', 'hi'}

@lang.route('/set/<lang_code>')
def set_language(lang_code):
    if lang_code in SUPPORTED:
        session['lang'] = lang_code
    next_url = request.args.get('next') or request.referrer or '/'
    return redirect(next_url)
