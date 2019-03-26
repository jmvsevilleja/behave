# -- FILE: behave4my_project/fixtures.py
# ALTERNATIVE: Place fixture in "features/environment.py" (but reuse is harder)
from behave import fixture
# import threading
# from wsgiref import simple_server
# from my_application import model
# from my_application import web_app


@fixture
def wsgi_server(context, port=8000):
    context.server = 'simple server'  # simple_server.WSGIServer(('', port))
    # context.server.set_app(web_app.main(environment='test'))
    # context.thread = threading.Thread(target=context.server.serve_forever)
    # context.thread.start()
    # yield context.server
    # -- CLEANUP-FIXTURE PART:
    # context.server.shutdown()
    # context.thread.join()
