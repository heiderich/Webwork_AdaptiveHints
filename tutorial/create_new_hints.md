## Analyze student answers and create customized hints ##

1. Login to webwork as teacher http://webwork.cse.ucsd.edu/teacher/

2. In webwork, click on one problem part that you would like to create hints for.

3. In the filter function section, type in a filter name (e.g.'test') and click 'Generate Filter Template'. You should see something like this:

```python
def C_WeekX_XX_X_test(params):
  """ Written by wej001 Tue Oct 13 2015 11:07:27 GMT-0700 (Pacific Sommerzeit)
  <Filter Description goes here>
  """
  # params = {'attempt': '', 'att_tree': [], 'answer': '', 'ans_tree': [], 'variables': [{'name':,'value':}]} 
  import json
  print json.dumps(params)
  return ''
```

4. Click the button 'Run Filter' and you should be able to see all the attempts that have been made in the Filter Output window below.

5. Download and store the log of attempts as a text file by clicking 'Download Filter Output'.

6. You can analyze these attempts by running ``FindMatchingSubexpressions.py`` on the saved text file.

7. Once you run the script, you will see an output of what subexpressions of the students answers match with the right answer and how many attempts there were for each matching subexpression. Based on these subexpressions you can write conditional hints.
