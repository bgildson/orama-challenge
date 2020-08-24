# -*- config: utf-8 -*-

import pytest


@pytest.fixture(scope='session')
def freelance_compute_skills_payload():
    return {
        'freelance': {
            'id': 42,
            'user': {
                'firstName': 'Hunter',
                'lastName': 'Moore',
                'jobTitle': 'Fullstack JS Developer',
            },
            'status': 'new',
            'retribution': 650,
            'availabilityDate': '2018-06-13T00:00:00+01:00',
            'professionalExperiences': [
                {
                    'id': 4,
                    'companyName': 'Okuneva, Kerluke and Strosin',
                    'startDate': '2016-01-01T00:00:00+01:00',
                    'endDate': '2018-05-01T00:00:00+01:00',
                    'skills': [
                        {'id': 241, 'name': 'React'},
                        {'id': 270, 'name': 'Node.js'},
                        {'id': 370, 'name': 'Javascript'},
                    ],
                },
                {
                    'id': 54,
                    'companyName': 'Hayes - Veum',
                    'startDate': '2014-01-01T00:00:00+01:00',
                    'endDate': '2016-09-01T00:00:00+01:00',
                    'skills': [
                        {'id': 470, 'name': 'MySQL'},
                        {'id': 400, 'name': 'Java'},
                        {'id': 370, 'name': 'Javascript'},
                    ],
                },
                {
                    'id': 80,
                    'companyName': 'Harber, Kirlin and Thompson',
                    'startDate': '2013-05-01T00:00:00+01:00',
                    'endDate': '2014-07-01T00:00:00+01:00',
                    'skills': [
                        {'id': 370, 'name': 'Javascript'},
                        {'id': 400, 'name': 'Java'},
                    ],
                },
            ],
        }
    }


@pytest.fixture(scope='session')
def freelance_compute_skills_result():
    return {
        'freelance': {
            'id': 42,
            'computedSkills': [
                {'id': 241, 'name': 'React', 'durationInMonths': 28},
                {'id': 270, 'name': 'Node.js', 'durationInMonths': 28},
                {'id': 370, 'name': 'Javascript', 'durationInMonths': 60},
                {'id': 470, 'name': 'MySQL', 'durationInMonths': 32},
                {'id': 400, 'name': 'Java', 'durationInMonths': 40},
            ],
        }
    }
