from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import parse_qs
import os

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1
        self.load_tasks()

    def add_task(self, title, priority):
        task = {
            'title': title,
            'priority': priority,
            'isDone': False,
            'id': self.next_id
        }
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
        return task

    def get_tasks(self):
        return self.tasks

    def complete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['isDone'] = True
                self.save_tasks()
                return True
        return False

    def save_tasks(self):
        with open('tasks.txt', 'w') as file:
            json.dump(self.tasks, file)

    def load_tasks(self):
        if os.path.exists('tasks.txt'):
            with open('tasks.txt', 'r') as file:
                self.tasks = json.load(file)
            if self.tasks:
                self.next_id = max(task['id'] for task in self.tasks) + 1

class TaskHandler(BaseHTTPRequestHandler):
    task_manager = TaskManager()

    def do_GET(self):
        if self.path == '/tasks':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(self.task_manager.get_tasks()).encode('utf-8'))
        elif self.path == '/form':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(self.generate_form().encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == '/tasks':
            length = int(self.headers['Content-Length'])
            post_data = json.loads(self.rfile.read(length).decode('utf-8'))
            task = self.task_manager.add_task(post_data['title'], post_data['priority'])
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(task).encode('utf-8'))
        elif self.path == '/form':
            length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(length).decode('utf-8')
            data = parse_qs(post_data)
            title = data.get('title', [''])[0]
            priority = data.get('priority', [''])[0]
            if title and priority:
                self.task_manager.add_task(title, priority)
                self.send_response(303)  # Перенаправляем обратно на форму
                self.send_header('Location', '/form')
            else:
                self.send_response(400)
            self.end_headers()
        elif self.path.startswith('/tasks/') and self.path.endswith('/complete'):
            task_id = int(self.path.split('/')[-2])
            if self.task_manager.complete_task(task_id):
                self.send_response(200)
            else:
                self.send_response(404)
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()
    
    def generate_form(self):
        return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Task Manager</title>
        </head>
        <body>
            <h1>Task Manager</h1>
            <h2>Add Task</h2>
            <form action="/form" method="POST">
                <label for="title">Title:</label>
                <input type="text" id="title" name="title" required>
                <br><br>
                <label for="priority">Priority:</label>
                <select id="priority" name="priority">
                    <option value="low">Low</option>
                    <option value="normal">Normal</option>
                    <option value="high">High</option>
                </select>
                <br><br>
                <button type="submit">Add Task</button>
            </form>
            <h2>Tasks</h2>
            <ul>
                {}
            </ul>
        </body>
        </html>
        '''.format(
            ''.join(
                f'<li>{task["title"]} ({task["priority"]}) - {"Done" if task["isDone"] else "Not Done"}</li>' for task
                in self.task_manager.get_tasks())
        )


def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, TaskHandler)
    print('Server running on port 8000...')
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()