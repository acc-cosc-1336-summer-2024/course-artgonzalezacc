#
survey_questions_dictionary = \
{
    '2.1':'The texts, assigned readings, and other course resources help me learn the course material.',
    '2.2':'Clear instructions are provided',
    '2.3':'Tests, papers, assignments, and or other activities include clear instructions.' ,
    '2.4':'Uses instructional technology',
    '2.5':'Tests, papers, assignments, or other activities'     
}

survey_response_options = {1:'Never',2:'Sometimes',3:'More',4:'More more',5:'Always', 6:'Always Always'}
survey_responses_list = [] #surveyid, questionid, response

def display_survey_question():

    survey_id = 1

    for question_id, question in survey_questions_dictionary.items():
        print(question)

        for option, value in survey_response_options.items():
            print(option, value)

        response = int(input("Enter option: "))

        capture_survey_response(survey_id, question_id, response)
        survey_id += 1
        
        print(survey_responses_list)

def capture_survey_response(survey_id, question_id, response):
    survey_responses_list.append([survey_id, question_id, response])