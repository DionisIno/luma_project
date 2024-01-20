"""This section contains data for testing of the Forgot Your Password Page"""

import random
import string


forgot_your_password_data = {
    "h1_heading": 'Forgot Your Password?',
    "forgot_your_password_note": 'Please enter your email address below to receive a password reset link.',
    "email_label": 'Email',
    "captcha_field_label": 'Please type the letters and numbers below',
    "reload_captcha_btn": 'Reload captcha',
    "captcha_image_alt_text": 'Please type the letters and numbers below',
    "reset_my_password_btn": 'Reset My Password',
}

forgot_your_password_errors = {
    "incorrect_email_format_msg": 'Please enter a valid email address (Ex: johndoe@domain.com).',
    "required_field_msg": 'This is a required field.',
    "incorrect_captcha_msg": 'Incorrect CAPTCHA',
}

captcha = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

captcha_img_link = "https://magento.softwaretestingboard.com/pub/media/captcha/base/1e395ab056006f9368cbaec8dce78af7.png"
