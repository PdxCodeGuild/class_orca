from django.test import TestCase

import datetime
from django.utils import timezone
from django.urls import reverse

from polls.models import Question

class QuestionModelTest(TestCase):
    def test_was_published_recently_with_FUTURE_question(self):
        ''' was_pub returns FALSE for Qs w/ pub_date in future'''

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_OLD_question(self):
        ''' was_pub returns FALSE for Qs w/ pub_date OLDER than 1 day'''
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False) 
    
    def test_was_published_recently_with_RECENT_question(self):
        '''was_pub returns TRUE for Qs w/ pub_date within last day'''
        time = timezone.now() - datetime.timedelta(hours=23, minutes= 59, seconds=59)
        current_question = Question(pub_date=time)
        self.assertIs(current_question.was_published_recently(), True)

def create_question(question_text, days):
    ''' helper for QIVT'''
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTest(TestCase):
    def test_no_question(self):
        '''
        if no question exist, message display
        '''
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'no polls')
        self.assertQuerysetEqual(response.context['latest_question_list'],[])

    def test_past_question(self):
        ''' Qs w/ pub_date in the past are displayed on index.html'''
        create_question(question_text='Past question.', days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )
    def test_future_question(self):
        '''
        Qs w/ pub_date in future are not displayed'''
        
        create_question(question_text='Future question.', days=30)
        response = self.client.get(reverse('polls:index'))
        
        self.assertContains(response, 'no polls')
        self.assertQuerysetEqual(response.context['latest_question_list'],[]
            )

    def test_future_question_and_past_question(self):
        ''' even if both past and future Qs exist only past Q are display'''

        create_question(question_text='Past question.', days =-30)
        create_question(question_text='Future question.', days=30)

        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'], ['<Question: Past question.>']
        )

    def test_two_past_questions(self):
        '''questions index page may display multiple Qs'''

        create_question(question_text='Past question 1.', days=-30)
        create_question(question_text='Past question 2.', days=-5)

        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )
    
    class QuestionDetailViewTests(TestCase):
        def test_future_question(self):
            ''' detail view of a Q w/ pub_date in future returns 404'''

            future_question = create_question(question_text='Future question.', days=5)
            url = reverse('polls:detail', args= (future_question.id,))

            response = self.client.get(url)
            self.assertEqual(response.status_code, 404)

    