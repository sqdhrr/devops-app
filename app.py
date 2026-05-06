"""
Flask Task Tracker Web Application
A simple task management web app suitable for DevOps CI/CD demonstrations.
"""
from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)

# Simple in-memory task storage (for demo purposes)
TASKS_FILE = 'tasks.json'
tasks = []

def load_tasks():
    """Load tasks from JSON file."""
    global tasks
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r') as f:
                tasks = json.load(f)
        except (json.JSONDecodeError, IOError):
            tasks = []
    else:
        tasks = []

def save_tasks():
    """Save tasks to JSON file."""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

@app.route('/')
def home():
    """Homepage with task display and add task form."""
    load_tasks()
    return render_template('index.html', tasks=tasks, task_count=len(tasks))

@app.route('/add', methods=['POST'])
def add_task():
    """Add a new task."""
    task_title = request.form.get('task_title', '').strip()
    
    if not task_title:
        return redirect(url_for('home'))
    
    load_tasks()
    new_task = {
        'id': len(tasks) + 1,
        'title': task_title,
        'completed': False,
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    tasks.append(new_task)
    save_tasks()
    
    return redirect(url_for('home'))

@app.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    """Mark a task as completed."""
    load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
            break
    save_tasks()
    return redirect(url_for('home'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    """Delete a task."""
    load_tasks()
    tasks[:] = [task for task in tasks if task['id'] != task_id]
    save_tasks()
    return redirect(url_for('home'))

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """API endpoint to get all tasks as JSON."""
    load_tasks()
    return jsonify({
        'status': 'success',
        'total_tasks': len(tasks),
        'tasks': tasks
    })

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint for DevOps/monitoring."""
    load_tasks()
    return jsonify({
        'status': 'healthy',
        'service': 'task-tracker',
        'version': '1.0.0',
        'tasks_count': len(tasks),
        'timestamp': datetime.now().isoformat()
    }), 200

@app.route('/ready', methods=['GET'])
def ready():
    """Readiness check endpoint for Kubernetes."""
    try:
        load_tasks()
        return jsonify({
            'status': 'ready',
            'service': 'task-tracker'
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'not_ready',
            'error': str(e)
        }), 503

@app.route('/live', methods=['GET'])
def live():
    """Liveness check endpoint for Kubernetes."""
    return jsonify({
        'status': 'alive',
        'service': 'task-tracker'
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
