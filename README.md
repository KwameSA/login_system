# LushLyrics Fork – User Authentication Implementation

This repository contains my fork of the [LushLyrics](https://github.com/original-repo](https://github.com/mohammedwed/Lushlyrics-insecure)) project with a focus on implementing secure **user authentication and password management** workflows.

---

## Overview

The main goal of this fork was to enhance the user experience and security of the application by implementing:

- **Login and Logout functionality**  
- **User registration (signup) workflow**  
- **Password reset workflow**, including reset via email  
- **Access restriction for unauthenticated users**  

This ensures that only registered users can access the LushLyrics content, providing a secure and professional experience for users.

---

## Features Implemented

### 1. User Registration
- Custom signup form using Django’s `UserCreationForm` with email validation.
- Password confirmation and validation to prevent duplicates or weak passwords.
- Prevents duplicate emails using `clean_email()` method in `RegisterForm`.

### 2. Login / Logout
- Users can log in using their **username** (future extension: support email login).
- Logout redirects users to the login page.
- Error messages displayed for invalid credentials.

### 3. Password Reset Workflow
- Complete workflow implemented using Django’s built-in password reset views:
  - `PasswordResetView` – request password reset via email.
  - `PasswordResetDoneView` – confirmation that reset email was sent.
  - `PasswordResetConfirmView` – set new password using secure token link.
  - `PasswordResetCompleteView` – confirmation that password was successfully changed.
- Email simulation via console backend for development.
- Fully styled forms (`password_reset.css`) for consistency with the application design.

### 4. Access Restriction
- All website content is restricted to authenticated users.
- Anonymous users are redirected to the login page.

---

## Technologies Used

- **Backend**: Python 3.11, Django 3.0.7  
- **Frontend**: HTML5, CSS3, Font Awesome (icons)  
- **Version Control**: Git & GitHub  
- **Authentication**: Django built-in authentication system (`UserCreationForm`, `LoginView`, `LogoutView`, password reset views)  

---

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/lushlyrics-fork.git
cd lushlyrics-fork
```

2. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```
3. Install dependencies:
```
pip install -r requirements.txt
```

4. Run migrations:
```
python manage.py migrate
```
5. Run the development server:
   ```
   python manage.py runserver
   ```
6.Access the application:
```
http://127.0.0.1:8000
```

### Usage

1. Signup – Create a new user account with a unique username and email.

2. Login – Authenticate using your username (and password).

3. Logout – Click logout to end the session.

4. Password Reset – Click “Forgot Password?” on login to initiate password recovery. Follow the console email link to reset your password.

## Notes

Password reset emails are sent to the console in development.

Ensure the venv/ directory is excluded from Git via .gitignore.

This fork focuses solely on authentication workflows; the main LushLyrics functionality (music playback, playlists) remains unaltered.

## License

This project is licensed under the Apache License 2.0. See the LICENSE file for details.

# Author

Samuel Akuffo – Implementation of authentication workflows for the LushLyrics fork.


