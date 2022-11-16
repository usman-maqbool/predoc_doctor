from datetime import date, datetime
class Parser(object):

   def __init__(self, payload):
      self.questions = payload['form_response']['definition']['fields']
      self.answers = payload['form_response']['answers']
      self.variables = payload['form_response'] or None
      self.formatted_answer = []
      self.formatted_questions = []
      self.questionnaire = []
      self.none_choiced_fields  = ['phone_number', 'date', 'number', 'website', 'opinion_scale', 'email', 'rating', 'short_text', 'long_text', 'yes_no']
      self.choiced_fields  = ['multiple_choice', 'picture_choice', 'dropdown']

   def __get_type_question(self, question):
      return question.get('title')


   def __get_type_answer(self, answer):
      if answer.get('type') == 'choice':
         return answer.get('choice').get('label')
      return answer[answer.get('type')]


   def __get_original_question(self, q_payload):
      type = q_payload.get('type')
      if type in self.none_choiced_fields:
         return {
               'title' : q_payload.get("title"),
               'choices': None
            }
      elif type in self.choiced_fields:  
         return {
               'title' : q_payload.get('title'),
               "choices" : q_payload.get('choices')
            }

   def parse_answers(self):
      for answer in self.answers:
         self.formatted_answer.append(self.__get_type_answer(answer))
      return self.formatted_answer

   def parse_questions(self):
      for question in self.questions:
         self.formatted_questions.append(self.__get_type_question(question))
      return self.formatted_questions

   def parse_original_questionnaire(self):
      for question in self.questions:
         self.questionnaire.append(self.__get_original_question(question))
      return self.questionnaire

   def get_date_of_birth(self):
      for answer in self.answers:
         if answer.get('type') == 'date':
            return answer.get('date')

   def get_age(self):
      today = date.today()
      birthdate = self.get_date_of_birth()
      birthdate = datetime.strptime(birthdate, '%Y-%m-%d').date()
      return  today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
   
   def get_first_name(self):
      for question in self.questions:
         if "first name" in question.get('title'):
            ref = question.get('ref')
            break
      for answer in self.answers:
         if answer.get('field').get('ref') == ref:
            return answer.get('text')