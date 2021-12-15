import threading
from queue import Queue


class Jobs():
	def __init__(self):
		super(Jobs, self).__init__()
		self.queue = Queue()

	def add(self, job):
		self.queue.put(job)

	def get(self):
		return self.queue.get()

	def done(self):
		self.queue.task_done()

	def count(self):
		return int(self.queue.qsize())

	def join(self):
		self.queue.join()

	def empty(self):
		return self.queue.empty()



class Thread(threading.Thread):
	def __init__(self, func, args=''):
		super(Thread, self).__init__()
		self.func = func
		self.args = args

	def run(self):
		try:
			if self.args == '':
				self.result = self.func()
			else:
				self.result = self.func(*self.args)
		except Exception as e:
			print('thread exception:', e)


class Threads():
	def __init__(self, func, args='', ntask=1):
		super(Threads, self).__init__()
		self.ntask = ntask
		self.func = func
		self.args = args

	def start(self):
		for i in range(1, self.ntask+1):
			worker = Thread(func=self.func, args=self.args)
			worker.start()
