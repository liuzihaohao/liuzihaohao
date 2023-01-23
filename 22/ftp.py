from pyftpdlib.authorizers import DummyAuthorizer
from  pyftpdlib.handlers  import FTPHandler
from  pyftpdlib.servers import FTPServer
authorizer = DummyAuthorizer()
authorizer.add_user('admin', '123456', '/liuzihao/fileweb/', perm='elradfmwMT')
authorizer.add_anonymous('/liuzihao/fileweb/',perm='elr')
handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(('', 2121), handler)
server.serve_forever() 
