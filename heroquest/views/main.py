from flask import Blueprint, redirect, render_template, request, flash, url_for
from flask_login import current_user, login_required

from .. import db
from ..models.hero import Hero, HeroClass

main = Blueprint("main", __name__)


@main.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for("main.heroes"))
    
    return redirect(url_for("auth.login"))


@main.route("/create-hero", methods=["GET", "POST"])
@login_required
def create_hero():
    if request.method == "POST":
        hero_name = request.form["hero-name"]
        hero_class = request.form["hero-class"]

        if hero_class == "barbarian":
            hero = Hero(name=hero_name, hero_class=HeroClass.BARBARIAN, body=8, mind=2, attack=3, defend=2, movement=2)  # pyright: ignore
        elif hero_class == "dwarf":
            hero = Hero(name=hero_name, hero_class=HeroClass.DWARF, body=7, mind=3, attack=2, defend=2, movement=2)  # pyright: ignore
        elif hero_class == "elf":
            hero = Hero(name=hero_name, hero_class=HeroClass.ELF, body=6, mind=4, attack=2, defend=2, movement=2)  # pyright: ignore
        elif hero_class == "wizard":
            hero = Hero(name=hero_name, hero_class=HeroClass.WIZARD, body=4, mind=6, attack=1, defend=2, movement=2)  # pyright: ignore
        else:
            flash("Invalid hero class", "danger")
            return redirect(url_for("game.create_hero"))

        db.session.add(hero)
        db.session.commit()
        flash("Hero creation sucsessful", "success")

        return redirect(url_for("main.hero", hero_id=hero.id))

    return render_template("main/create_hero.html")


@main.route("/heroes")
@login_required
def heroes():
    heroes = Hero.query.all()
    return render_template("main/heroes.html", heroes=heroes)


@main.route("/hero/<int:hero_id>")
@login_required
def hero(hero_id):
    hero = Hero.query.get(hero_id)
    if not hero:
        flash("Hero not found", "danger")
        return redirect(url_for("main.heroes"))

    return render_template("main/hero.html", hero=hero)
