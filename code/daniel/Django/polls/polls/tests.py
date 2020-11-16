from django.test import TestCase

import datetime
from django.utils import timezone
from django.urls import reverse
from .models import Question


class QuestionModelTest(TestCase):

    def test_was_published_recently_with_future_question(self):
        '''was_published_recently returns FALSE for questions that are published in the future'''
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False) 

    def test_was_published_recently_with_old_question(self):
        '''was_published_recently returns FALSE for questions that have a pub_date older than one day'''
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        '''was_published_recently returns TRUE for questions that have a pub_date within the last 24 hours'''
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        current_question = Question(pub_date=time)
        self.assertIs(current_question.was_published_recently(), True)

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)
        
class QuestionIndexViewTest(TestCase):
    def test_no_questions(self):
        '''if no question exists, a message is displayed'''
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available.')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
    
    def test_past_question(self):
        '''Questions with a pub_date in the past are displayed on index.html'''
        create_question(question_text='Past question.', days=-30) 
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question.>'])

    def test_future_questions(self):
        '''Questions with pub_date in the future are not displayed on the page'''
        create_question(question_text='Future question.', days=30)  
        response= self.client.get(reverse('polls:index'))
        self.assertContains(response, 'No polls are available.')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        '''Even if both past and future question exist, only the past questions are displayed'''
        create_question(question_text='Past question.', days=-30) 
        create_question(question_text='Future question.', days=30) 
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question.>'])

    def test_two_past_questions(self):
        '''The question index page may display multiple questions.'''
        create_question(question_text='Past question 1.', days=-30) 
        create_question(question_text='Past question 2.', days=-5) 
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question 2.>', '<Question: Past question 1.>'])

class DetailViewTest(TestCase):
    def test_future_question(self):
        '''The detail view of a question with a pub_date in the future returns a 404 not found'''
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:details', args=(future_question.id,)) 
        response = self.client.get(url) 
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        '''The detail view of a question with a pub_date in the past displays the questions text'''
        past_question = create_question(question_text='Past question.', days=-5)
        url = reverse('polls:details', args=(past_question.id,)) 
        response = self.client.get(url) 
        self.assertContains(response, past_question.question_text)

