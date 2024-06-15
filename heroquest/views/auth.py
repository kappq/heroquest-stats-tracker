from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from .. import db
from ..models.user import User

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        remember = request.form.get("remember")

        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):  # pyright: ignore
            flash("Invalid email or password", "error")
            return redirect(url_for("auth.login"))

        login_user(user, remember=bool(remember))
        flash("Login successful", "success")

        return redirect(url_for("main.heroes"))

    return render_template("auth/login.html")


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already used", "error")
            return redirect(url_for("auth.signup"))

        user = User.query.filter_by(username=username).first()
        if user:
            flash("Username already used", "error")
            return redirect(url_for("auth.signup"))

        password_hash = generate_password_hash(password)  # pyright: ignore
        new_user = User(email=email, username=username, password=password_hash)  # pyright: ignore

        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful", "success")

        return redirect(url_for("auth.login"))

    return render_template("auth/signup.html")


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Log out successful", "success")

    return redirect(url_for("main.index"))
