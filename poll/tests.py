from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question
# Create your tests here.
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time=timezone.now()+ datetime.timedelta(days=30)
        future_question=Question(pub_date =time)
        self.assertIs(future_question.was_published_recently(),False)

        
    def test_was_published_recently_with_old_question:
        time=timezone.now()+ datetime.timedelta(days=30,seconds=1)
        old_question=Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(),False)
    