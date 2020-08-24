# -*- condig: utf-8 -*-

from app.utils.computers import compute_freelance_skills


class TestComputeFreelanceSkills(object):
    def test_one_experience(
        self, freelance_one_experience, freelance_one_experience_computed
    ):
        computed = compute_freelance_skills(freelance_one_experience)
        assert computed == freelance_one_experience_computed

    def test_two_experiences_with_same_skill_in_continuous_time(
        self,
        freelance_two_experiences_with_same_skill_in_continuous_time,
        freelance_two_experiences_with_same_skill_in_continuous_time_computed,
    ):
        computed = compute_freelance_skills(
            freelance_two_experiences_with_same_skill_in_continuous_time
        )
        assert (
            computed
            == freelance_two_experiences_with_same_skill_in_continuous_time_computed
        )

    def test_two_experiences_with_same_skill_with_interval_between(
        self,
        freelance_two_experiences_with_same_skill_with_interval_between,
        freelance_two_experiences_with_same_skill_with_interval_between_computed,
    ):
        computed = compute_freelance_skills(
            freelance_two_experiences_with_same_skill_with_interval_between
        )
        assert (
            computed
            == freelance_two_experiences_with_same_skill_with_interval_between_computed
        )

    def test_two_experiences_with_same_skill_in_converge_time(
        self,
        freelance_two_experiences_with_same_skill_in_converge_time,
        freelance_two_experiences_with_same_skill_in_converge_time_computed,
    ):
        computed = compute_freelance_skills(
            freelance_two_experiences_with_same_skill_in_converge_time
        )
        assert (
            computed
            == freelance_two_experiences_with_same_skill_in_converge_time_computed
        )

    def test_challenge_example(
        self, freelance_challenge_example, freelance_challenge_example_computed
    ):
        computed = compute_freelance_skills(freelance_challenge_example)
        assert computed == freelance_challenge_example_computed
