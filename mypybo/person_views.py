from flask import Blueprint, render_template, request
from pybo import db
from pybo.models import Person, Car
from werkzeug.utils import redirect

bp = Blueprint('person', __name__, url_prefix="")

@bp.route('person_list')
def test() :
    
    person_list = db.session.query(Person).all()
    
    return render_template('person_list.html', person_list=person_list)

@bp.route('person_form')
def person_form() :
    
    return render_template('person_form.html')

@bp.route('add_person')
def add_person() :
    
    name = request.args.get('name')
    age = request.args.get('age')
    address = request.args.get('address')
    
    p1 = Person(name=name, age=age, address=address)
    db.session.add(p1)
    db.session.commit()
    
    return redirect('person_list')