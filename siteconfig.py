# site_config.py
# purpose: stores all of the values that change between teachers' sites
# brendan long Feb 17 2013

python_anywhere_user = xxxx # e.g. 'bccbrendan'
teacher_gmail = xxxx # e.g. 'bccbrendan@gmail.com'

# should be False for pythonanywherehosting and True for localhost
standalone = False 

# these just depend on the values above
if standalone:
    site_file_root = '/home/brendan/py_dev/essay_submission_site/'
    site_url = 'http://localhost:8080'
else:
    site_file_root = '/home/' + python_anywhere_user + '/mysite/'
    site_url = 'http://' + python_anywhere_user + '.pythonanywhere.com/'


