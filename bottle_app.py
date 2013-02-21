# bottle_app.py
# purpose: Basic webserver to help students practice writing + submitting essays
# brendan long Feb 17 2013

from bottle import default_app, route, request, run, view, redirect
import sendmail
import db
import siteconfig
from datetime import datetime

@route('/')
def home_page():
    with open( siteconfig.site_file_root + 'index.html', 'r') as f:
        return f.read()

@route('/literary_essay')
@view ( siteconfig.site_file_root + 'essay_submission.tpl')
def literary_essay_form ():
    return dict(essay_title='Literary Essay', char_len='1750', site_url=siteconfig.site_url)

@route('/expository_essay')
@view ( siteconfig.site_file_root + 'essay_submission.tpl')
def expository_essay_form():
    return dict(essay_title='Expository Essay', char_len='1750', site_url=siteconfig.site_url)

@route('/persuasive_essay')
@view (siteconfig.site_file_root + 'essay_submission.tpl')
def persuasive_essay_form():
    return dict(essay_title='Persuasive Essay', char_len='1750', site_url=siteconfig.site_url)

@route('/single_selection_oer')
@view (siteconfig.site_file_root + 'essay_submission.tpl')
def single_selection_oer_form():
    return dict(essay_title='Single Selection OER', char_len='675', site_url=siteconfig.site_url)

@route('/crossover_oer')
@view (siteconfig.site_file_root + 'essay_submission.tpl')
def crossover_oer_form():
    return dict(essay_title='Crossover OER', char_len='675', site_url=siteconfig.site_url)


@route('/essay_submission', method='POST')
def submit_essay():
    submit_time = datetime.now().strftime("%Y-%m-%d %I:%M%p")
    lastname = request.forms.get('lastname')
    firstname    = request.forms.get('firstname')
    period = request.forms.get('period')
    essay_type = request.forms.get('essay_type')
    essay    = request.forms.get('essay')

    submission = db.EssaySubmission( -1, submit_time, lastname, firstname, period, essay_type, essay, False)

    """
    # try to email -- disabled
    try:
        sendmail.sendmail ( submission.essay_title, submission.GetEmailString(), siteconfig.teacher_gmail )
    except Exception:
        submission.email_success = False
    else:
        submission.email_success = True
    """

    # log submission in database
    db.add_row ( submission, siteconfig.database )
 

    with open( siteconfig.site_file_root + 'submission_success.html', 'r') as f:
        return f.read()

@route('/view_submissions')
@view(siteconfig.site_file_root + 'view_submissions.tpl')
def view_submissions():
    rows = db.get_all_rows(siteconfig.database)
    html_rows = '\n'.join( [ row.GetHTMLTableString('/view_essay') for row in rows ] )
    return dict ( entries=html_rows, site_url=siteconfig.site_url )
    
@route('/view_essay')
@view(siteconfig.site_file_root + 'view_essay.tpl')
def view_essay():
    id = int(request.GET.get("id"))
    row = db.get_row ( id, siteconfig.database )
    return dict ( text = row.GetHTMLTextAreaString() )


@route('/delete_submissions', method='POST')
def delete_submissions():
    db.delete_all ( siteconfig.database )
    redirect('/view_submissions')
 
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


if siteconfig.standalone:
    run(host='localhost', port=8080, debug=True)
else:
    application = default_app()
