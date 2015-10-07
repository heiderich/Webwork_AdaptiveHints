import sys,os
sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__))+'/../servers'))
from rest_server.webwork_config import mysql_username, mysql_password
import pandas as pd
import numpy as np
from rest_server.tornado_database import  Connection
if not len( mysql_username):
    mysql_username, mysql_password='webworkWrite','webwork'

if len(sys.argv)==1:
    course = u'CSE103'
else:
    course=sys.argv[1]
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
    df=df.astype('str')
    df.insert(0,'', map(str,df.index.values))
    table= np.vstack((['', 'Field','Type', 'Null','Key','Default','Extra'],df.values))
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
        DB.append((t, pd.DataFrame([j for j in res])[['Field','Type', 'Null','Key','Default','Extra']]))
    with open('./databaseDescription.md','w') as fileout:
        for i,(t,df) in enumerate(DB):
            print >> fileout, "### {}. {}\n***Description***:\n\n***Schema***:\n```\n{}\n```\n--------------------------------------------------".format(i+1,t,md_table(df)) 

