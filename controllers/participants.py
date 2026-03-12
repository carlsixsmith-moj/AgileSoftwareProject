from flask import Blueprint, render_template, request, redirect, url_for, abort
from flask_login import login_required
from models import Participant, db
from datetime import datetime
from controllers.auth import admin_required

participants_bp = Blueprint('participants', __name__, url_prefix='/participants')

"""Index route for the participants controller """
@participants_bp.route('/')
@login_required
def list_participants():
    participants = Participant.query.all()
    return render_template('participants/list.html', participants=participants)

@participants_bp.route('/<string:id>/edit', methods=['GET','POST'])
@login_required
def edit_participant(id):
    participant = db.session.get(Participant, id)

    if participant is None:
        abort(404)

    if request.method=='POST':
        name = request.form['name']
        dob_str = request.form.get('dob', '').strip()

        try:
            # Parse date string from form (expects YYYY-MM-DD format)
            if dob_str:
                participant.dob = datetime.strptime(dob_str, '%Y-%m-%d').date()
            participant.name = name
            db.session.commit()
            return redirect(url_for('participants.list_participants'))
        except ValueError as e:
            error = str(e)
            return render_template('participants/edit.html', error=error, participant = participant, form_dob=dob_str)
    
    return render_template('participants/edit.html', participant = participant)


@participants_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_participant():
    if request.method == 'POST':
        participant_id = (request.form.get('id') or '').strip()
        name = (request.form.get('name') or '').strip()
        dob_str = (request.form.get('dob') or '').strip()

        try:
            # Parse date string from form (expects YYYY-MM-DD format)
            if not dob_str:
                raise ValueError('Date of birth is required.')
            
            try:
                dob = datetime.strptime(dob_str, '%Y-%m-%d').date()
            except ValueError:
                raise ValueError('Invalid date format. Please use YYYY-MM-DD.')
            
            existing_participant = Participant.query.filter_by(id=participant_id).first()
            if existing_participant is not None:
                error = 'Participant ID already exists. Please use a unique ID.'
                return render_template('participants/add.html', error=error, form_id=participant_id, form_name=name, form_dob=dob_str)

            new_participant = Participant(id=participant_id, name=name, dob=dob)
            db.session.add(new_participant)
            db.session.commit()
            return redirect(url_for('participants.list_participants'))
        except ValueError as e:
            error = str(e)
            return render_template('participants/add.html', error=error, form_id=participant_id, form_name=name, form_dob=dob_str)

    return render_template('participants/add.html')

@participants_bp.route('/<string:id>/delete')
@admin_required
def delete_participant(id):
    participant = db.session.get(Participant, id)

    if participant is None:
        abort(404)

    db.session.delete(participant)
    db.session.commit()

    return redirect(url_for('participants.list_participants'))