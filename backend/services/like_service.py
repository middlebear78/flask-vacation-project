from backend.extensions import db
from backend.models.db_models import Like, Vacation


def add_like(user_id, vacation_id):
    like = Like(user_id=user_id, vacation_id=vacation_id)
    db.session.add(like)

    vacation = db.session.get(Vacation, vacation_id)
    if vacation:
        vacation.likes = (vacation.likes or 0) + 1

    db.session.commit()

    count = Like.query.filter_by(vacation_id=vacation_id).count()
    return count


def remove_like(user_id, vacation_id):
    like = Like.query.filter_by(user_id=user_id, vacation_id=vacation_id).first()
    if like:
        db.session.delete(like)

        vacation = db.session.get(Vacation, vacation_id)
        if vacation:
            vacation.likes = max((vacation.likes or 0) - 1, 0)

        db.session.commit()

    count = Like.query.filter_by(vacation_id=vacation_id).count()
    return count


def get_user_liked_vacation_ids(user_id):
    likes = Like.query.filter_by(user_id=user_id).all()
    return [like.vacation_id for like in likes]
