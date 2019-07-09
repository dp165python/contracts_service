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


class Contract(db.Model, AddUpdateDelete):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    contract_name = db.Column(db.String(250), unique=True, nullable=False)
    information = db.Column(db.String(250))
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    rule_id = db.Column(UUID(as_uuid=True), db.ForeignKey('rule.id'), nullable=False)
    rule = db.relationship('Rule', backref=db.backref('contracts', lazy='dynamic' , order_by='Contract.contract_name'))

    def __init__(self, contract_name, information, rule):
        self.contract_name = contract_name
        self.information = information
        self.rule = rule


class Rule(db.Model, AddUpdateDelete):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = db.Column(db.String(150), unique=True, nullable=False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    f_operand = db.Column(db.String(250), nullable=False)
    s_operand = db.Column(db.String(250), nullable=False)
    operator = db.Column(db.String(2), nullable=False)
    coefficient = db.Column(db.String(250), nullable=False)

    def __init__(self, name, f_operand, s_operand, operator, coefficient):
        self.name = name
        self.f_operand = f_operand
        self.s_operand = s_operand
        self.operator = operator
        self.coefficient = coefficient

