from marshmallow import Schema, fields, validate


class ContractSchema(Schema):
    id = fields.UUID(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(3))
    rules = fields.Nested('RuleSchema', many=True, exclude=('contract',))
    information = fields.String(validate=validate.Length(1))


class RuleSchema(Schema):
    id = fields.UUID(dump_only=True)
    rule_name = fields.String(required=True, validate=validate.Length(1))
    contract = fields.Nested('ContractSchema', exclude=('rules',))
    f_operand = fields.String(validate=validate.Length(1))
    s_operand = fields.String(validate=validate.Length(1))
    operator = fields.String(validate=validate.Length(1))
    coefficient = fields.Float(validate=validate.Length(1))
    page = fields.Integer(validate=validate.Length(1))


contract_schema = ContractSchema()
rule_schema = RuleSchema()
