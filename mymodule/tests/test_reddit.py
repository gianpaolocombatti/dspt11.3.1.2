from mymodule.reddit import User, Topic

def test_create_user():
    name = 'test user'
    reputation = 498
    is_moderator = True
    test_user = User(name=name, reputation=reputation, is_moderator=is_moderator)
    assert(type(test_user) == User and
           test_user.name == name and
           test_user.reputation == reputation and
           test_user.is_moderator == is_moderator)

def test_user_upvote_topic(test_user, test_topic):
    up_votes = test_topic.up_votes
    test_user.up_vote(test_topic)
    assert(test_topic.up_votes == up_votes + 1)
