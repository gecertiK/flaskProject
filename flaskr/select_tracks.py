from flask import Blueprint, render_template

from flaskr.db import get_db

bp = Blueprint('select_tracks', __name__)


@bp.route('/names/')
def names():
    db = get_db()
    count = db.execute('SELECT COUNT ( DISTINCT artist ) AS Quantity FROM tracks;').fetchone()
    return render_template('names.html', count=count)


@bp.route('/tracks/')
def tracks():
    db = get_db()
    count = db.execute('SELECT COUNT ( id ) AS "Quantity" FROM tracks;').fetchone()
    return render_template('tracks.html', count=count)


@bp.route('/tracks/<genre>/')
def genres(genre):
    genre = genre.lower()
    db = get_db()
    count = db.execute('SELECT COUNT (id) AS "Quantity" FROM tracks WHERE genre = ?;', (genre,)).fetchone()
    return render_template('genre.html', count=count, genre=genre)


@bp.route('/tracks-sec/')
def tracks_sec():
    db = get_db()
    tracks_sec = db.execute('SELECT title, seconds FROM tracks;').fetchall()
    return render_template('tracks_sec.html', tracks_sec=tracks_sec)


@bp.route('/tracks-sec/statistics/')
def tracks_sec_statistics():
    db = get_db()
    sum_avg_tracks = db.execute(
        'SELECT SUM(seconds) AS "total", AVG(seconds) AS "Average" FROM tracks;').fetchone()
    return render_template('sum_avg_tracks.html', sum_avg_tracks=sum_avg_tracks)
