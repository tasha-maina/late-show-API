from flask import request
from flask_restful import Resource
from models import db, Episode, Guest, Appearance

class Episodes(Resource):
    def get(self):
        episodes = Episode.query.all()
        return [e.to_dict() for e in episodes], 200


class EpisodeById(Resource):
    def get(self, id):
        episode = Episode.query.get(id)
        if not episode:
            return {"error": "Episode not found"}, 404
        return episode.to_dict(rules=("-appearances.episode",)), 200

    def delete(self, id):
        episode = Episode.query.get(id)
        if not episode:
            return {"error": "Episode not found"}, 404

        db.session.delete(episode)
        db.session.commit()
        return {}, 204


class Guests(Resource):
    def get(self):
        guests = Guest.query.all()
        return [g.to_dict() for g in guests], 200


class Appearances(Resource):
    def post(self):
        data = request.get_json()

        try:
            appearance = Appearance(
                rating=data["rating"],
                episode_id=data["episode_id"],
                guest_id=data["guest_id"]
            )
            db.session.add(appearance)
            db.session.commit()
            return appearance.to_dict(), 201

        except Exception as e:
            return {"errors": ["validation errors"]}, 400
