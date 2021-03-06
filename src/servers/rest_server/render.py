import tornado.ioloop
import tornado.web
import tornado.gen
import pg_wrapper
import os
import tempfile
import base64
import json
from json_request_handler import JSONRequestHandler
import logging
logger = logging.getLogger(__name__)

def task_render(pg_file, seed, psvn=1234, callback=None):
    '''Async task to perform the XMLRPC request to render the problem'''
    callback(pg_wrapper.render_pg_xmlrpc(pg_file, int(seed), psvn))
 
class Render(JSONRequestHandler, tornado.web.RequestHandler):
    """Interface with Webwork/PG for rendering a PG file problem.

    Uses XMLRPC to perform the request.
    """

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        """POST /render

        Arguments:
          pg_file
            Either a path to a PG file or the content of a PG file
            encoded with Base64.
          seed
            Random seed
        Returns:
          Rendered HTML of the provided PG file.
        """
        pg_file = self.get_argument("pg_file")
        seed = self.get_argument("seed")
        psvn = self.get_argument("psvn", 1234)
        # check validity of input
        if (len(pg_file) == 0 or len(seed) == 0 or not seed.isdigit()):
            raise tornado.web.HTTPError(400)

        response = { 'render_html' : '',
                     'error_msg' : '' }
        
        # Case1: pg_file is a path
        if os.path.isabs(pg_file):
            # check if the file actually exists
            if not os.path.isfile(pg_file):
                response['error_msg'] = 'PG file not found'
                self._write_finish(response)
                return

            # call the PG wrapper
            rendered_html = yield tornado.gen.Task(task_render,
                                                   pg_file,
                                                   int(seed), psvn)
            
            if rendered_html is None:
                response['error_msg'] = 'PG service error'
                self._write_finish(response)
                return

            # all good
            response = { 'rendered_html': rendered_html }
            self._write_finish(response)

        # Case 2: pg_file is base64 encoded.
        else:
            try:
                # create a temp file and decode the pg to the file
                temp = tempfile.NamedTemporaryFile(delete=False)
                temp.write(base64.b64decode(pg_file))
                temp.close()
            except Exception:
                response['error_msg'] = 'Unable to create a temporary file'
                self._write_finish(response)
                return
                
            rendered_html = yield tornado.gen.Task(task_render,
                                                   temp.name,
                                                   int(seed), int(psvn))
            # remove the temp file
            os.remove(temp.name)

            if rendered_html is None:
                response['error_msg'] = 'PG service error'
                self._write_finish(response)
                return
        
            response = { 'rendered_html': rendered_html }
            self._write_finish(response)


    def _write_finish(self, response):
        self.write(response)
        self.finish()
