# site_config.py
# purpose: stores all of the values that change between teachers' sites
# brendan long Feb 17 2013

python_anywhere_user = xxxx # e.g. 'mslongsenglishii'
teacher_gmail = xxxx        # e.g. 'mslongenglishii@gmail.com'

# should be False for pythonanywherehosting and True for localhost
standalone = True 

# these just depend on the values above
site_file_root = '/home/' + python_anywhere_user + '/mysite/'
site_url = 'http://' + python_anywhere_user + '.pythonanywhere.com/'


