# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, request

from app.utils.computers import compute_freelance_skills
from .schemas import ComputeSkillsPayloadSchema, ComputeSkillsResultSchema


bp = Blueprint('freelancers', __name__, url_prefix='/api/freelancers')
payload_schema = ComputeSkillsPayloadSchema()
result_schema = ComputeSkillsResultSchema()


@bp.route('/compute-skills', methods=['POST'])
def compute_skills():
    """
    Receives the freelancer professional experiences and returns the computation result
    """
    try:
        errors = payload_schema.validate(request.get_json())
        if errors:
            return jsonify(errors='could not compute payload'), 422

        payload = payload_schema.load(request.get_json())

        computed = compute_freelance_skills(payload)

        result = result_schema.load(computed)

        return jsonify(result)
    except Exception:
        return jsonify(error='an unexpected error occurred, try again later'), 500
