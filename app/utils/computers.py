# -*- coding: utf-8 -*-

from typing import Any, Dict

from dateutil.relativedelta import relativedelta
from datetime import datetime


def compute_freelance_skills(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Receives the freelance payload and count the months experience with every skill
    """
    result = {
        'freelance': {
            'id': payload['freelance']['id'],
            'computed_skills': []
        }
    }

    skills = {}
    for professional_experience in payload['freelance']['professional_experiences']:
        for skill in professional_experience['skills']:
            if skill['id'] not in skills:
                skills[skill['id']] = {
                    'id': skill['id'],
                    'name': skill['name'],
                    'months': {}
                }

            current: datetime = professional_experience['start_date']
            last: datetime = professional_experience['end_date']
            last = last.replace(day=1)
            while current <= last:
                year_month = current.strftime('%Y%m')
                skills[skill['id']]['months'][year_month] = None
                current += relativedelta(months=1)

    for skill in skills.values():
        computed_skill = {
            'id': skill['id'],
            'name': skill['name'],
            'duration_in_months': len(skill['months'])
        }
        result['freelance']['computed_skills'].append(computed_skill)

    return result
