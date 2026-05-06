# Task Tracker - Flask Web Application

A simple, production-ready task management web application built with Flask. Designed specifically for DevOps CI/CD demonstrations with health check endpoints and containerization support.

## Features

✨ **Core Features**
- 📋 Homepage with task display
- ➕ Add new tasks with timestamps
- ✓ Mark tasks as completed/incomplete
- 🗑️ Delete tasks
- 📊 Task statistics dashboard

🏥 **DevOps Features**
- `/health` - Health check endpoint (returns JSON status)
- `/ready` - Kubernetes readiness probe
- `/live` - Kubernetes liveness probe
- `/tasks` - JSON API for task listing
- Docker-ready (included Dockerfile)
- Persistent task storage (JSON file-based)

## Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or download the project**
   ```bash
   cd task-tracker
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the app**
   - Open your browser to: `http://localhost:5000`

## API Endpoints

### Web Interface
- `GET /` - Homepage with task list and add form
- `POST /add` - Add a new task (form submission)
- `POST /complete/<id>` - Toggle task completion status
- `POST /delete/<id>` - Delete a task

### REST API
- `GET /tasks` - Get all tasks as JSON
- `GET /health` - Health check endpoint
- `GET /ready` - Readiness probe (Kubernetes)
- `GET /live` - Liveness probe (Kubernetes)

### Example Health Check Response
```json
{
  "status": "healthy",
  "service": "task-tracker",
  "version": "1.0.0",
  "tasks_count": 5,
  "timestamp": "2026-05-06T10:30:45.123456"
}
```

## Project Structure

```
task-tracker/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker container configuration
├── .gitignore           # Git ignore rules
├── templates/           # HTML templates
│   └── index.html      # Main page template
├── static/              # Static assets
│   └── style.css       # Application styling
└── README.md            # This file
```

## Docker Deployment

### Build Docker Image
```bash
docker build -t task-tracker:latest .
```

### Run Docker Container
```bash
docker run -p 5000:5000 task-tracker:latest
```

### Docker Compose (Optional)
For local development:
```bash
docker-compose up
```

## Development

### Run with Debug Mode
The application runs with `debug=True` by default, enabling:
- Auto-reloading on code changes
- Detailed error pages
- Interactive debugger

### Testing
```bash
# Check health endpoint
curl http://localhost:5000/health

# Get tasks as JSON
curl http://localhost:5000/tasks

# Check liveness
curl http://localhost:5000/live
```

## Environment Variables

- `FLASK_ENV` - Set to `production` for production deployments
- `FLASK_DEBUG` - Set to `0` to disable debug mode
- Port: Configured to run on `0.0.0.0:5000` (accessible from any interface)

## CI/CD Integration

This application is optimized for CI/CD pipelines:

- ✅ Health check endpoints for monitoring
- ✅ Kubernetes-compatible probe endpoints
- ✅ Containerized (Docker-ready)
- ✅ Minimal dependencies
- ✅ Simple startup process
- ✅ JSON APIs for automation

### Example GitHub Actions Deployment
```yaml
- name: Health Check
  run: curl http://localhost:5000/health
```

## Production Considerations

For production deployments:

1. **Disable Debug Mode** - Set `debug=False` in app.py
2. **Use a Production Server** - Replace Flask's development server with:
   - Gunicorn
   - uWSGI
   - Waitress
3. **Use Environment Variables** - Store configuration in environment variables
4. **Set Up Logging** - Configure proper logging
5. **Database** - Replace JSON file storage with a proper database (PostgreSQL, SQLite, etc.)
6. **Security** - Enable HTTPS, CORS headers, input validation

## Example Production Run with Gunicorn
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Troubleshooting

### Port Already in Use
If port 5000 is already in use:
```bash
# Change the port in app.py or use environment variable
python app.py --port 8000
```

### Tasks Not Persisting
- Check that the `tasks.json` file is being created in the project directory
- Ensure the application has write permissions

### Browser Not Loading Styles
- Clear browser cache (Ctrl+Shift+Delete or Cmd+Shift+Delete)
- Ensure static files are properly served

## Contributing

Feel free to extend this application with:
- Database integration (SQLAlchemy)
- User authentication
- Task categories/tags
- Due dates
- Priority levels
- Export/import functionality

## License

This project is provided as-is for educational and demonstration purposes.

## Support

For issues or questions, please check:
1. That Python 3.8+ is installed
2. All dependencies are installed: `pip install -r requirements.txt`
3. The application is running on the correct port
4. Port 5000 is not blocked by firewall

---

**Ready for DevOps Integration** ✅

This application is designed to be easily integrated into CI/CD pipelines, Kubernetes clusters, and container orchestration systems.
