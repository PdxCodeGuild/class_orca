from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
import datetime

from .models import Question

class QuestionModelTest(TestCase):

    def test_was_published_recently_with_future_q(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_q(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)
    
    def test_was_published_recently_with_recent_q(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59)
        recent_q = Question(pub_date=time)
        self.assertIs(recent_q.was_published_recently(), True)

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTest(TestCase):
    def test_no_questions(self):

        response = self.client.get(reverse('polls:index'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'No polls available')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        create_question(question_text='Past question', days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question>']
        )

    def test_future_question(self):
        create_question(question_text="future question", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
    
    def test_future_q_and_past_q(self):
        create_question(question_text='Past question', days=-30)
        create_question(question_text="Future question", days=+30)

        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question>']
        )
    
    def test_two_past_q(self):
        create_question(question_text='Past question 1', days=-30)
        create_question(question_text='Past question 2', days=-5)

        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2>', '<Question: Past question 1>']
        )

# class QuestionDetailViewTest(TestCase):
#     def test_future_question(self):

#         future_question = create_question(question_text='Future question', days=5)
#         url = reverse('polls:detail', args=(future_question.id,))

#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 404)







