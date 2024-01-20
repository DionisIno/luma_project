"""This section contains data for testing of the SignIn Page"""

import pytest

from data.credentials import credentials


sign_in_data = {
    "h1_heading": 'Customer Login',
    "customer_login_heading": 'Registered Customers',
    "new_customers_heading": 'New Customers',
    "customer_login_note": 'If you have an account, sign in with your email address.',
    "email_label": 'Email',
    "password_label": 'Password',
    "forgot_password_link_text": 'Forgot Your Password?',
    "sign_in_btn": 'Sign In',
    "new_customers_note": 'Creating an account has many benefits: check out faster, keep more than one address, track orders and more.',
    "create_account_btn": 'Create an Account',
}

LOGIN = [
        (credentials['email'], credentials['password']),
        pytest.param(
            credentials['invalid_email'], credentials['password'],
        ),
        pytest.param(
            credentials['email'], credentials['invalid_password'],
        ),
        pytest.param(
            '', credentials['password'],
        ),
        pytest.param(
            credentials['email'], '',
        ),
        (credentials['case_sensitive_email'], credentials['password']),
        pytest.param(
            credentials['email'], credentials['case_sensitive_password'],
        ),
        (credentials['email_with_spaces'], credentials['password']),
        pytest.param(
            credentials['email'], credentials['password_with_leading_spaces'],
        ),
        pytest.param(
            credentials['email'], credentials['password_with_trailing_spaces'],
        )
    ]

sign_in_errors = {
    "incorrect_email_format_msg": 'Please enter a valid email address (Ex: johndoe@domain.com).',
    "required_field_msg": 'This is a required field.',
    "invalid_credentials_msg":
        'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.',
    "incorrect_captcha_msg": 'Incorrect CAPTCHA',
}
