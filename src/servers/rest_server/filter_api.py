##### work with filter functions from database #####

import os.path
import tornado
import simplejson as json
import tornado.ioloop
import tornado.web
import logging
import random
import tempfile

from tornado.template import Template
from convert_timestamp import utc_to_system_timestamp
from process_query import ProcessQuery, conn
from operator import itemgetter
import pandas as pd
from datetime import datetime, timedelta
from dateutil.tz import tzlocal
import os
import re
#from webwork_parser import parse_webwork
from auth import require_auth
from parsetrees.expr_parser.Eval_parsed import parse_and_eval
from multiprocessing import Process, Pipe, Queue, current_process
from StringIO import StringIO
from parsers import parse_eval
from pg_utils import get_source, get_part_answer
from webwork_utils import get_user_vars, vars_for_student, answer_for_student
from exec_filters import filtered_answers
from filter_bank import filter_bank
from pg_wrapper import render_pg_xmlrpc
tz = tzlocal()


def serialize_datetime(obj):
    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial

logger = logging.getLogger(__name__)
BASE = '/opt/AdaptiveHintsFilters'


class FilterFunctions(ProcessQuery):
    """ /filter_functions """

    def set_default_headers(self):
        # Allows X-site requests
        super(ProcessQuery, self).set_default_headers()
        self.add_header("Access-Control-Allow-Methods", "PUT,DELETE")
        self.reload_filters()

    def reload_filters(self):
        self.filter_bank = filter_bank()
        basepath = os.path.dirname(__file__)
        filters_path = os.path.join(basepath, "filters/")
        filter_helpers_path = os.path.join(basepath, "filter_helpers/")
        self.filter_bank.import_filters_from_files(filters_path)
        self.filter_bank.import_filters_from_files(filter_helpers_path)
        self.filters_dir = filters_path


    def filter_path(self, id):
        ''' Helper method for generating file path to put filter functions. '''
        args = self.filtered_arguments('course', 'set_id', 'problem_id', 'name').values() + [id]
        logger.debug(args)
        path = os.path.join(BASE, *args)
        logger.debug(path)

    def get(self):
        ''' For loading filter functions

            Sample arguments:
            id="1",

            Returning: [
                {
                    "id": 3, ...
                },
                ...
            ]
        '''

        allowed_args = self.filtered_arguments('id', 'set_id', 'problem_id', 'name', 'author', 'course', 'function_type')
        #where = self.where_clause(**allowed_args)
        #query = '''select * from filter_functions {WHERE};'''.format(WHERE=where)
        #logger.debug(query)
        #rows = conn.query(query)
        #self.write(json.dumps(rows, default=serialize_datetime))

        # load from folder
        files = self.filter_bank.get_env_keys()
        functions = []
        for f in files:
            if f[0] == "U" or f[0] == "T" or f[0] == "C":
                functions += [{'name': f, 'code': self.filter_bank.get_code(self.filters_dir, f), 'doc': self.filter_bank.get_docstring(f)}]
        self.write(json.dumps(functions, default=serialize_datetime))

    def post(self):
        ''' For creating filter functions. '''
        course = self.get_argument('course')
        set_id = self.get_argument('set_id', 'GenericFilterFunctions')
        problem_id = self.get_argument('problem_id', 1)
        author = self.get_argument('author')
        name = self.get_argument('name')
        code = self.get_argument('code')
        function_type = name[0]

        # Create dummy hint first
        # create_hint ='''insert into {course}_hint
        #    (pg_text, author, set_id, problem_id, part_id) values
        #    ("", "{author}", "DummyHints", 1, 1)
        #'''.format(course=course, author=author)
        #hint_id = conn.execute(create_hint)
        #logger.debug(hint_id)
        now = datetime.now().isoformat()
        #create_filter_function = ''' INSERT INTO filter_functions
        #(name, course, author, set_id, problem_id, code, dummy_hint_id, created, updated, function_type)
        #values ("{name}", "{course}", "{author}", "{set_id}", {problem_id}, "{code}", "{hint_id}", "{created}", "{updated}", "{function_type}");
        #'''.format(name=name, course=course, author=author, set_id=set_id,
        #           problem_id=problem_id, code=code, hint_id=0, created=now,
        #           updated=now, function_type=function_type)
        #create_filter_function = ''' INSERT INTO filter_functions
        #(name, course, author, set_id, problem_id, dummy_hint_id, code, created, updated)
        #values ("{name}", "{course}", "{author}", "{set_id}", {problem_id}, {hint_id}, "{code}", "{created}", "{updated}");
        #'''.format(name=name, course=course, author=author, set_id=set_id,
        #           problem_id=problem_id, hint_id=hint_id, code=code, created=now,
        #           updated=now)
        #ret = conn.execute(create_filter_function) # Returns row ID

        # add filter function in filters folder
        self.filter_bank.add_filter(name,code)
        save_to = os.path.abspath(os.path.join(self.filters_dir, name))
        with open(save_to+'.py', 'w') as f:
            f.write(code)

        #self.write(json.dumps(ret))

    def put(self):
        id = self.get_argument('id')
        name = self.get_argument('name')
        logger.debug(id)
        code = self.get_argument('code')
        now = datetime.now().isoformat()
        # update in database
        #query = ''' UPDATE filter_functions SET
        #code = "{code}", updated = "{time}"
        #WHERE id={id};'''.format(code=code, time=now, id=id)
        #get_query = ''' SELECT * FROM filter_functions where '''
        #logger.debug(query)
        #ret = conn.execute(query)

        # update in filters folder
        self.filter_bank.add_filter(name,code)
        #self.write(json.dumps(ret))
        #logger.debug(self.filter_path(id))
        
    def delete(self):
        pass

