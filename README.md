# Django Resume Uploader

Django Resume Uploader is a web application built with Django that facilitates the upload and management of resumes. It provides a user-friendly interface for users to upload their resumes, and administrators can review and manage the submitted resumes.

## Features

- **Resume Upload:** Users can upload their resumes through a user-friendly interface.
- **Admin Panel:** Admins can view and manage all submitted resumes.
- **File Storage:** Resumes are stored on the server.
- **Responsive Design:** The application is designed to work seamlessly on various devices.

## Prerequisites

Make sure you have the following installed before running the application:

- Python 3.x
- Django (latest version)

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/Prasad981998/ResumeUploader.git
    ```
    
2. Install dependencies:to use image field in your project.

    ```bash
    pip install pillow
    ```

3. register media file in setting.py file (at the end).

    ```bash
    MEDIA_URL = '/media/'
    MEDIA_ROOT=BASE_DIR/'media'
    ```

4. modules to import and update urls.py file:

    ```bash
    from django.conf import settings 
    from django.conf.urls.static import static #to show images from myimage

    urlpatterns = [
        
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```

5. Run the migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```


4. Create a superuser for admin access:

    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Open your browser and go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to log in with the superuser credentials and manage resumes.

## Usage

- Create a new account or log in if you already have one.
- Navigate to the "Upload Resume" section to upload your resume.
- User can view uploaded resume in web page.
- Admins can review and manage submitted resumes in the admin panel.
- Have a seamless experience managing resumes with Django Resume Uploader!

## Contributing

If you'd like to contribute to this project, please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the Django community for their amazing framework.

## NOTE
- This project is in development phase many functionalities are in process to update.

