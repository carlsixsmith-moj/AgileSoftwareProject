from functools import wraps
from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


def admin_required(f):
    """Decorator that requires the current user to be an admin."""
    @wraps(f)
    @login_required
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('participants.list_participants'))

    error = None
    if request.method == 'POST':
        username = (request.form.get('username') or '').strip()
        password = request.form.get('password') or ''

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('participants.list_participants'))
        else:
            error = 'Invalid username or password.'

    return render_template('auth/login.html', error=error)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth_bp.route('/register', methods=['GET', 'POST'])
@admin_required
def register():
    """Only admins can create new user accounts."""
    error = None
    if request.method == 'POST':
        username = (request.form.get('username') or '').strip()
        password = request.form.get('password') or ''
        role = request.form.get('role', 'user')

        if not username or not password:
            error = 'Username and password are required.'
        elif role not in ('admin', 'user'):
            error = 'Invalid role.'
        elif User.query.filter_by(username=username).first():
            error = 'Username already exists.'
        else:
            new_user = User(username=username, role=role)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash(f'User "{username}" created successfully.', 'success')
            return redirect(url_for('auth.register'))

    return render_template('auth/register.html', error=error)
