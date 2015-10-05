##### work with filter functions from database #####

import os.path
import tornado
import simplejson as json
import tornado.ioloop
import tornado.web
import logging

from tornado.template import Template
from convert_timestamp import utc_to_system_timestamp
from process_query import ProcessQuery, conn
from operator import itemgetter
import pandas as pd
from datetime import datetime, timedelta
from dateutil.tz import tzlocal
import os
import re
from webwork_parser import parse_webwork
from auth import require_auth
from Eval_parsed import eval_parsed, Collect_numbers, numbers_and_exps, parse_and_eval
from multiprocessing import Process, Pipe, Queue, current_process
from StringIO import StringIO
from parsers import parse_eval
from pg_utils import get_source, get_part_answer
from webwork_utils import get_user_vars, vars_for_student, answer_for_student
from exec_filters import filtered_answers
from filter_bank import filter_bank
tz = tzlocal()


def serialize_datetime(obj):
    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial

logger = logging.getLogger(__name__)
BASE = '/opt/AdaptiveHintsFilters'


class FilterFunctions(ProcessQuery):
    """ /filter_functions """

    # def __init__(self):
    #     self.a_filter_bank = filter_bank()
    #     self.a_filter_bank.import_filters_from_files('filter_helpers/')
    #     self.a_filter_bank.import_filters_from_files('filters/')

    def set_default_headers(self):
        # Allows X-site requests
        super(ProcessQuery, self).set_default_headers()
        self.add_header("Access-Control-Allow-Methods", "PUT,DELETE")

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
        a_filter_bank = filter_bank()
        basepath = os.path.dirname(__file__)
        logger.info(basepath)
        filters_path = os.path.join(basepath, "../filters/")
        a_filter_bank.import_filters_from_files(filters_path)
        files = a_filter_bank.get_env_keys()
        functions = []
        for f in files:
            if f[0] != "_":
                functions += [{'name': f, 'code': a_filter_bank.get_code(filters_path, f), 'doc': a_filter_bank.get_docstring(f)}]
        self.write(json.dumps(functions, default=serialize_datetime))

    def post(self):
        ''' For creating filter functions. '''
        course = self.get_argument('course')
        set_id = self.get_argument('set_id', 'GenericFilterFunctions')
        problem_id = self.get_argument('problem_id', 1)
        author = self.get_argument('author')
        name = self.get_argument('name')
        code = self.get_argument('code')
        function_type = self.get_argument('function_type')


        # Create dummy hint first
        #create_hint ='''insert into {course}_hint
        #    (pg_text, author, set_id, problem_id, part_id) values
        #    ("", "{author}", "DummyHints", 1, 1)
        #'''.format(course=course, author=author)
        #hint_id = conn.execute(create_hint)
        #logger.debug(hint_id)
        now = datetime.now().isoformat()
        #create_filter_function = ''' INSERT INTO filter_functions
        #(name, course, author, set_id, problem_id, code, created, updated, function_type)
        #values ("{name}", "{course}", "{author}", "{set_id}", {problem_id}, "{code}", "{created}", "{updated}", "{function_type}");
        #'''.format(name=name, course=course, author=author, set_id=set_id,
        #           problem_id=problem_id, code=code, created=now,
        #           updated=now, function_type=function_type)
        #create_filter_function = ''' INSERT INTO filter_functions
        #(name, course, author, set_id, problem_id, dummy_hint_id, code, created, updated)
        #values ("{name}", "{course}", "{author}", "{set_id}", {problem_id}, {hint_id}, "{code}", "{created}", "{updated}");
        #'''.format(name=name, course=course, author=author, set_id=set_id,
        #           problem_id=problem_id, hint_id=hint_id, code=code, created=now,
        #           updated=now)
        #ret = conn.execute(create_filter_function) # Returns row ID

        # add filter function in filters folder
        a_filter_bank = filter_bank()
        basepath = os.path.dirname(__file__)
        filters_path = os.path.join(basepath, "../filters")
        filter_helpers_path = os.path.join(basepath, "../filter_helpers")
        a_filter_bank.import_filters_from_files(filter_helpers_path)
        a_filter_bank.import_filters_from_files(filters_path)
        a_filter_bank.add_filter(name,code)
        save_to = os.path.abspath(os.path.join(basepath, "..", "filters", name))
        with open(save_to+'.py', 'w') as f:
            f.write(code)

        self.write(json.dumps(ret))

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
        a_filter_bank = filter_bank()
        basepath = os.path.dirname(__file__)
        filters_path = os.path.join(basepath, "../filters")
        filter_helpers_path = os.path.join(basepath, "../filter_helpers")
        a_filter_bank.import_filters_from_files(filter_helpers_path)
        a_filter_bank.import_filters_from_files(filters_path)
        a_filter_bank.add_filter(name,code)
        #self.write(json.dumps(ret))
        #logger.debug(self.filter_path(id))
        
    def delete(self):
        pass

def apply_filter(answer_data, user_vars, filter_function_string, pipe):
    import os
    import sys
    import StringIO
    import tempfile
    USER_ID=1009

    tempdir = tempfile.mkdtemp()
    os.chown(tempdir, USER_ID, -1)
    os.chroot(tempdir)
    os.setuid(USER_ID)

    try:
        exec filter_function_string in globals(), locals()
        a = answer_data
        # This function must be defined by the exec'd code
        ret = answer_filter(a['string'], a['parsed'], a['evaled'], a['correct_string'],
                            a['correct_tree'], a['correct_eval'], user_vars)
        pipe.send(ret)
    except Exception, e:
        logger.error("Error in filter function: %s", e)
        print e
    out.flush()
    return

