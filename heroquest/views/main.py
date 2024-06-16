from flask import Blueprint, redirect, render_template, request, flash, url_for, jsonify
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
            hero = Hero(owner=current_user.id, name=hero_name, hero_class=HeroClass.BARBARIAN, body=8, mind=2, attack=3, defend=2, movement=2)  # pyright: ignore
        elif hero_class == "dwarf":
            hero = Hero(owner=current_user.id, name=hero_name, hero_class=HeroClass.DWARF, body=7, mind=3, attack=2, defend=2, movement=2)  # pyright: ignore
        elif hero_class == "elf":
            hero = Hero(owner=current_user.id, name=hero_name, hero_class=HeroClass.ELF, body=6, mind=4, attack=2, defend=2, movement=2)  # pyright: ignore
        elif hero_class == "wizard":
            hero = Hero(owner=current_user.id, name=hero_name, hero_class=HeroClass.WIZARD, body=4, mind=6, attack=1, defend=2, movement=2)  # pyright: ignore
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
    return render_template("main/heroes.html", heroes=current_user.heroes)


@main.route("/hero/<int:hero_id>")
@login_required
def hero(hero_id):
    hero = Hero.query.get(hero_id)
    if not hero or hero.owner != current_user.id:
        flash("Hero not found", "danger")
        return redirect(url_for("main.heroes"))

    return render_template("main/hero.html", hero=hero)


@main.route("/update-hero/<int:hero_id>", methods=["POST"])
@login_required
def update_hero(hero_id):
    hero = Hero.query.get(hero_id)
    if not hero or hero.owner != current_user.id:
        flash("Hero not found", "danger")
        return jsonify({"error": "Hero not found"})

    stat = request.json["stat"]
    value = request.json["value"]
    if not stat or not value:
        return jsonify({"error": "`stat` or `value` missing"})

    if stat == "body":
        hero.body += value
    elif stat == "mind":
        hero.mind += value
    elif stat == "attack":
        hero.attack += value
    elif stat == "defend":
        hero.defend += value
    elif stat == "movement":
        hero.movement += value

    db.session.commit()

    return jsonify({"success": "Hero updated successfully"})
