# Job Board Platform

## Overview
Welcome to the Job Board Platform API! This project is a powerful job board system built using Django and Django REST Framework (DRF). It provides essential functionalities for managing job postings, candidate profiles, resume uploads, and job application tracking.

Additionally, the project includes comprehensive test coverage using `pytest` and `Coverage.py`, ensuring high code reliability and maintainability.

## Features

### User Authentication
- **JWT Authentication**: Secure authentication using Djoser and JSON Web Tokens (JWT).
- **Custom User Model**: Supports employer and job seeker roles with specific permissions.

### Job Listings
- **Create, Update, Delete Job Listings**: Employers can manage job postings.
- **Categorized Job Listings**: Organize jobs based on industries and job types.
- **Search and Filter**: Search jobs by keywords, location, industry, and job type.

### Candidate Profiles
- **Profile Management**: Job seekers can create and update their profiles.
- **Resume Upload**: Candidates can upload resumes for job applications.
- **Skill & Experience Tracking**: Store job seekers' skills, experience, and education history.

### Job Applications
- **Apply for Jobs**: Job seekers can apply directly from the platform.
- **Application Tracking**: Track application status (Pending, Reviewed, Accepted, Rejected).
- **Employer Dashboard**: Employers can view and manage received applications.

### Reporting and Analytics
- **Job Posting Analytics**: Employers can track views and applications per job.
- **User Insights**: Analyze job seeker engagement and preferences.
- **Admin Dashboard**: Track platform usage and job posting trends.

### Testing and Coverage
- **Unit Tests**: Comprehensive tests for all functionalities using `pytest`.
- **Coverage Analysis**: Uses `Coverage.py` to measure test coverage, ensuring 90%+ code coverage.

## Installation

### Prerequisites
- Python 3.8+
- PostgreSQL
- Django 5.1.6
- Poetry (Python package manager)

### Setup

1. **Clone the Repository**
```bash
git clone https://github.com/Andrew-oduola/job_board_api.git
cd job_board_api
```

2. **Create a Virtual Environment and Activate It**
```bash
poetry install
poetry shell
```

3. **Set Up Environment Variables**
Create a `.env` file in the project root and add the following:

```env
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_NAME=your_database_name
DATABASE_USER=your_database_user
DATABASE_PASSWORD=your_database_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

4. **Run Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create a Superuser**
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin user.

6. **Run the Development Server**
```bash
python manage.py runserver
```
Access the application at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## API Endpoints

### Authentication
- **Login**: `POST /auth/jwt/create/`
- **Refresh Token**: `POST /auth/jwt/refresh/`
- **Verify Token**: `POST /auth/jwt/verify/`

### Job Listings
- **List Jobs**: `GET /api/jobs/list/`
- **Create Job**: `POST /api/jobs/list/`
- **Retrieve Job**: `GET /api/jobs/list/{id}/`
- **Update Job**: `PUT /api/jobs/list/{id}/`
- **Delete Job**: `DELETE /api/jobs/list/{id}/`


### Job Applications
- **List Applications**: `GET /api/jobs/applications/`
- **Create Application**: `POST /api/jobs/applications/`
- **Retrieve Application**: `GET /api/jobs/applications/{id}/`
- **Update Application**: `PUT /api/jobs/applications/{id}/`
- **Delete Application**: `DELETE /api/jobs/applications/{id}/`

## Running Tests and Coverage Analysis

### Install and Set Up Pytest & Coverage
```bash
poetry add --dev pytest pytest-django coverage
```

### Run Pytest
```bash
pytest
```

### Measure Test Coverage
```bash
coverage run -m pytest
coverage report -m
```
Ensure that test coverage is at least 90%.

### Generate HTML Coverage Report
```bash
coverage html
```
Open `htmlcov/index.html` in a browser to view detailed coverage analysis.

## Project Structure

```
📂 job_board
│── 📁 users           # User authentication and management
│── 📁 jobs            # Job postings
│── 📁 applications    # Job applications
│── 📁 candidates      # Candidate profiles
│── 📁 analytics       # Reporting and analytics
│── 📁 job_board       # Main project file
│── 📄 manage.py       # Django project manager
│── 📄 poetry.lock     # Poetry dependencies lock file
│── 📄 pyproject.toml  # Project dependencies and config
│── 📄 .env            # Environment variables
│── 📄 pytest.ini
📄 README.md       # Project documentation
📄 .gitignore
```

Happy Coding! 🚀

