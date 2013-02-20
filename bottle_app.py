# bottle_app.py
# purpose: Basic webserver to help students practice writing + submitting essays
# brendan long Feb 17 2013

from bottle import default_app, route, request
import sendmail

python_anywhere_user = 'mslongsenglishii'
site_file_root = '/home/' + python_anywhere_user + '/mysite/'
teacher_gmail = 'mslongenglishii@gmail.com'

@route('/')
def home_page():
    with open( site_file_root + 'index.html', 'r') as f:
        return f.read()

@route('/literary_essay')
def literary_essary_form():
    return instantiate_page_template ( 'Literary Essay', 1750 )

@route('/expository_essay')
def expository_essay_form():
    return instantiate_page_template ( 'Expository Essay', 1750 )

@route('/persuasive_essay')
def persuasive_essay_form():
    return instantiate_page_template ( 'Persuasive Essay', 1750 )

@route('/single_selection_oer')
def single_selection_oer_form():
    return instantiate_page_template ( 'Single Selection OER', 675 )

@route('/crossover_oer')
def crossover_oer_form():
    return instantiate_page_template ( 'Crossover OER', 675 )


@route('/essay_submission', method='POST')
def submit_essay():
    lastname = request.forms.get('lastname')
    firstname    = request.forms.get('firstname')
    period = request.forms.get('period')
    essay_type = request.forms.get('essay_type')
    essay    = request.forms.get('essay')

    message = """\
    <p>Last Name: %s</p>
    <p>First Name: %s</p>
    <p>Period: %s</p>
    <p>Essay Type: %s</p>

    %s
    """ % (lastname, firstname, period, essay_type, essay)
    try:
        sendmail.sendmail ( essay_type, message, teacher_gmail )
    except Exception, e:
        return print_error_page ( essay, str(e) )
    else:
        with open( site_file_root + 'submission_success.html', 'r') as f:
            return f.read()



def instantiate_page_template ( essay_type, character_limit ):
    with open( site_file_root + 'essay_submission_template.txt', 'r') as f:
        page = f.read()
    page1 = page.replace( '____LEN____', str(character_limit) )
    page2 = page1.replace( '____PYTHON_ANYWHERE_USER____', python_anywhere_user )

    return page2.replace( '____ESSAY_TYPE____', essay_type )

def print_error_page ( essay_text, exception_message ):
    page = """\
    <HTML>
    <HEAD>
    </HEAD>
    <BODY>
    <a href="/literary_essay">Literary Essay</a>&nbsp&nbsp
    <a href="/expository_essay">Expository Essay</a>&nbsp&nbsp
    <a href="/persuasive_essay">Persuasive Essay</a>&nbsp&nbsp
    <a href="/single_selection_oer">Single Selection OER</a>&nbsp&nbsp
    <a href="/crossover_oer">Crossover OER</a>&nbsp&nbsp
    <br><br>
    <b>An error occured while submitting your essay.</b><br>
    <b>Please copy your essay below, and paste it into Microsoft Word.</b><br>
    <b>After that, call your teacher over.</b><br>
    <TEXTAREA name=essay rows=25 wrap=physical cols=70 name="essay"
    spellcheck="false">""" + essay_text + "</TEXTAREA><br>" + exception_message + "</BODY></HTML>"
    return page



application = default_app()
