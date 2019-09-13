import multiprocessing

bind = '0.0.0.0:7070'
workers = multiprocessing.cpu_count() * 2 + 1
timeout = 30
worker_connections = 1000
