# Roomedia

Roomedia is a multipage Django web application representing a portfolio site for an IT company, showcasing both the
company itself and its products. The project incorporates best practices for RESTful APIs using Django Rest Framework (
DRF), Django Debug Toolbar for sql requests optimization, and Simple JWT for API authentication.

## Info

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Maintenance](https://img.shields.io/maintenance/yes/2023)](https://github.com/ArmanPythonistGhandilyan/roomedia_django/commits/master)

[![Version](https://img.shields.io/badge/version-1.0.0-blue)](https://github.com/ArmanPythonistGhandilyan/roomedia_django/releases/tag/v1.0.0)

### API Documentation with swagger

Explore and test the APIs using the interactive Swagger documentation.

- **Swagger UI**: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **ReDoc**: [http://127.0.0.1:8000/redoc/)](http://your-domain-or-local-url/redoc/)

## Features

- **Multipage Website:** Explore the various pages of the site to learn more about the company, its products and full
  use of messages, subscriptions and other forms in site.

- **RESTful API:** Utilizes Django Rest Framework to implement RESTful API endpoints, ensuring efficient communication
  between the frontend and backend.

- **API Authentication with Simple JWT:** Implements Simple JWT for secure API authentication, following
  industry-standard practices.

## Some screenshots from frontend

![Example Screenshot](https://i.imgur.com/OlHWECA.png)

![Dashboard](https://imgur.com/V1mkPMw.png)

![Feature Example](https://i.imgur.com/ppNVS90.png)

![Feature Example](https://i.imgur.com/0aPIhNW.png)

![Feature Example](https://i.imgur.com/TjgGTMx.png)

![Feature Example](https://i.imgur.com/aR3J9l3.png)

![Feature Example](https://i.imgur.com/tXdHAhh.png)

![Feature Example](https://i.imgur.com/HnTU6rx.png)

![Feature Example](https://i.imgur.com/4V21tuI.png)

![Feature Example](https://i.imgur.com/ry2xDoV.png)

![Feature Example](https://i.imgur.com/5UTqeHF.png)

## Getting Started

To run the project locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/ArmanPythonistGhandilyan/roomedia_django_drf.git
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source venv/bin/activate
        ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. **Important Reminder:** Open the `roomedia/settings.py` file and customize the `SECRET_KEY` and `DEBUG` variables
   according to your local development preferences.
6. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

Visit [http://localhost:8000](http://localhost:8000) to explore the Roomedia site locally.

## Contributing

If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## Contacts

If you have questions, suggestions, or want to contribute, feel free to reach out!

- **Author:** Arman Ghandilyan
- **Email:** armanghandilyan977@gmail.com
- **GitHub:** [@ArmanPythonistGhandilyan](https://github.com/ArmanPythonistGhandilyan)
- **LinkedIn:** [Arman Ghandilyan](https://www.linkedin.com/in/arman-ghandilyan/)

Feel free to open issues, submit pull requests, or just drop a message. Your feedback and contributions are highly
appreciated!





 