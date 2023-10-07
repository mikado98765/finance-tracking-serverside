"""Finance development configuration."""

import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = b'\x98^\xc2\xb2\xd6\xfe\xbae\x88\xa4\x8d\xefa\x05\xa8\xb1\xbb\xe3\xc6e\xa6\xd7\x9c#'
SESSION_COOKIE_NAME = 'login'

# # File Upload to var/uploads/
FINANCE_ROOT = pathlib.Path(__file__).resolve().parent.parent
# UPLOAD_FOLDER = FINANCE_ROOT/'var'/'uploads'
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
# MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Database file is var/finance.sqlite3
DATABASE_FILENAME = FINANCE_ROOT/'var'/'finance.sqlite3'

