import traceback
from ..models import ServerError

def build_handled_query(query):
    def handled_query(*kwargs, **args):
        try:
            return query(*kwargs, **args)

        except:
            print('Stack Trace ==>', traceback.format_exc())

            return ServerError()

    return handled_query
