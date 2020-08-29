# -*- coding: utf-8 -*-

from unittest import mock

from flask import url_for


class TestComputeSkills(object):
    def test_should_fail_with_unexpected_payload(self, app, client):
        with app.test_request_context():
            res = client.post(
                url_for('freelancers.compute_skills'), json='wrong payload',
            )
            assert res.status_code == 422

    def test_should_handle_correctly_an_unexpected_exception(
        self, app, client, freelance_compute_skills_payload,
    ):
        with mock.patch(
            'app.modules.freelancers.views.compute_freelance_skills',
            side_effect=Exception('wat'),
        ):
            with app.test_request_context():
                res = client.post(
                    url_for('freelancers.compute_skills'),
                    json=freelance_compute_skills_payload,
                )
                assert res.status_code == 500

    def test_should_works_with_a_correct_payload(
        self,
        app,
        client,
        freelance_compute_skills_payload,
        freelance_compute_skills_result,
    ):
        with app.test_request_context():
            res = client.post(
                url_for('freelancers.compute_skills'),
                json=freelance_compute_skills_payload,
            )
            assert res.status_code == 200
            assert res.get_json() == freelance_compute_skills_result
