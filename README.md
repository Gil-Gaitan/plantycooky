# plantycooky
Site Update V2.1 Omega (IN DEVELOPMENT) Course: blog.miguelgringberg.com THANKS!!!

# Plant Seeds Cook - Flask Web Application

## Project Overview
Welcome to the **Plant Seeds Cook** web application! This project is a Flask-based web app that I am building to showcase my backend skills, data engineering techniques, and algorithm implementations. It serves as a hub for learning, applying, and sharing various web technologies, including databases, APIs, and user authentication.

This project includes:
- Flask for backend development
- SQLAlchemy for database interactions
- Flask-Login for user authentication
- Docker for containerization

### Features
1. **User Authentication:** Login and logout functionality with secure password checks.
2. **Homepage:** Display personalized posts and messages for authenticated users.
3. **Data Engineering:** The backend connects to a MySQL database for managing user data.
4. **Dynamic Routing:** Routes include home, login, and logout pages, with dynamic content rendering based on user data.

## Installation & Setup
To get started with this project, follow the steps below:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/plant-seeds-cook.git
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the database:
    ```bash
    flask db upgrade
    ```

4. Run the application:
    ```bash
    flask run
    ```

## Docker Setup
To run the application in a Docker container, follow these steps:

1. Build the Docker image:
    ```bash
    docker build -t plant-seeds-cook .
    ```

2. Run the container:
    ```bash
    docker run -p 5000:5000 plant-seeds-cook
    ```

## Credits
A huge thank you to [Miguel Grinberg](https://blog.miguelgrinberg.com) for his excellent tutorials and insights on Flask and web development. His work has been instrumental in shaping this project and helping me understand the core concepts of Flask and user authentication.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

