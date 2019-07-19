from uuid import uuid4

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID

db = SQLAlchemy()


class Contract(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = db.Column(db.String(150), unique=True, nullable=False)
    information = db.Column(db.String(250))


class Rule(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    rule_name = db.Column(db.String(250), unique=True, nullable=False)
    contract_id = db.Column(UUID(as_uuid=True), db.ForeignKey('contract.id'), nullable=False)
    contract = db.relationship('Contract', backref=db.backref('rules', lazy='dynamic', order_by='Rule.rule_name'))
    f_operand = db.Column(db.String(250), nullable=False)
    s_operand = db.Column(db.String(250), nullable=False)
    operator = db.Column(db.String(2), nullable=False)
    coefficient = db.Column(db.String(250), nullable=False)
