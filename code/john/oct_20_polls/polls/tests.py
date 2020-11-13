# THIS FILE IS AWESOME, BECAUSE YOU CAN WRITE TESTS HERE, THEN WRITE CODE AROUND THIS...
from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone
from django.urls import reverse

from polls.models import Question
# the below showed that our 'is recent' was buggy...
# future_question = Question(pub_date = timezone.now() + datetime.timedelta(days=30))
# future_question.was_published_recently()

class QuestionModelTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        '''
        checks if was_published_recently returns FALSE for questions whose pub_date is in the future
        '''
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date = time)
        self.assertIs(future_question.was_published_recently(), False) # assert: word to ask a question, and the Q comes back with a response 
        # Q How is assert different than an IF statement, or even a TRY statement?

    def test_was_published_recently_with_old_question(self):
        '''
        checks if was_published_recently returns FALSE for questions whose pub_date is OLDER than 1 day
        '''
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date = time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        '''
        checks if was_published_recently returns TRUE for questions whose pub_date is WITHIN 1 day
        '''
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date = time)
        self.assertIs(recent_question.was_published_recently(), True)

# this is outside, as "a helper function" to make a new question...
def create_question(question_text, days):
    # time2 = timezone.now()
    time = timezone.now() + datetime.timedelta(days=days)
    # print(f'{time2} is time2, HI!')
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTest(TestCase):
    def test_no_questions(self):
        '''
        If there are no questions, a message is displayed:
        '''
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available.') # check matches line 9 of //index.html:  <p>No polls are available.</p>
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        '''
        questions with a pub_date in the past are displayed in index.html
        '''
        create_question(question_text='Past question.', days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_future_question(self):
        '''
        questions with a pub_date in the past are NOT displayed on the page
        '''
        create_question(question_text='Future question.', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, 'No polls are available.')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):        
        '''
        even if both past and future questions exist, only the past questions are displayed
        '''

        create_question(question_text='Past question.', days=-30)
        create_question(question_text='Future question.', days=30)
        
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_two_past_questions(self):        
        '''
        the question indext page may display multiple questions
        '''
        
        create_question(question_text='Past question 1.', days=-30)        
        create_question(question_text='Past question 2.', days=-5)

        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )

class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        '''
        the detail view of a question with a pub date in the future returns a 404 not found
        '''
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))

        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        '''
        the detail view of a question with a pub_date in the past displays the question's text
        '''
        past_question = create_question(question_text='Past question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))

        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)



