from marshmallow import Schema, fields, pre_load, validate


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
    coefficient = fields.String(validate=validate.Length(1))

    @pre_load
    def process_contract(self, data):
        contract = data.get('contract')
        if contract:
            if isinstance(contract, dict):
                contract_name = contract.get('name')
            else:
                contract_name = contract
            contract_dict = dict(name=contract_name)
        else:
            contract_dict = {}
        data['contract'] = contract_dict
        return data
