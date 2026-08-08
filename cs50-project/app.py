
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from cs50 import SQL
from flask import flash
import random

app = Flask(__name__)
app.secret_key = "your-secret-key"

db = SQL("sqlite:///campus.db")


@app.route("/add_attendance", methods=["GET", "POST"])
def add_attendance():

    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        subject_id = request.form.get("subject_id")
        date = request.form.get("date")
        status = request.form.get("status")

        if not subject_id:
            return "Select a subject"

        if not date:
            return "Select a date"

        if not status:
            return "Select status"

        db.execute("""
            INSERT INTO attendance
            (subject_id, date, status)
            VALUES (?, ?, ?)
        """,
        subject_id,
        date,
        status)

        flash("Attendance saved successfully!")
        return redirect(url_for("attendance"))

    subjects = db.execute("""
        SELECT *
        FROM subjects
        WHERE user_id = ?
    """, session["user_id"])

    return render_template(
        "add_attendance.html",
        subjects=subjects
    )


@app.route("/delete_attendance/<int:id>")
def delete_attendance(id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    db.execute("""
        DELETE FROM attendance
        WHERE id = ?
        AND subject_id IN (
            SELECT id
            FROM subjects
            WHERE user_id = ?
        )
    """, id, session["user_id"])

    return redirect(url_for("attendance"))


@app.route("/edit_attendance/<int:id>", methods=["GET", "POST"])
def edit_attendance(id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        subject_id = request.form.get("subject_id")
        date = request.form.get("date")
        status = request.form.get("status")

        db.execute("""
            UPDATE attendance
            SET subject_id = ?, date = ?, status = ?
            WHERE id = ?
            AND subject_id IN (
                SELECT id
                FROM subjects
                WHERE user_id = ?
            )
        """,
        subject_id,
        date,
        status,
        id,
        session["user_id"])

        return redirect(url_for("attendance"))

    attendance = db.execute("""
        SELECT *
        FROM attendance
        WHERE id = ?
    """, id)

    subjects = db.execute("""
        SELECT *
        FROM subjects
        WHERE user_id = ?
    """, session["user_id"])

    return render_template(
        "edit_attendance.html",
        attendance=attendance[0],
        subjects=subjects
    )


@app.route("/attendance")
def attendance():

    if "user_id" not in session:
        return redirect(url_for("login"))

    attendance = db.execute("""
        SELECT attendance.*,
               subjects.subject_name
        FROM attendance
        JOIN subjects
        ON attendance.subject_id = subjects.id
        WHERE subjects.user_id = ?
        ORDER BY date DESC
    """, session["user_id"])

    return render_template(
        "attendance.html",
        attendance=attendance
    )


@app.route("/add_timetable", methods=["GET", "POST"])
def add_timetable():

    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        subject = request.form.get("subject")
        day = request.form.get("day")
        start_time = request.form.get("start_time")
        end_time = request.form.get("end_time")

        if not subject:
            return "Subject is required"

        if not day:
            return "Day is required"

        if not start_time:
            return "Start time is required"

        if not end_time:
            return "End time is required"

        db.execute("""
            INSERT INTO timetable
            (user_id, subject, day, start_time, end_time)
            VALUES (?, ?, ?, ?, ?)
        """,
        session["user_id"],
        subject,
        day,
        start_time,
        end_time)

        flash("Class added successfully!")
        return redirect(url_for("timetable"))

    subjects = db.execute("""
        SELECT subject_name
        FROM subjects
        WHERE user_id = ?
    """, session["user_id"])

    return render_template(
        "add_timetable.html",
        subjects=subjects
    )



@app.route("/timetable")
def timetable():

    if "user_id" not in session:
        return redirect(url_for("login"))

    schedule = db.execute("""
        SELECT *
        FROM timetable
        WHERE user_id = ?
        ORDER BY day, start_time
    """, session["user_id"])

    return render_template(
        "timetable.html",
        schedule=schedule
    )


@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("login"))

    subjects = db.execute(
        "SELECT COUNT(*) AS total FROM subjects WHERE user_id = ?",
        session["user_id"]
    )

    notes = db.execute("""
        SELECT COUNT(*) AS total
        FROM notes
        JOIN subjects
        ON notes.subject_id = subjects.id
        WHERE subjects.user_id = ?
    """, session["user_id"])

    assignments = db.execute("""
        SELECT COUNT(*) AS total
        FROM assignments
        JOIN subjects
        ON assignments.subject_id = subjects.id
        WHERE subjects.user_id = ?
    """, session["user_id"])

    pending = db.execute("""
        SELECT COUNT(*) AS total
        FROM assignments
        JOIN subjects
        ON assignments.subject_id = subjects.id
        WHERE subjects.user_id = ?
        AND assignments.status = 'Pending'
    """, session["user_id"])


    return render_template(
        "dashboard.html",
        subjects=subjects[0]["total"],
        notes=notes[0]["total"],
        assignments=assignments[0]["total"],
        pending=pending[0]["total"]
    )


@app.route("/edit_timetable/<int:id>", methods=["GET", "POST"])
def edit_timetable(id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        subject = request.form.get("subject")
        day = request.form.get("day")
        start_time = request.form.get("start_time")
        end_time = request.form.get("end_time")

        db.execute("""
            UPDATE timetable
            SET subject = ?,
                day = ?,
                start_time = ?,
                end_time = ?
            WHERE id = ? AND user_id = ?
        """,
        subject,
        day,
        start_time,
        end_time,
        id,
        session["user_id"])

        return redirect(url_for("timetable"))

    row = db.execute("""
        SELECT *
        FROM timetable
        WHERE id = ? AND user_id = ?
    """,
    id,
    session["user_id"])

    subjects = db.execute("""
        SELECT subject_name
        FROM subjects
        WHERE user_id = ?
    """, session["user_id"])

    return render_template(
        "edit_timetable.html",
        row=row[0],
        subjects=subjects
    )



@app.route("/delete_timetable/<int:id>")
def delete_timetable(id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    db.execute("""
        DELETE FROM timetable
        WHERE id = ? AND user_id = ?
    """,
    id,
    session["user_id"])

    return redirect(url_for("timetable"))


@app.route("/assignments")
def assignments():

    if "user_id" not in session:
        return redirect(url_for("login"))

    search = request.args.get("search")

    if search:

        assignments = db.execute("""
            SELECT assignments.*, subjects.subject_name
            FROM assignments
            JOIN subjects
            ON assignments.subject_id = subjects.id
            WHERE subjects.user_id = ?
            AND title LIKE ?
            ORDER BY due_date
        """,
        session["user_id"],
        "%" + search + "%")

    else:

        assignments = db.execute("""
            SELECT assignments.*, subjects.subject_name
            FROM assignments
            JOIN subjects
            ON assignments.subject_id = subjects.id
            WHERE subjects.user_id = ?
            ORDER BY due_date
        """,
        session["user_id"])

    return render_template(
        "assignments.html",
        assignments=assignments
    )


@app.route("/edit_assignment/<int:id>", methods=["GET", "POST"])
def edit_assignment(id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        subject_id = request.form.get("subject_id")
        title = request.form.get("title")
        due_date = request.form.get("due_date")
        status = request.form.get("status")

        db.execute("""
            UPDATE assignments
            SET subject_id = ?,
                title = ?,
                due_date = ?,
                status = ?
            WHERE id = ?
            AND subject_id IN (
                SELECT id
                FROM subjects
                WHERE user_id = ?
            )
        """,
        subject_id,
        title,
        due_date,
        status,
        id,
        session["user_id"])

        return redirect(url_for("assignments"))

    assignment = db.execute("""
        SELECT *
        FROM assignments
        WHERE id = ?
    """, id)

    subjects = db.execute("""
        SELECT *
        FROM subjects
        WHERE user_id = ?
    """, session["user_id"])

    return render_template(
        "edit_assignment.html",
        assignment=assignment[0],
        subjects=subjects
    )


@app.route("/delete_assignment/<int:id>")
def delete_assignment(id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    db.execute("""
        DELETE FROM assignments
        WHERE id = ?
        AND subject_id IN (
            SELECT id
            FROM subjects
            WHERE user_id = ?
        )
    """, id, session["user_id"])

    return redirect(url_for("assignments"))




@app.route("/add_assignment", methods=["GET", "POST"])
def add_assignment():

    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        subject_id = request.form.get("subject_id")
        title = request.form.get("title")
        due_date = request.form.get("due_date")

        if not subject_id:
            return "Select a subject"

        if not title:
            return "Title is required"

        if not due_date:
            return "Due date is required"

        db.execute("""
            INSERT INTO assignments
            (subject_id, title, due_date)
            VALUES (?, ?, ?)
        """, subject_id, title, due_date)

        flash("Assignment added successfully!")
        return redirect(url_for("assignments"))

    subjects = db.execute("""
        SELECT *
        FROM subjects
        WHERE user_id = ?
    """, session["user_id"])

    return render_template(
        "add_assignment.html",
        subjects=subjects
    )

@app.route("/complete_assignment/<int:id>")
def complete_assignment(id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    db.execute("""
        UPDATE assignments
        SET status = 'Completed'
        WHERE id = ?
    """, id)

    return redirect(url_for("assignments"))


@app.route("/subjects")
def subjects():

    if "user_id" not in session:
        return redirect(url_for("login"))

    search = request.args.get("search")

    if search:

        subjects = db.execute("""
            SELECT *
            FROM subjects
            WHERE user_id = ?
            AND subject_name LIKE ?
            ORDER BY subject_name
        """,
        session["user_id"],
        "%" + search + "%")

    else:

        subjects = db.execute("""
            SELECT *
            FROM subjects
            WHERE user_id = ?
            ORDER BY subject_name
        """,
        session["user_id"])

    return render_template(
        "subjects.html",
        subjects=subjects
    )


@app.route("/edit_subject/<int:id>", methods=["GET", "POST"])
def edit_subject(id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        subject_name = request.form.get("subject_name")

        db.execute(
            "UPDATE subjects SET subject_name = ? WHERE id = ? AND user_id = ?",
            subject_name,
            id,
            session["user_id"]
        )

        return redirect(url_for("subjects"))

    subject = db.execute(
        "SELECT * FROM subjects WHERE id = ? AND user_id = ?",
        id,
        session["user_id"]
    )

    return render_template("edit_subject.html", subject=subject[0])



@app.route("/delete_subject/<int:id>")
def delete_subject(id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    db.execute(
        "DELETE FROM subjects WHERE id = ? AND user_id = ?",
        id,
        session["user_id"]
    )

    return redirect(url_for("subjects"))

@app.route("/add_subject", methods=["GET", "POST"])
def add_subject():

    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        subject_name = request.form.get("subject_name")

        if not subject_name:
            return "Subject name is required"

        db.execute(
            "INSERT INTO subjects (user_id, subject_name) VALUES (?, ?)",
            session["user_id"],
            subject_name
        )

        flash("Subject added successfully!")
        return redirect(url_for("subjects"))

    return render_template("add_subject.html")

@app.route("/")
def index():

    quotes = [
        "Study smarter, stay organized, achieve more.",
        "Small progress every day leads to big success.",
        "Your future is created by what you do today.",
        "Consistency beats motivation.",
        "Every assignment completed is one step closer to your goals."
    ]

    quote = random.choice(quotes)

    return render_template("index.html", quote=quote)


@app.route("/notes")
def notes():

    if "user_id" not in session:
        return redirect(url_for("login"))

    search = request.args.get("search")

    if search:

        notes = db.execute("""
            SELECT notes.*, subjects.subject_name
            FROM notes
            JOIN subjects
            ON notes.subject_id = subjects.id
            WHERE subjects.user_id = ?
            AND title LIKE ?
            ORDER BY notes.id DESC
        """,
        session["user_id"],
        "%" + search + "%")

    else:

        notes = db.execute("""
            SELECT notes.*, subjects.subject_name
            FROM notes
            JOIN subjects
            ON notes.subject_id = subjects.id
            WHERE subjects.user_id = ?
            ORDER BY notes.id DESC
        """,
        session["user_id"])

    return render_template("notes.html", notes=notes)

@app.route("/add_note", methods=["GET", "POST"])
def add_note():

    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        subject_id = request.form.get("subject_id")
        title = request.form.get("title")
        content = request.form.get("content")

        if not subject_id:
            return "Select a subject"

        if not title:
            return "Title is required"

        if not content:
            return "Content is required"

        db.execute(
            "INSERT INTO notes (subject_id, title, content) VALUES (?, ?, ?)",
            subject_id,
            title,
            content
        )

        flash("Note added successfully!")
        return redirect(url_for("notes"))

    subjects = db.execute(
        "SELECT * FROM subjects WHERE user_id = ?",
        session["user_id"]
    )

    return render_template("add_note.html", subjects=subjects)

@app.route("/note/<int:id>")
def note(id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    rows = db.execute("""
        SELECT notes.*,
               subjects.subject_name
        FROM notes
        JOIN subjects
        ON notes.subject_id = subjects.id
        WHERE notes.id = ? AND subjects.user_id = ?
    """, id, session["user_id"])

    if len(rows) != 1:
        return "Note not found"

    return render_template("note.html", note=rows[0])


@app.route("/edit_note/<int:id>", methods=["GET", "POST"])
def edit_note(id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        subject_id = request.form.get("subject_id")
        title = request.form.get("title")
        content = request.form.get("content")

        db.execute("""
            UPDATE notes
            SET subject_id = ?, title = ?, content = ?
            WHERE id = ?
        """, subject_id, title, content, id)

        return redirect(url_for("notes"))

    note = db.execute("""
        SELECT * FROM notes
        WHERE id = ?
    """, id)

    subjects = db.execute("""
        SELECT * FROM subjects
        WHERE user_id = ?
    """, session["user_id"])

    return render_template(
        "edit_note.html",
        note=note[0],
        subjects=subjects
    )


@app.route("/delete_note/<int:id>")
def delete_note(id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    db.execute("""
        DELETE FROM notes
        WHERE id = ?
    """, id)

    return redirect(url_for("notes"))




@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if not username:
            return "Username is required"

        if not password:
            return "Password is required"

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?",
            username
        )

        if len(rows) != 1:
            return "Invalid username"

        user = rows[0]

        if not check_password_hash(user["hash"], password):
            return "Invalid password"

        session["user_id"] = user["id"]

        flash("Welcome back!")
        return redirect(url_for("dashboard"))

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Validation
        if not username:
            return "Username is required"

        if not password:
            return "Password is required"

        if password != confirmation:
            return "Passwords do not match"

        # Check if username already exists
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?",
            username
        )

        if len(rows) != 0:
            return "Username already exists"

        # Hash password
        hash = generate_password_hash(password)

        # Insert user
        db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)",
            username,
            hash
        )

        flash("Registration successful!")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))



if __name__ == "__main__":
    app.run(debug=True)
