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
survey_response_results = {} #key:value
survey_response_results_totals = {'2.1':0, '2.2':0, '2.3':0, '2.4':0, '2.5':0}

def display_survey_question():

    survey_id = 1

    for question_id, question in survey_questions_dictionary.items():
        print(question)

        for option, value in survey_response_options.items():
            print(option, value)

        response = 0
        
        while response < 1 or response > 6:
            response = int(input("Enter option (1-6): "))

        capture_survey_response(survey_id, question_id, response)
        survey_id += 1

def capture_survey_response(survey_id, question_id, response):
    survey_responses_list.append([survey_id, question_id, response])

def tabulate_survey_response_results():

    cnt = 0

    for response in survey_responses_list:
        survey_response_results_totals[response[1]] += response[2]

        if '2.5' == response[1]:
            cnt += 1

    for question_id, totals in survey_response_results_totals.items():
        survey_response_results[question_id] = totals / cnt

def get_course_average():
    total_average = 0
    total = 0

    for question_id, average in survey_response_results.items():
        total += average

    total_average = total / len(survey_response_results)

    return total_average

def get_faculty_rating(ratio):

    if (ratio <= 6 and ratio >= 5.5) :

        return 'Excellent'
    elif(ratio >= 5):
        return 'Very Good'

    elif (ratio >= 4):
        return 'Good'

    elif (ratio >= 3):
        return 'Needs Improvement'

    elif (ratio <= 3):
        return 'Unacceptable'
    
    else: 
        return 'Invalid value'
    
def display_menu():
    option = 0

    while option != 3:
        print('1-Enter survey responses: ')
        print('2-Get survey results: ')
        print('3-Exit')
        
        option = int(input("Enter option: "))
        
        handle_menu_options(option)

def handle_menu_options(option):

    if(option == 1):
        display_survey_question()
    elif(option == 2):
        tabulate_survey_response_results()

        average = get_course_average()

        print(average)

        rating = get_faculty_rating(average)

        print(rating)
    elif(option == 3):
        print('Exiting...')