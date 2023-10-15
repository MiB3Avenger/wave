# Worker setup
workers = 4
keepalive = 30
timeout = 60

# Logging setup
errorlog = '-'  # Log to stdout
accesslog = '-'  # Log to stdout
loglevel = 'info'
access_log_format = '''{"logname":"accesslog", "message": "%(h)s %(l)s %(u)s %(t)s \\"%(r)s\\" %(s)s %(b)s \\"%(f)s\\" \\"%(a)s\\""}'''
