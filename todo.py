"""Simple TODO list application."""
   
   class TodoList:
       def __init__(self):
           self.todos = []
       
       def add_todo(self, task):
           """Add a new todo item."""
           self.todos.append({'task': task, 'completed': False})
       
       def list_todos(self):
           """List all todos."""
           return self.todos
   
   if __name__ == "__main__":
       todo_list = TodoList()
       todo_list.add_todo("Learn about Jules")
       print(todo_list.list_todos())
