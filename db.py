import sqlite3
import cgi

table_name = 'essays'

create_table_statement = "CREATE TABLE " + table_name + \
        "(id INTEGER PRIMARY KEY, "        + \
        "time char(100) NOT NULL, "        + \
        "lname char(100) NOT NULL, "       + \
        "fname  char(100) NOT NULL, "      + \
        "period char(100) NOT NULL, "      + \
        "essay_title char(100) NOT NULL, " + \
        "essay_body char(3000) NOT NULL, " + \
        "email_success bool NOT NULL)"

class node:
    def __init__ ( self, x, y ):
        self.x = x
        self.y = y
                        
class EssaySubmission:
    def __init__ ( self,
                   key,
                   time,
                   lname,
                   fname,
                   period,
                   essay_title,
                   essay_body,
                   email_success ):
        self.key = key
        self.time = time
        self.lname = lname
        self.fname = fname 
        self.period = period
        self.essay_title = essay_title
        self.essay_body = essay_body
        self.email_success = email_success

    def GetHTMLTableString (self, view_body_url):
        submission_get_url = view_body_url + "?id=" + str(self.key)
        body_link = "<a href=\"" + submission_get_url + "\">" + self.essay_title + "</a>"
        if self.email_success:
            emailed = 'Yes'
        else:
            emailed = 'No'
        tokens = []
        tokens.append ( "<tr>" )
        # TODO  tokens.append ( "<td>"+checkbox input]</td>
        tokens.append ( "<td>" + cgi.escape(str(self.time))  + "</td>" )
        tokens.append ( "<td>" + cgi.escape(self.lname) + "</td>" )
        tokens.append ( "<td>" + cgi.escape(self.fname) + "</td>" )
        tokens.append ( "<td>" + self.period+ "</td>" )
        tokens.append ( "<td>" + body_link  + "</td>" )
        tokens.append ( "<td>" + emailed    + "</td>")
        tokens.append ( "</tr>")
        return "\n" +''.join( tokens )

    def GetHTMLTextAreaString(self):
        tokens = []
        tokens.append ( self.lname + ", " + self.fname + "\n")
        tokens.append ( self.period + " Period\n" )
        tokens.append ( "Submitted " + str(self.time) + "\n")
        tokens.append ( self.essay_title + "\n\n")
        tokens.append ( self.essay_body )
        return ''.join( tokens )
    
    def GetEmailString(self):
        message = """\
        <p>Last Name: %s</p>
        <p>First Name: %s</p>
        <p>Period: %s</p>
        <p>Essay Type: %s</p>

        %s
        """ % (self.lname, self.fname, self.period, self.essay_title, self.essay_body)
        return message

def SubmissionFromDBRow( db_row ):
    return EssaySubmission (
            db_row[0],
            db_row[1],
            db_row[2],
            db_row[3],
            db_row[4],
            db_row[5],
            db_row[6],
            db_row[7] == 1)
 
def init_db (database_file ):
    con = sqlite3.connect(database_file)
    con.execute(create_table_statement)
    con.commit()

def add_row ( row, database_file ):
    con = sqlite3.connect( database_file )
    con.execute('INSERT INTO ' + table_name + 
                    '( time, lname, fname, period, essay_title, ' +
                    'essay_body, email_success) ' +
                    'VALUES (?, ?, ?, ?, ?, ?, ?)',
                ( str(row.time), row.lname, row.fname, row.period, 
                  row.essay_title, row.essay_body,
                  '1' if row.email_success else '0') )
    con.commit()

def get_row ( id, database_file ):
    should_be_len_1 =  get_rows ( "SELECT * FROM " + table_name + " WHERE ID = " + str(id), database_file )
    return should_be_len_1[0]

def get_all_rows ( database_file ):
    return get_rows ( "SELECT * FROM " + table_name + " ORDER BY time DESC", database_file)

def get_rows ( sql_statement, database_file ):
    con = sqlite3.connect( database_file )
    cursor = con.cursor()
    cursor.execute( sql_statement )
    results = cursor.fetchall()
    return [ SubmissionFromDBRow(row) for row in results ]

def delete_rows ( row_ids, database_file ):
    if len(row_ids) == 0:
        return
    statement = "DELETE FROM " + table_name + " WHERE " + \
    ''.join( [ "id = " + str(id) + " OR " for id in row_ids ] ) + '0' # add 1 to take care of last 'OR' 
    con = sqlite3.connect( database_file )
    con.execute( statement )
    con.commit()

def delete_all (database_file ):
    statement = "DELETE FROM " + table_name
    con = sqlite3.connect( database_file )
    con.execute( statement )
    con.commit()

    
 
