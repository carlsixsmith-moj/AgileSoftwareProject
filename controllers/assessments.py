from flask import Blueprint, render_template, request, redirect, url_for, abort
from flask_login import login_required
from models import Participant, Assessment, ThoughtsAndBehaviours ,db
from datetime import datetime


assessments_bp = Blueprint('assessments', __name__, url_prefix="/participants/<string:participantId>/assessments")

@assessments_bp.route('/')
@login_required
def list_assessments(participantId):
    participant = db.session.get(Participant, participantId)
    if participant is None:
        abort(404)

    return render_template('assessments/list.html', assessments = participant.assessments, participantId = participantId)

@assessments_bp.route("/<int:assessmentId>/")
@login_required
def get_assessment(participantId, assessmentId):
    assessment = db.session.get(Assessment, assessmentId)
    if assessment.participant_id != participantId:
        abort(400)

    return render_template('assessments/details.html', assessment = assessment, participantId = participantId)


@assessments_bp.route('/add', methods=['GET','POST'])
@login_required
def add_assessment(participantId):
    participant = db.session.get(Participant, participantId)
    if participant is None:
        abort(404)

    if request.method=='POST':
        date_recorded_str = (request.form.get('date_recorded') or '').strip()
        try:
            try:
                if not date_recorded_str:
                    raise ValueError('Date Recorded is required.')
            
                date_recorded = datetime.strptime(date_recorded_str, '%Y-%m-%d').date()
            except ValueError:
                raise ValueError('Invalid date format. Please use YYYY-MM-DD')
       
            
            new_assessment = Assessment(participant_id=participantId, date_recorded=date_recorded)
            thoughts = ThoughtsAndBehaviours(
                bounce_back = request.form.get('bounce_back'),
                consequences = request.form.get('consequences'),
                working_hard = request.form.get('working_hard'),
                feel_good = request.form.get('feel_good'),
                adaptable = request.form.get('adaptable'),
                feelings = request.form.get('feelings'),
                emotional_problems = request.form.get('emotional_problems'),
                easy_to_talk = request.form.get('easy_to_talk'),
            )
            new_assessment.thoughts_and_behaviours = thoughts;

            db.session.add(new_assessment)
            db.session.commit()
            return redirect(url_for('assessments.list_assessments', participantId=participantId))
        except ValueError as e:
            error = str(e)
            return render_template('assessments/add.html', error=error) 



    return render_template('assessments/add.html', participantId = participant.id)