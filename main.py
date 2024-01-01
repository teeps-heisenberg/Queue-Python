from queues import Queue

my_queue = Queue(4)

my_queue.print_queue()

my_queue.enqueue(67)
my_queue.enqueue(98)
my_queue.enqueue(24)
my_queue.print_queue()

my_queue.dequeue()
my_queue.print_queue()