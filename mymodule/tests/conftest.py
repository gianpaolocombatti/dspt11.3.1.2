import pytest
from mymodule.reddit import User, Topic

@pytest.fixture()
def test_user():
    test_user = User(name='test user', reputation=5000, is_moderator=False)
    return test_user

@pytest.fixture()
def test_topic(test_user):
    test_topic = Topic(title = 'test_title', body='test_body', user=test_user)
    return test_topic

