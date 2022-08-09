from flask import Flask, jsonify,redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://john:password@localhost/gitag'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class GIOne(db.Model):

    __tablename__ = "gi_one"

    id = db.Column(db.Integer, primary_key=True)
    assoc_name = db.Column(db.String, index=True)
    address = db.Column(db.String)
    applicants_name = db.Column(db.String)
    statement_of_case = db.Column(db.String)
    applicant_sign = db.Column(db.String)
    type_of_goods = db.Column(db.String)
    specs = db.Column(db.String)
    gi_name = db.Column(db.String)
    desc = db.Column(db.String)
    prod_map = db.Column(db.String)
    proof_of_origin = db.Column(db.String)
    methods_of_production = db.Column(db.String)
    uniqueness = db.Column(db.String)
    inspection_body = db.Column(db.String)
    logo_url = db.Column(db.String)
    # application_status = db.Column(db.String)
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

db.create_all()

@app.route("/", methods=["GET","POST","DELETE","PATCH"])
def index():
    if request.method == "GET":
        # db.session.refresh()
        db_form = db.session.query(GIOne).first()

        return dict(db_form.as_dict())
    if request.method == "POST":
        data = request.form
        db_form = GIOne(assoc_name=data["assoc_name"],
        address=data["address"],
        applicants_name=data["applicants_name"],
        statement_of_case=data["statement_of_case"],
        applicant_sign=data["applicant_sign"],
        type_of_goods=data["type_of_goods"],
        specs=data["specs"],
        gi_name=data["gi_name"],
        desc=data["desc"],
        prod_map=data["prod_map"],
        proof_of_origin=data["proof_of_origin"],
        methods_of_production=data["methods_of_production"],
        uniqueness=data["uniqueness"],
        inspection_body=data["inspection_body"],
        logo_url=data["logo_url"])
        db.session.add(db_form)
        db.session.commit()
    return jsonify(db_form.as_dict())
if __name__ == '__main__':
    app.run(debug=True) 

