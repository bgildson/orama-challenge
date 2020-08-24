# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, request

from app.utils.computers import compute_freelance_skills
from .schemas import ComputeSkillsPayloadSchema, ComputeSkillsResultSchema


bp = Blueprint('freelancers', __name__, url_prefix='/api/freelancers')


@bp.route('/compute-skills', methods=['POST'])
def compute_skills():
    """
    Receives the freelancer professional experiences and returns the computation result
    """
    try:
        payload_schema = ComputeSkillsPayloadSchema()
        payload = payload_schema.load(request.get_json())

        computed = compute_freelance_skills(payload)

        result_schema = ComputeSkillsResultSchema()
        result = result_schema.load(computed)

        return jsonify(result)
    except Exception as _:
        return jsonify({'message': 'could not computate payload'}), 422
