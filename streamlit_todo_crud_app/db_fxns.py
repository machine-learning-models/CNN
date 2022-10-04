
import sqlite3

conn = sqlite3.connect('data.db', check_same_thread=False)
c = conn.cursor()

# Database
# Table
#Field/Columns
#DataType

def create_table():
    #table_task = 'tasktable(task TEXT, task_status TEXT, task_due_date DATE)'
    db_statement = "'CREATE TABLE IF NOT EXISTS tasktable(task TEXT, task_status TEXT, task_due_date DATE)'"
    c.execute('CREATE TABLE IF NOT EXISTS tasktable(task TEXT, task_status TEXT, task_due_date DATE)')

def add_data(task, task_status, task_due_date):
    #db_add_data = "'INSERT INTO tasktable(task, task_status, task_due_date) VALUES (?,?,?)'"
    c.execute('INSERT INTO tasktable(task, task_status, task_due_date) VALUES (?,?,?)',(task, task_status, task_due_date))
    conn.commit()

def view_all_data():
    c.execute('SELECT * FROM tasktable')
    data = c.fetchall()
    return data

def view_unique_tasks():
    c.execute('SELECT DISTINCT task FROM tasktable')
    data = c.fetchall()
    return data

def get_task(task):
    c.execute('SELECT * FROM tasktable WHERE task="{}"'.format(task))
    # Different Way To Access Data 
    #c.execute('SELECT * FROM tasktable WHERE task=?', (task))
    data = c.fetchall()
    return data

def edit_task_data( new_task, new_task_status, new_task_date, task, task_status, task_due_date):
	c.execute("UPDATE tasktable SET task =?,task_status=?,task_due_date=? WHERE task=? and task_status=? and task_due_date=? ",(new_task,new_task_status,new_task_date,task,task_status,task_due_date))
	conn.commit()
	data = c.fetchall()
	return data

def delete_data(task):
    c.execute('DELETE FROM tasktable WHERE task = "{}"'.format(task))
    conn.commit()
    
    


