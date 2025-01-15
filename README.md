# Chat Application

A real-time chat application built with Django and Django Channels. This application allows users to sign up, log in, and communicate with other users in real-time using WebSockets.

---

## Features

- User authentication (sign-up and log-in)
- List of all registered users in a collapsible left menu
- Ability to select a user and initiate a chat
- Real-time messaging with WebSocket
- Old messages retrieval from the database
- Responsive and user-friendly chat interface

---

## Prerequisites

Ensure the following are installed on your system:

1. **Python** (version 3.8 or higher)
2. **Redis** (for production-level WebSocket handling)
3. **Pipenv** or **virtualenv** (for virtual environment management)

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository_url>
cd chat_project
```

### 2. Create a Virtual Environment
#### Using `virtualenv`:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the Database
By default, the project uses SQLite. If you'd like to use another database, update the `DATABASES` setting in `chat_project/settings.py`.

Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser
```bash
python manage.py createsuperuser
```
Follow the prompts to set up admin credentials.

### 6. Run Redis (Optional for Development)
If you plan to use Redis for `CHANNEL_LAYERS`, ensure Redis is running:
```bash
redis-server
```

### 7. Start the Development Server
```bash
python manage.py runserver
```

Open your browser and navigate to:
```
http://127.0.0.1:8000/chat_app/
```

---

## Project Structure

```plaintext
chat_project/
|— chat_project/         # Project settings and configurations
|— chat_app/             # Main chat application
   |— templates/         # HTML templates
   |— static/            # Static files (CSS, JS)
   |— routing.py         # WebSocket routing
   |— consumers.py       # WebSocket consumers
|— db.sqlite3           # SQLite database (default)
|— manage.py            # Django management script
|— requirements.txt     # Python dependencies
```

---

## How to Use

1. Navigate to `/chat_app/` after starting the server.
2. Sign up or log in using the authentication system.
3. Select a user from the left menu to start a chat.
4. Type your message in the input box and press "Send" to chat in real-time.

---

## WebSocket Debugging

If the WebSocket connection fails:
- Ensure the server is running.
- Check Redis (if used) is running.
- Verify the WebSocket URL in your browser console.
- Review server logs for WebSocket errors.

---

## Deployment

### 1. Using Gunicorn and Daphne
Install production dependencies:
```bash
pip install gunicorn daphne
```

Run the server:
```bash
daphne -b 0.0.0.0 -p 8000 chat_project.asgi:application
```

### 2. Configure Nginx and HTTPS
Set up a reverse proxy using Nginx and secure the application with HTTPS using a service like Let's Encrypt.

---

## Support
If you encounter any issues or have questions, please reach out to the project maintainer.
