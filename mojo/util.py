import os
from mojo.config import TEMPLATES_DIR
from passlib.hash import pbkdf2_sha256


def template(path):
    """Template pathing shortcut function."""
    return os.path.join(TEMPLATES_DIR, path)


def encrypt(password):
    hash = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)
    return hash


def verify(password, hash):
    return pbkdf2_sha256.verify(password, hash)


def error_404(self):
    self.clear()
    self.set_status(404)
    self.render(template('404.html'))
