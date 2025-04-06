# Python Server-Side Rendering 🖥️

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green.svg)
![Jinja2](https://img.shields.io/badge/Jinja2-3.0%2B-red.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.0-purple.svg)

## 📖 Description
This project demonstrates server-side rendering techniques in Python web applications using Flask and Jinja2. It focuses on building web interfaces where HTML is generated on the server before being sent to the client's browser. This approach offers advantages like improved SEO, faster initial page loads, and better compatibility across devices. Through practical examples, the project explores template rendering, form processing, data persistence, and dynamic content generation techniques essential for modern web development.

## 📂 Contents
- **task_01_basic_template.py**: Introduction to Flask and basic template rendering
- **task_02_dynamic_content.py**: Passing variables from Python to templates 
- **task_03_template_inheritance.py**: Creating reusable layouts with template inheritance
- **task_04_forms.py**: Handling form submissions and validation
- **task_05_database.py**: Connecting templates with database content
- **templates/**: Directory containing Jinja2 HTML templates
  - **base.html**: Base template providing common structure for all pages
  - **layout.html**: Base template with common structure and Bootstrap integration
  - **home.html**: Landing page template
  - **dashboard.html**: User dashboard after authentication
  - **login.html**: User authentication form
  - **register.html**: New user registration form
- **static/**: Directory for static assets
  - **css/custom.css**: Custom styling extensions
  - **js/scripts.js**: Client-side interactivity
  - **images/**: Project images and icons
- **database.py**: Database connection and query management
- **forms.py**: Form classes with validation rules
- **utils.py**: Helper functions and utilities

## 🚀 Getting Started
1. Install required packages:
   ```bash
   pip install flask jinja2 flask-wtf
   ```

2. Set up the Flask environment:
   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   ```

3. Run the Flask development server:
   ```bash
   flask run
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:5000/
   ```

## 🛠️ Requirements
- Python 3.8+
- Flask 2.0+
- Jinja2 3.0+
- Flask-WTF (for form handling)
- Web browser with JavaScript enabled
- Ubuntu 20.04 LTS recommended

## Key Concepts ✨
- **Server-Side Rendering**: Generating HTML on the server instead of the client
- **Templating Engine**: Using Jinja2 to create dynamic HTML
- **Template Inheritance**: Building reusable page layouts through extending base templates
- **Context Variables**: Passing data from Python to HTML templates
- **Form Handling**: Processing and validating form submissions
- **Flash Messages**: Providing feedback to users
- **URL Routing**: Mapping URLs to Python functions
- **Session Management**: Maintaining user state across requests

## Examples

### Basic Flask Application
```python
#!/usr/bin/python3
"""Simple Flask application with Jinja2 templating"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Render the home page"""
    return render_template('index.html', title="Home Page", 
                          message="Welcome to Server-Side Rendering!")

@app.route('/about')
def about():
    """Render the about page"""
    return render_template('about.html', title="About Us")

if __name__ == '__main__':
    app.run(debug=True)
```

### Jinja2 Template
```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{{ url_for('index') }}">Home</a></li>
                <li><a href="{{ url_for('about') }}">About</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        {% block content %}{% endblock %}
    </main>
    
    <footer>
        <p>&copy; 2023 Python SSR Example</p>
    </footer>
</body>
</html>
```

### Template Extension
```html
<!-- templates/index.html -->
{% extends 'base.html' %}

{% block content %}
    <h1>{{ title }}</h1>
    <p>{{ message }}</p>
    
    {% if user %}
        <p>Hello, {{ user.name }}!</p>
    {% else %}
        <p>Please log in to continue.</p>
    {% endif %}
    
    <h2>List of Items</h2>
    <ul>
        {% for item in items %}
            <li>{{ item }}</li>
        {% else %}
            <li>No items found.</li>
        {% endfor %}
    </ul>
{% endblock %}
```

### Form Handling
```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask-wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators = DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

class LoginForm(FlaskForm):
    """Login form definition"""
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle login form submission"""
    form = LoginForm()
    if form.validate_on_submit():
        # Process form data
        email = form.email.data
        password = form.password.data
        # Check credentials...
        flash('Login successful!', 'success')
        return redirect(url_for('index'))
    return render_template('login.html', title="Login", form=form)
```

## License
![License](https://img.shields.io/badge/License-MIT-green.svg)  
This project is under the MIT License.

## Author ✍️
- Benjamin Ristord