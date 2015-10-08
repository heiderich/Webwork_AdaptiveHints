#The functions  md_table and pad_to copied and modified from csvtomd, https://github.com/mplewis/csvtomd
import sys,os
sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__))+'/../servers'))
import pandas as pd
import numpy as np
from rest_server.tornado_database import  Connection

table_descriptions={
                   u'achievement' : 'description1',
                   u'achievement_user' : 'description2', 
                   u'answers_by_part' : 'description3', 
                   u'assigned_hint' : 'description4', 
                   u'assigned_hint_feedback' : 'description5', 
                   u'assigned_hint_filter' : 'description6', 
                   u'correct_answers' : 'description7', 
                   u'global_user_achievement' : 'description8', 
                   u'hint' : 'description9', 
                   u'hint_filter' : 'description', 
                   u'key' : 'description', 
                   u'password' : 'description', 
                   u'past_answer' : 'description', 
                   u'permission' : 'description', 
                   u'problem' : 'description', 
                   u'problem_user' : 'description', 
                   u'realtime_past_answer' : 'description', 
                   u'set' : 'description', 
                   u'set_locations' : 'description', 
                   u'set_locations_user' : 'description', 
                   u'set_user' : 'description', 
                   u'setting' : 'description', 
                   u'user' : 'description', 
                   u'user_variables' : 'description'
                   }

print 'Usage:\ndescribe_tables.py mysql_username mysql_password [class_name (default=CSE103_Fall2015)]'
if len(sys.argv)==1:
    course = u'CSE103_Fall2015'
    from rest_server.webwork_config import mysql_username, mysql_password
elif len(sys.argv)==3:
    course = u'CSE103_Fall2015'
    mysql_username, mysql_password=sys.argv[1],sys.argv[2]
elif len(sys.argv)==4:
    mysql_username, mysql_password=sys.argv[1],sys.argv[2]
    course=sys.argv[3]
else:
    print 'Usage:\ndescribe_tables.py mysql_username mysql_password [class_name (default=CSE103_Fall2015)]'
print 'writing descriptions of tables of course '+course +' in databaseDescription.md file...'     

tables = []

def pad_to(unpadded, target_len):
    """
    Pad a string to the target length in characters, or return the original
    string if it's longer than the target length.
    """
    under = target_len - len(unpadded)
    if under <= 0:
        return unpadded
    return unpadded + (' ' * under)

def md_table(df,  padding=1, divider='|', header_div='-'):
    """
    Convert a 2D array of items into a Markdown table.
    padding: the number of padding spaces on either side of each divider
    divider: the vertical divider to place between columns
    header_div: the horizontal divider to place between the header row and
        body cells
    """
    if not df.shape[0]: return "This table is empty!"
    df=df.applymap(lambda x : u'{}'.format(x))
    df.insert(0,'', map(str,df.index.values))
    table= np.vstack(( df.columns.values,df.values))
    # Output data buffer
    output = ''
    # Pad short rows to the length of the longest row to fix issues with
    # rendering "jagged" CSV files
    longest_row_len = max([len(row) for row in table])
    for row in table:
        while len(row) < longest_row_len:
            row.append('')
    # Get max length of any cell for each column
    col_sizes = [max(map(len, col)) for col in zip(*table)]
    # Set up the horizontal header dividers
    header_divs = [None] * len(col_sizes)
    num_cols = len(col_sizes)
    # Pad header divs to the column size
    for cell_num in range(num_cols):
        header_divs[cell_num] = header_div * (col_sizes[cell_num] +
                                              padding * 2)
    # Trim first and last padding chars, if they exist
    if padding > 0:
        header_div_row = divider.join(header_divs)[padding:-padding]
    else:
        header_div_row = divider.join(header_divs)
    # Pad each cell to the column size
    for row in table:
        for cell_num, cell in enumerate(row):
            row[cell_num] = pad_to(cell, col_sizes[cell_num])
    # Split out the header from the body
    header = table[0]
    body = table[1:]
    # Build the inter-column dividers using the padding settings above
    multipad = ' ' * padding
    divider = multipad + divider + multipad
    output += divider.join(header) + '\n'
    output += header_div_row + '\n'
    for row in body:
        output += divider.join(row) + '\n'
    # Strip the last newline
    if output.endswith('\n'):
        output = output[:-1]
    return output




if __name__ == '__main__':
    conn = Connection('localhost','webwork',user=mysql_username,password=mysql_password)
    result=conn.query("show tables")
    table_names=[r for r in map(lambda x:x.values()[0], result) if r[:len(course)]==course]
    DB=[]
    for t in table_names:
        res= conn.query("describe {}".format(t))
	eg=conn.query("select * from {} limit 5".format(t))
        DB.append((t, pd.DataFrame([j for j in res])[['Field','Type', 'Null','Key','Default','Extra']], pd.DataFrame([j for j in eg])))
    with open('./databaseDescription.md','w') as fileout:
        for i,(t,df,eg) in enumerate(DB):
            description= [v for k,v in table_descriptions.items() if t ==(course+'_'+k) ][0]
            print >> fileout, (u'### {}. {}\n***Description***:\n\n{}\n\n***Schema***:\n```\n{}\n```\n***Example***:\n```\n{}\n```\n--------------------------------------------------'.format(i+1,t,description,md_table(df),md_table(eg))).encode("utf-8")