class ApplyFilterFunctions(ProcessQuery):
    def set_default_headers(self):
        # Allows X-site requests
        super(ProcessQuery, self).set_default_headers()
        self.add_header("Access-Control-Allow-Methods", "PUT,DELETE")

    def post(self):
        '''
        Tests one student's answer against the filters defined for the problem part.

        For any filters which match, returns the hint_id of the matched hint and
        optionally, any PGML which should be inserted into the hint.
        '''
        course = self.get_argument('course')
        set_id = self.get_argument('set_id')
        problem_id = self.get_argument('problem_id')
        part_id = int(self.get_argument('part_id'))
        user_id = self.get_argument('part_id')
        answer_string = self.get_argument('answer_string')
        function_type = self.get_argument('function_type')
        pg_file = self.get_source()
        # Only run filters if at least 3 answers and at least 10 minutes since first answer
        # try:
        #     answer_count = conn.get('''SELECT COUNT(*) as count from {course}_answers_by_part {WHERE};'''
        #                             .format(course=course, WHERE=self.where_clause('set_id', 'problem_id', 'part_id', 'user_id'))).get('count')
        #     first_answer = conn.get('''SELECT timestamp from {course}_answers_by_part {WHERE}
        # ORDER BY timestamp ASC LIMIT 1;'''
        #                             .format(course=course, WHERE=self.where_clause('set_id', 'problem_id', 'part_id', 'user_id'))).get('timestamp')
        #     last_answer = conn.get('''SELECT timestamp from {course}_answers_by_part {WHERE}
        # ORDER BY timestamp DESC LIMIT 1;'''
        #                            .format(course=course, WHERE=self.where_clause('set_id', 'problem_id', 'part_id', 'user_id'))).get('timestamp')
        #     diff = last_answer-first_answer
        #     if answer_count < 3 or diff < timedelta(minutes=10):
        #         self.write(json.dumps({}))
        #         return
        # except:
        #     logger.warn('Error')
        #     self.write(json.dumps({}))
        #     return
        # Get any hints already assigned to user
        hints_assigned = conn.query('''SELECT hint_id from {course}_assigned_hint {WHERE} AND pg_id='AnSwEr{part_id:04d}';'''
                                    .format(course=course,
                                            WHERE=self.where_clause('set_id', 'problem_id', 'user_id'),
                                            part_id=part_id))
        hints_assigned = set([hint['hint_id'] for hint in hints_assigned])
        # Get student's variables, parse their answer, their correct answer
        user_variables = conn.query('''SELECT * from {course}_user_variables
        WHERE set_id="{set_id}" AND problem_id = {problem_id} AND user_id = "{user_id}";
        '''.format(course=course, set_id=set_id, problem_id=problem_id, user_id=user_id))

        user_variables = {row['name']: row['value'] for row in user_variables}
        # re.compile(r'\[__+\]{(?:Compute\(")?(.+?)(?:"\))?}')
        answer_re = re.compile('\[__+\]{(?:(?:Compute\(")(.+?)(?:"\))(?:.*)|(.+?))}')
        answer_boxes = answer_re.findall(pg_file)
        part_answer = answer_boxes[part_id-1][0] or answer_boxes[part_id-1][1]
        answer_ptree, answer_etree = parse_and_eval(part_answer, user_variables)
        ptree, etree = parse_and_eval(answer_string)
        answer_data = {'string': answer_string, 'parsed': ptree, 'evaled': etree,
                       'correct_string': part_answer, 'correct_tree': answer_ptree,
                       'correct_eval': answer_etree}
        #get conditional filter functions
        conditional_filter_funcs = conn.query('''SELECT ff.id, ff.code, af.hint_id, af.course, af.set_id,
        af.problem_id, af.part_id FROM filter_functions as ff
        JOIN assigned_filters as af ON af.filter_function_id = ff.id
        WHERE af.course='{course}' AND af.set_id='{set_id}' AND af.problem_id={problem_id} AND af.part_id={part_id};'''.
                                  format(course=course, set_id=set_id, problem_id=problem_id, part_id=part_id))
        #get universal filter functions
        universal_filter_funcs = conn.query('''SELECT ff.id, ff.code, af.hint_id, af.course, af.set_id,
        af.problem_id, af.part_id FROM filter_functions as ff
        JOIN assigned_filters as af ON af.filter_function_id = ff.id
        WHERE af.course='{course}' AND af.set_id='{set_id}' AND af.problem_id={problem_id} AND af.part_id={part_id};'''.
                                  format(course=course, set_id=set_id, problem_id=problem_id, part_id=part_id))
        #logger.debug('Filters: %s', filter_funcs)

        ret = {}
        for func in conditional_filter_funcs:
            if func.hint_id in hints_assigned:
                continue
            code = func['code']
            parent, child = Pipe()
            p = Process(target=apply_filter, args=(answer_data, user_variables, code, child))
            p.start()
            # TODO Can we do this without blocking the process?
            p.join(timeout=15)
            if p.is_alive():
                logger.warn("Function took too long, we killed it.")
                p.terminate()
                ret[func.hint_id] = None
            else:
                result = parent.recv()
                logger.debug("Got this back: %s", result)
                if type(result) == str:
                    ret[func.hint_id] = result
                else:
                    ret[func.hint_id] = None

        self.write(json.dumps(ret))

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
