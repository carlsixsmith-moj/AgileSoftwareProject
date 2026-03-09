import sys
import os
from datetime import date, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app
from models import db, Participant, Assessment

with app.app_context():
    db.create_all()
    print('Created database schema')

    if Participant.query.first() is None:
        participants = [
            Participant(id="1CFG1109X", name="Barry Stone"),
            Participant(id="1CFG1333S", name="Peter Allen"),
            Participant(id="1CFG1553F", name="VICTOR JORDAN"),
            Participant(id="1CFG1626P", name="BRUCE CURRY"),
            Participant(id="1CFG2457U", name="BRUCE WAYNE"),
            Participant(id="1CFG2622V", name="DINAH JORDAN"),
            Participant(id="1CFG2883L", name="OLIVER PRINCE"),
            Participant(id="1CFG4261Y", name="DIANA WAYNE"),
            Participant(id="1CFG4595K", name="CLARK KENT"),
            Participant(id="1CFG4867Q", name="OLIVER JORDAN"),
            Participant(id="1CFG4936J", name="VICTOR JORDAN"),
            Participant(id="1CFG5131C", name="BARRY ALLEN"),
            Participant(id="1CFG5298O", name="VICTOR JORDAN"),
            Participant(id="1CFG5437L", name="HAL PARKER"),
            Participant(id="1CFG5469L", name="PETER QUEEN"),
            Participant(id="1CFG5854G", name="DINAH QUEEN"),
            Participant(id="1CFG6059P", name="Oliver Kent"),
            Participant(id="1CFG6390M", name="ARTHUR LANCE"),
            Participant(id="1CFG7256O", name="BARRY PARKER"),
            Participant(id="1CFG7276C", name="OLIVER PRINCE"),
            Participant(id="1CFG8236D", name="BRUCE ALLEN"),
            Participant(id="1CFG8391O", name="HAL KENT"),
            Participant(id="1CFG8432I", name="HAL CURRY"),
            Participant(id="1CFG8516T", name="DINAH KENT"),
            Participant(id="1CFG9326Y", name="BRUCE KENT"),
            Participant(id="1CFG9475S", name="VICTOR JORDAN"),
            Participant(id="1CFG9798U", name="Hal Queen"),
            Participant(id="1CFG9960M", name="BRUCE LANCE")
        ]
        db.session.add_all(participants)
        db.session.commit()

        print("\nParticipants created")
        for p in participants:
            print(f"    [{p.id}] {p.name}")
    else:
        print("\nParticipants already exist, skipping participant seeding.")

    if Assessment.query.first() is None:
        participants = Participant.query.order_by(Participant.id).all()
        if not participants:
            print("\nNo participants available, cannot seed assessments.")
        else:
            start_date = date(2026, 1, 6)
            assessments = []

            # Create 2 assessments for the first 12 participants.
            for index, participant in enumerate(participants[:12]):
                first_date = start_date + timedelta(days=index * 7)
                second_date = first_date + timedelta(days=28)
                assessments.append(Assessment(participant=participant, date_recorded=first_date))
                assessments.append(Assessment(participant=participant, date_recorded=second_date))

            db.session.add_all(assessments)
            db.session.commit()

            print("\nAssessments created")
            for a in assessments:
                print(f"    [Assessment {a.id}] participant={a.participant_id}, date={a.date_recorded}")
    else:
        print("\nAssessments already exist, skipping assessment seeding.")