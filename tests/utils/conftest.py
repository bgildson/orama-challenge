# -*- config: utf-8 -*-

from datetime import datetime
import pytest


@pytest.fixture(scope='session')
def freelance_one_experience():
    return {
        'freelance': {
            'id': 42,
            'user': {
                'first_name': 'Hunter',
                'last_name': 'Moore',
                'job_title': 'Fullstack JS Developer',
            },
            'status': 'new',
            'retribution': 650,
            'availability_date': datetime(2018, 6, 13),
            'professional_experiences': [
                {
                    'id': 4,
                    'company_name': 'Okuneva, Kerluke and Strosin',
                    'start_date': datetime(2016, 1, 1),
                    'end_date': datetime(2018, 5, 1),
                    'skills': [{'id': 370, 'name': 'Javascript'},],
                },
            ],
        }
    }


@pytest.fixture(scope='session')
def freelance_one_experience_computed():
    return {
        'freelance': {
            'id': 42,
            'computed_skills': [
                {'id': 370, 'name': 'Javascript', 'duration_in_months': 29}
            ],
        }
    }


@pytest.fixture(scope='session')
def freelance_two_experiences_with_same_skill_in_continuous_time():
    return {
        'freelance': {
            'id': 42,
            'user': {
                'first_name': 'Hunter',
                'last_name': 'Moore',
                'job_title': 'Fullstack JS Developer',
            },
            'status': 'new',
            'retribution': 650,
            'availability_date': datetime(2018, 6, 13),
            'professional_experiences': [
                {
                    'id': 54,
                    'company_name': 'Hayes - Veum',
                    'start_date': datetime(2014, 1, 1),
                    'end_date': datetime(2016, 9, 1),
                    'skills': [{'id': 370, 'name': 'Javascript'}],
                },
                {
                    'id': 80,
                    'company_name': 'Harber, Kirlin and Thompson',
                    'start_date': datetime(2016, 10, 1),
                    'end_date': datetime(2018, 6, 1),
                    'skills': [{'id': 370, 'name': 'Javascript'},],
                },
            ],
        }
    }


@pytest.fixture(scope='session')
def freelance_two_experiences_with_same_skill_in_continuous_time_computed():
    return {
        'freelance': {
            'id': 42,
            'computed_skills': [
                {'id': 370, 'name': 'Javascript', 'duration_in_months': 54}
            ],
        }
    }


@pytest.fixture(scope='session')
def freelance_two_experiences_with_same_skill_with_interval_between():
    return {
        'freelance': {
            'id': 42,
            'user': {
                'first_name': 'Hunter',
                'last_name': 'Moore',
                'job_title': 'Fullstack JS Developer',
            },
            'status': 'new',
            'retribution': 650,
            'availability_date': datetime(2018, 6, 13),
            'professional_experiences': [
                {
                    'id': 54,
                    'company_name': 'Hayes - Veum',
                    'start_date': datetime(2014, 1, 1),
                    'end_date': datetime(2016, 1, 1),
                    'skills': [{'id': 370, 'name': 'Javascript'}],
                },
                {
                    'id': 80,
                    'company_name': 'Harber, Kirlin and Thompson',
                    'start_date': datetime(2016, 10, 1),
                    'end_date': datetime(2018, 6, 1),
                    'skills': [{'id': 370, 'name': 'Javascript'},],
                },
            ],
        }
    }


@pytest.fixture(scope='session')
def freelance_two_experiences_with_same_skill_with_interval_between_computed():
    return {
        'freelance': {
            'id': 42,
            'computed_skills': [
                {'id': 370, 'name': 'Javascript', 'duration_in_months': 46}
            ],
        }
    }


@pytest.fixture(scope='session')
def freelance_two_experiences_with_same_skill_in_converge_time():
    return {
        'freelance': {
            'id': 42,
            'user': {
                'first_name': 'Hunter',
                'last_name': 'Moore',
                'job_title': 'Fullstack JS Developer',
            },
            'status': 'new',
            'retribution': 650,
            'availability_date': datetime(2018, 6, 13),
            'professional_experiences': [
                {
                    'id': 54,
                    'company_name': 'Hayes - Veum',
                    'start_date': datetime(2014, 1, 1),
                    'end_date': datetime(2016, 9, 1),
                    'skills': [{'id': 370, 'name': 'Javascript'}],
                },
                {
                    'id': 80,
                    'company_name': 'Harber, Kirlin and Thompson',
                    'start_date': datetime(2016, 1, 1),
                    'end_date': datetime(2018, 6, 1),
                    'skills': [{'id': 370, 'name': 'Javascript'},],
                },
            ],
        }
    }


@pytest.fixture(scope='session')
def freelance_two_experiences_with_same_skill_in_converge_time_computed():
    return {
        'freelance': {
            'id': 42,
            'computed_skills': [
                {'id': 370, 'name': 'Javascript', 'duration_in_months': 54}
            ],
        }
    }


@pytest.fixture(scope='session')
def freelance_challenge_example():
    return {
        'freelance': {
            'id': 42,
            'user': {
                'first_name': 'Hunter',
                'last_name': 'Moore',
                'job_title': 'Fullstack JS Developer',
            },
            'status': 'new',
            'retribution': 650,
            'availability_date': datetime(2018, 6, 13),
            'professional_experiences': [
                {
                    'id': 4,
                    'company_name': 'Okuneva, Kerluke and Strosin',
                    'start_date': datetime(2016, 1, 1),
                    'end_date': datetime(2018, 5, 1),
                    'skills': [
                        {'id': 241, 'name': 'React'},
                        {'id': 270, 'name': 'Node.js'},
                        {'id': 370, 'name': 'Javascript'},
                    ],
                },
                {
                    'id': 54,
                    'company_name': 'Hayes - Veum',
                    'start_date': datetime(2014, 1, 1),
                    'end_date': datetime(2016, 9, 1),
                    'skills': [
                        {'id': 470, 'name': 'MySQL'},
                        {'id': 400, 'name': 'Java'},
                        {'id': 370, 'name': 'Javascript'},
                    ],
                },
                {
                    'id': 80,
                    'company_name': 'Harber, Kirlin and Thompson',
                    'start_date': datetime(2013, 5, 1),
                    'end_date': datetime(2014, 7, 1),
                    'skills': [
                        {'id': 370, 'name': 'Javascript'},
                        {'id': 400, 'name': 'Java'},
                    ],
                },
            ],
        }
    }


@pytest.fixture(scope='session')
def freelance_challenge_example_computed():
    return {
        'freelance': {
            'id': 42,
            'computed_skills': [
                {'id': 241, 'name': 'React', 'duration_in_months': 29},
                {'id': 270, 'name': 'Node.js', 'duration_in_months': 29},
                {'id': 370, 'name': 'Javascript', 'duration_in_months': 61},
                {'id': 470, 'name': 'MySQL', 'duration_in_months': 33},
                {'id': 400, 'name': 'Java', 'duration_in_months': 41},
            ],
        }
    }
