# NETFILM Authentication Service

## Overview

NETFILM Authentication Service is a simple Flask-based application that provides user authentication features. It allows users to register, log in, reset passwords, and log out. This application is containerized using Docker for easy portability and deployment.

## Features
- **User Registration**: Allows new users to create an account.
- **User Login**: Allows existing users to log in to their account.
- **Password Reset**: Users can request a password reset via email.
- **Home Page**: Displays a home page for users after logging in, inspired by Netflix.
- **Logout**: Allows users to log out from their account.

## Project Structure

```
AUTHENTICATION_SERVICE/
├── app/
│   ├── templates/
│   │   ├── index.html
│   │   ├── register.html
│   │   ├── login.html
│   │   ├── reset_password.html
│   │   └── home.html
│   ├── __init__.py
│   └── app.py
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt
```

- **app/**: Contains the application code.
  - **templates/**: HTML templates for the web interface.
  - **app.py**: Main Flask application file.
- **Dockerfile**: Defines the instructions to containerize the application.
- **requirements.txt**: Lists the dependencies required for the project.
- **README.md**: Documentation for the project.

## Prerequisites

- **Docker**: Make sure Docker is installed on your system.
- **Python 3.9+**: For local development.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd AUTHENTICATION_SERVICE
```

### 2. Create a Virtual Environment (Optional for Local Development)

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

Install all the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Run the Application Locally

You can run the Flask app locally with the following command:

```bash
python app/app.py
```

Visit `http://localhost:5000` to see the application in action.

## Docker Instructions

To containerize the application and run it with Docker, follow these steps.

### 1. Build the Docker Image

```bash
docker build -t authentication_service .
```

### 2. Run the Docker Container

```bash
docker run -p 5000:5000 authentication_service
```

This command runs the application in a Docker container and maps port 5000 of your local machine to port 5000 of the container.

### 3. Access the Application

Open your browser and navigate to `http://localhost:5000` to access the application.
