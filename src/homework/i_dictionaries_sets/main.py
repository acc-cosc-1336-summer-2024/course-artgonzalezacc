#
import dictionary

choice = 1

while choice == 1:
    dictionary.display_survey_question()
    choice = int(input("Enter another one"))


dictionary.tabulate_survey_response_results()

average = dictionary.get_course_average()

print(average)

rating = dictionary.get_faculty_rating(average)

print(rating)