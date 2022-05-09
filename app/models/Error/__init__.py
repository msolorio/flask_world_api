default_general_err_msg = 'There was an error.'

class generalError():
    def __init__(self, message=default_general_err_msg, status=500):
        self.message = message
        self.status = status




default_client_err_msg = 'There was an issue with your request.'

class ClientError(generalError):
    def __init__(self, message=default_client_err_msg):
        self.message = message
        self.status = 400



default_server_err_msg = 'There was an error getting your data.'

class ServerError(generalError):
    def __init__(self, message=default_server_err_msg):
        self.message = message
        self.status = 500
