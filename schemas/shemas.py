from marshmallow import Schema, fields, pre_load
from marshmallow import validate
from flask_marshmallow import Marshmallow

ma = Marshmallow()


class RuleSchema(ma.Schema):
    id = fields.UUID(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(3))
    url = ma.URLFor('api.ruleresource', id='<id>', _external=True)
    contracts = fields.Nested('ContractSchema', many=True, exclude=('rule',))
    creation_date = fields.DateTime()
    f_operand = fields.String(validate=validate.Length(1))
    s_operand = fields.String(validate=validate.Length(1))
    operator = fields.String(validate=validate.Length(1))
    coefficient = fields.String(validate=validate.Length(1))


class ContractSchema(ma.Schema):
    id = fields.UUID(dump_only=True)
    contract_name = fields.String(required=True, validate=validate.Length(1))
    creation_date = fields.DateTime()
    rule = fields.Nested('RuleSchema', exclude=('contracts',))
    url = ma.URLFor('api.contractresource', id='<id>', _external=True)
    information = fields.String(validate=validate.Length(1))

    @pre_load
    def process_rule(self, data):
        rule = data.get('rule')
        if rule:
            if isinstance(rule, dict):
                rule_name = rule.get('name')
            else:
                rule_name = rule
            rule_dict = dict(name=rule_name)
        else:
            rule_dict = {}
        data['rule'] = rule_dict
        return data
