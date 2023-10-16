from todolist import TodoList
from redis import Redis

cli = Redis(decode_responses=True)
user_id = "xiwa"
l = TodoList(cli, user_id)

print(l.add("server"))
print(l.add("fft"))
print(l.show_todo_list())
print(l.done("fft"))
print(l.show_todo_list())
print(l.show_done_list())
print(l.remove("server"))
print(l.show_todo_list())
