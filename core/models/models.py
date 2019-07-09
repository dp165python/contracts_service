from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

db = SQLAlchemy()


class AddUpdateDelete():
    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def update(self):
        return db.session.commit()

    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()


class Rule(db.Model, AddUpdateDelete):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    rule_name = db.Column(db.String(250), unique=True, nullable=False)
    contract_id = db.Column(UUID(as_uuid=True), db.ForeignKey('contract.id'), nullable=False)
    contract = db.relationship('Contract', backref=db.backref('rules', lazy='dynamic' , order_by='Rule.rule_name'))
    f_operand = db.Column(db.String(250), nullable=False)
    s_operand = db.Column(db.String(250), nullable=False)
    operator = db.Column(db.String(2), nullable=False)
    coefficient = db.Column(db.String(250), nullable=False)

    def __init__(self, rule_name, contract, f_operand, s_operand, operator, coefficient):
        self.rule_name = rule_name
        self.contract = contract
        self.f_operand = f_operand
        self.s_operand = s_operand
        self.operator = operator
        self.coefficient = coefficient


class Contract(db.Model, AddUpdateDelete):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = db.Column(db.String(150), unique=True, nullable=False)
    information = db.Column(db.String(250))

    def __init__(self, name, information):
        self.name = name
        self.information = information
