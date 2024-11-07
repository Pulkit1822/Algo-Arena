# Algo Arena Online Judge

## Project Overview

Algo Arena's Online Judge is a platform for competitive programming and algorithm development. The online judge system evaluates submitted code against test cases and provides instant feedback on correctness. It is designed to help users improve their coding skills by solving problems based on Data Structures and Algorithms (DSA).

## Technologies Used

- **Python**: The primary programming language used for the backend.
- **Django**: A high-level Python web framework used to build the online judge system.
- **SQLite**: A lightweight database used for storing user submissions and problem data.
- **Bootstrap**: A CSS framework used for styling the web pages.
- **Monaco Editor**: A code editor that provides a rich coding experience for users.

## Key Features

- **Code Submission and Execution**: Users can submit their code through a web interface and execute it on the platform.
- **Test Case Evaluation**: The platform evaluates the submitted code against predefined test cases, providing instant feedback on its correctness.
- **Custom Input Support**: Users can input custom test cases to further test their solutions.
- **Execution Time Tracking**: Utilizes Django's template language to display execution time alongside the output.
- **Memory Usage Monitoring**: Tracks memory usage using the `tracemalloc` module to help users optimize their code.
- **Error Suggestions**: Provides suggestions for fixing errors in the code by highlighting the particular section where the mistake is located.
- **User Experience Enhancement**: Utilizes Bootstrap CSS and jQuery to improve the appearance and functionality of the platform's HTML template.
- **Result Display**: Upon execution, users are presented with a screen indicating whether their code passed all test cases or not.
- **Monaco Editor**: Implemented the Monaco editor for better Python language readability and an enhanced code editing experience.
- **Dark Mode**: Added a dark mode facility for reducing eye strain and improving usability in low-light environments.
- **Responsive UI**: Enhanced the UI to be more responsive, providing a better experience on various devices.

## Setup and Run Locally

To set up and run the online judge project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Pulkit1822/Algo-Arena.git
    cd Algo-Arena/Online\ Judge/OnlineCompiler
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run database migrations**:
    ```bash
    python manage.py migrate
    ```

4. **Start the development server**:
    ```bash
    python manage.py runserver
    ```

5. **Open the application in your browser**:
    ```bash
    http://localhost:8000
    ```

## Contribution Guidelines

We welcome contributions to the Algo Arena online judge project. To contribute, follow these steps:

1. **Fork the repository**: Click on the "Fork" button at the top right corner of the repository page.

2. **Clone your forked repository**:
    ```bash
    git clone https://github.com/your-username/Algo-Arena.git
    cd Algo-Arena/Online\ Judge/OnlineCompiler
    ```

3. **Create a new branch**:
    ```bash
    git checkout -b feature-branch
    ```

4. **Make your changes**: Implement your changes and commit them with a meaningful commit message.

5. **Push your changes**:
    ```bash
    git push origin feature-branch
    ```

6. **Create a pull request**: Go to the original repository and create a pull request from your forked repository.

Thank you for contributing to Algo Arena!
