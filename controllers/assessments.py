from flask import Blueprint, render_template, request, redirect, url_for, abort
from models import Participant, Assessment, db

assessments_bp = Blueprint('assessments', __name__, url_prefix="/participants/<string:participantId>/assessments")

@assessments_bp.route('/')
def list_assessments(participantId):
    participant = db.session.get(Participant, participantId)
    if participant is None:
        abort(404)

    return render_template('assessments/list.html', assessments = participant.assessments, participantId = participantId)

@assessments_bp.route('/add')
def add_assessment(participantId):
    participant = db.session.get(Participant, participantId)
    if participant is None:
        abort(404)
    return render_template('assessments/add.html', participantId = participant.id)