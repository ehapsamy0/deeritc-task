from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    phone = fields.Str(required=False)
    email = fields.Email(required=True)

