from ..models import ServerError

def build_handled_query(query):
    def handled_query(*kwargs, **args):
        try:
            return query(*kwargs, **args)

        except:
            return ServerError()

    return handled_query
