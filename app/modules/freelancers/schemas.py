# -*- coding: utf-8 -*-

from marshmallow import Schema, fields


class ComputeSkillsPayloadSchema(Schema):
    freelance = fields.Nested('FreelanceSchema')


class FreelanceSchema(Schema):
    id = fields.Integer(required=True)
    user = fields.Nested('UserSchema')
    status = fields.String(required=True)
    retribution = fields.Number(required=True)
    availability_date = fields.DateTime(data_key='availabilityDate', required=True)
    professional_experiences = fields.List(
        fields.Nested('ProfessionalExperienceSchema'),
        data_key='professionalExperiences',
    )


class UserSchema(Schema):
    first_name = fields.String(data_key='firstName', required=True)
    last_name = fields.String(data_key='lastName', required=True)
    job_title = fields.String(data_key='jobTitle', required=True)


class ProfessionalExperienceSchema(Schema):
    id = fields.Integer(required=True)
    company_name = fields.String(data_key='companyName', required=True)
    start_date = fields.DateTime(data_key='startDate', required=True)
    end_date = fields.DateTime(data_key='endDate', required=True)
    skills = fields.List(fields.Nested('SkillSchema'))


class SkillSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)


class ComputeSkillsResultSchema(Schema):
    freelance = fields.Nested('ComputedFreelanceSchema', required=True)


class ComputedFreelanceSchema(Schema):
    id = fields.Integer(required=True)
    computed_skills = fields.List(
        fields.Nested('ComputedSkillSchema'), attribute='computedSkills'
    )


class ComputedSkillSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    duration_in_months = fields.Integer(attribute='durationInMonths', required=True)
