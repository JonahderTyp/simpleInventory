import multiprocessing

# Basic Gunicorn config
bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1

accesslog = "acess.log"
# Use gevent for async workers, if your app is I/O bound
# worker_class = 'gevent'

# Pre-start hook to run only once before any workers are started
def on_starting(server):
    import simpleInventory.prestart as pr
    pr.pre_start()