# def apply_filter(answer_data, user_vars, filter_function_string, pipe):
#     import os
#     import sys
#     import StringIO
#     import tempfile
#     USER_ID=1009
#     tempdir = tempfile.mkdtemp()
#     os.chown(tempdir, USER_ID, -1)
#     os.chroot(tempdir)
#     os.setuid(USER_ID)

#     try:
#         logger.info("string")
#         logger.info(filter_function_string)
#         exec filter_function_string in globals(), locals()
#         a = answer_data
#         # This function must be defined by the exec'd code
#         ret = answer_filter(a['string'], a['parsed'], a['evaled'], a['correct_string'],
#                             a['correct_tree'], a['correct_eval'], user_vars)
#         pipe.send(ret)
#     except Exception, e:
#         logger.error("Error in filter function: %s", e)
#         print e
#     out.flush()
#     return

class ApplyFilterFunctions(ProcessQuery):
    def set_default_headers(self):
        # Allows X-site requests
        super(ProcessQuery, self).set_default_headers()
        self.add_header("Access-Control-Allow-Methods", "PUT,DELETE")
        self.reload_filters()

    def reload_filters(self):
        self.filter_bank = filter_bank()
        basepath = os.path.dirname(__file__)
        filters_path = os.path.join(basepath, "filters/")
        filter_helpers_path = os.path.join(basepath, "filter_helpers/")
        self.filter_bank.import_filters_from_files(filters_path)
        self.filter_bank.import_filters_from_files(filter_helpers_path)
        self.filters_dir = filters_path

    def post(self):
        """
        Tests one student's answer against the filters defined for the problem part.
        For any filters which match, returns the matched hint(PGML) which should be inserted into the hint.
        """
        course = self.get_argument('course')
        set_id = self.get_argument('set_id')
        problem_id = self.get_argument('problem_id')
        part_id = int(self.get_argument('part_id'))
        user_id = self.get_argument('user_id')
        answer_string = self.get_argument('answer_string')
        pg_file = self.get_source()

        # re.compile(r'\[__+\]{(?:Compute\(")?(.+?)(?:"\))?}')
        answer_re = re.compile('\[__+\]{(?:(?:Compute\(")(.+?)(?:"\))(?:.*)|(.+?))}')
        answer_boxes = answer_re.findall(pg_file)
        part_answer = answer_boxes[part_id-1][0] or answer_boxes[part_id-1][1]
        
        # Get student's variables, parse their answer, their correct answer
        user_variables = conn.query('''SELECT * from {course}_user_variables
        WHERE set_id="{set_id}" AND problem_id = {problem_id} AND user_id = "{user_id}";
        '''.format(course=course, set_id=set_id, problem_id=problem_id, user_id=user_id))

        user_variables = {row['name']: row['value'] for row in user_variables}
        # Replace variable with values
        for var in user_variables:
            if var in part_answer:
                part_answer = part_answer.replace(var, str(user_variables[var]))
        
        answer_ptree, answer_etree = parse_and_eval(part_answer, user_variables)
        ptree, etree = parse_and_eval(answer_string)
        answer_data = {'attempt': answer_string, 'att_tree': etree, 'answer': part_answer,
                        'ans_tree': answer_etree, 'variables': user_variables}
        logger.debug(answer_data)
        if etree == None:
            logger.error("att_tree is None")
            return
        if answer_etree == None:
            logger.error("ans_tree is None")
            return


        # #get conditional filter functions
        # conditional_filter_funcs = conn.query('''SELECT ff.id, ff.code, af.hint_id, af.course, af.set_id,
        # af.problem_id, af.part_id FROM filter_functions as ff
        # JOIN assigned_filters as af ON af.filter_function_id = ff.id
        # WHERE af.course='{course}' AND af.set_id='{set_id}' AND af.problem_id={problem_id} AND af.part_id={part_id} AND af.function_type='C';'''.
        #                           format(course=course, set_id=set_id, problem_id=problem_id, part_id=part_id))
        # logger.info("Conditional Filter Functions:")
        # logger.info(conditional_filter_funcs)
        # #get universal filter functions
        # universal_filter_funcs = conn.query('''SELECT ff.id, ff.code, af.hint_id, af.course, af.set_id,
        # af.problem_id, af.part_id FROM filter_functions as ff
        # JOIN assigned_filters as af ON af.filter_function_id = ff.id
        # WHERE af.course='{course}' AND af.set_id='{set_id}' AND af.problem_id={problem_id} AND af.part_id={part_id} AND af.function_type='U';'''.
        #                           format(course=course, set_id=set_id, problem_id=problem_id, part_id=part_id))
        # logger.info("Universal Filter Functions:")
        # logger.info(universal_filter_funcs)
        #logger.debug('Filters: %s', filter_funcs)

        # load from folder
        files = self.filter_bank.get_env_keys()
        con_filter_funcs = []
        uni_filter_funcs = []
        time_filter_funcs = []
        for f in files:
            ### remove the doc string from code ###
            #code = self.filter_bank.get_code(self.filters_dir, f)
            #while '\"\"\"' in code:
            #    code = code[code.index('\"\"\"')+3:]
            if f[0] == "C":
                code = self.filter_bank.get_code(self.filters_dir, f)
                con_filter_funcs += [{'name': f, 'code': code, 'doc': self.filter_bank.get_docstring(f)}]
            elif f[0] == "U":
                code = self.filter_bank.get_code(self.filters_dir, f)
                uni_filter_funcs += [{'name': f, 'code': code, 'doc': self.filter_bank.get_docstring(f)}]
            elif f[0] == "T":
                code = self.filter_bank.get_code(self.filters_dir, f)
                time_filter_funcs += [{'name': f, 'code': code, 'doc': self.filter_bank.get_docstring(f)}]

        txt = ""
        correct_set_problem_part = str(set_id) + "_" + str(problem_id) + "_" + str(part_id)
        success = False        
        for func in con_filter_funcs:
            #if func.hint_id in hints_assigned:
            #    continue
            if correct_set_problem_part in func['name']:
                success,txt,_ = self.filter_bank.exec_filter(func['name'], answer_data) #self.exec_filter_func(func['code'], answer_data, user_variables)
                #TODO: remove the length check when things become reliable
                if txt != "" and success and len(txt) < 100:
                    break
                else:
                    success = False
        if not success:
            for func in uni_filter_funcs:
                if correct_set_problem_part in func['name']:
                    success,txt,_ = self.filter_bank.exec_filter(func['name'], answer_data)#self.exec_filter_func(func['code'], answer_data, user_variables)
                    #TODO: remove the length check when things become reliable
                    if txt != "" and success and len(txt) < 100:
                        break
                    else:
                        success = False
        if not success:
            logger.info("checking timebased")
            # Only run filters if at least 3 answers and at least 3 minutes since first answer
            try:
                answer_count = conn.get('''SELECT COUNT(*) as count from {course}_answers_by_part {WHERE};'''
                                        .format(course=course, WHERE=self.where_clause('set_id', 'problem_id', 'part_id', 'user_id'))).get('count')
                first_answer = conn.get('''SELECT timestamp from {course}_answers_by_part {WHERE}
            ORDER BY timestamp ASC LIMIT 1;'''
                                        .format(course=course, WHERE=self.where_clause('set_id', 'problem_id', 'part_id', 'user_id'))).get('timestamp')
                last_answer = conn.get('''SELECT timestamp from {course}_answers_by_part {WHERE}
            ORDER BY timestamp DESC LIMIT 1;'''
                                       .format(course=course, WHERE=self.where_clause('set_id', 'problem_id', 'part_id', 'user_id'))).get('timestamp')
                diff = last_answer-first_answer
                if answer_count > 3 and diff > timedelta(minutes=3):
                    logger.info("sending")
                    for func in time_filter_funcs:
                        if correct_set_problem_part in func['name']:
                            success,txt,_ = self.filter_bank.exec_filter(func['name'], answer_data)#self.exec_filter_func(func['code'], answer_data, user_variables)
                            #TODO: remove the length check when things become reliable
                            if txt != "" and success and len(txt) < 100:
                                break
                            else:
                                success = False
            except Exception, e:
                logger.warn('Error: ' + e)
                self.write(json.dumps({}))
                return
            # Get any hints already assigned to user
            # hints_assigned = conn.query('''SELECT hint_id from {course}_assigned_hint {WHERE} AND pg_id='AnSwEr{part_id:04d}';'''
            #                            .format(course=course,
            #                                    WHERE=self.where_clause('set_id', 'problem_id', 'user_id'),
            #                                    part_id=part_id))
            # hints_assigned = set([hint['hint_id'] for hint in hints_assigned])
            
        #handle the case where none of the condition apply
        if not success:
            txt = ""
            logger.info("no match hint")
        else:
            logger.info("matched hint %s", txt)

        # Send hint with 50% chance
        send = bool(random.getrandbits(1))

        ret = {}
        ret['hint_html'] = txt
        ret['location'] = "AnSwEr"+("0000"+str(part_id))[-4:]
        ret['hintbox_id'] = 0
        ret['assigned'] = int(send)
        self.write(json.dumps(ret))

    # def exec_filter_func(self, code, answer_data, user_variables):
    #     parent, child = Pipe()
    #     p = Process(target=apply_filter, args=(answer_data, user_variables, code, child))
    #     p.start()
    #     # TODO Can we do this without blocking the process?
    #     p.join(timeout=15)
    #     if p.is_alive():
    #         logger.warn("Function took too long, we killed it.")
    #         p.terminate()
    #         #ret[func.hint_id] = None
    #         return ""
    #     else:
    #         result = parent.recv()
    #         logger.debug("Got this back: %s", result)
    #         if type(result) == str:
    #             #ret[func.hint_id] = result
    #             return result
    #         else:
    #             #ret[func.hint_id] = None
    #             return ""

class AssignedFilterFunctions(ProcessQuery):
    def get(self):
        '''
        Assigns a filter function to a given part and hint.
        '''
        query = '''SELECT * FROM assigned_filters {WHERE}'''.\
            format(self.where_clause('course', 'set_id', 'problem_id', 'part_id'))
        res = conn.query(query)

        self.write(json.dumps(res))

    def post(self):
        '''
        Assigns a filter function to a given part and hint.
        '''
        course = self.get_argument('course')
        set_id = self.get_argument('set_id')
        problem_id = self.get_argument('problem_id')
        part_id = int(self.get_argument('part_id'))
        filter_function_id = int(self.get_argument('filter_function_id'))
        hint_id = int(self.get_argument('hint_id'))

        query = '''INSERT INTO assigned_filters
        (filter_function_id, course, set_id, problem_id, part_id, hint_id, created, updated)
        VALUES ({ff_id}, '{course}', '{set_id}', {problem_id}, {part_id},
        {hint_id}, NOW(), NOW())'''.\
            format(course=course, set_id=set_id, problem_id=problem_id,
                   part_id=part_id, hint_id=hint_id, ff_id=filter_function_id)
        res = conn.execute(query)

        self.write(json.dumps(res))
