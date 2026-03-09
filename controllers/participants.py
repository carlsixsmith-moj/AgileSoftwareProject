from flask import Blueprint, render_template, request, redirect, url_for, abort
from models import Participant, db

participants_bp = Blueprint('participants', __name__)

"""Index route for the participants controller """
@participants_bp.route('/')
def list_participants():
    participants = Participant.query.all()
    return render_template('participants.html', participants=participants)

@participants_bp.route('/edit/<string:id>', methods=['GET','POST'])
def edit_participant(id):
    participant = db.session.get(Participant, id)

    if participant is None:
        abort(404)

    if request.method=='POST':
        name = request.form['name']

        if(len(name) > 50):
            error = 'Participant name must be 50 characters or less'
            return render_template('edit_participant.html', error=error, participant = participant)

        
        participant.name = name

        db.session.commit()
        return redirect(url_for('participants.list_participants'))
    
    return render_template('edit_participant.html', participant = participant)


@participants_bp.route('/add', methods=['GET', 'POST'])
def add_participant():
    if request.method == 'POST':
        participant_id = (request.form.get('id') or '').strip()
        name = (request.form.get('name') or '').strip()

        if len(participant_id) != 9:
            error = 'Participant ID must be exactly 9 characters long.'
            return render_template('add_participant.html', error=error, form_id=participant_id, form_name=name)

        existing_participant = Participant.query.filter_by(id=participant_id).first()
        if existing_participant is not None:
            error = 'Participant ID already exists. Please use a unique ID.'
            return render_template('add_participant.html', error=error, form_id=participant_id, form_name=name)

        new_participant = Participant(id=participant_id, name=name)
        db.session.add(new_participant)
        db.session.commit()
        return redirect(url_for('participants.list_participants'))

    return render_template('add_participant.html')

@participants_bp.route('/delete/<string:id>')
def delete_participant(id):
    participant = db.session.get(Participant, id)

    if participant is None:
        abort(404)

    db.session.delete(participant)
    db.session.commit()

    return redirect(url_for('participants.list_participants'))