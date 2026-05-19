from responses import responses

def get_response(user_input):

    user_input = user_input.lower()

    for keyword in responses:

        if keyword in user_input:

            return responses[keyword]

    return """
Sorry, I could not understand your question.

Please ask about:
- Admissions
- Attendance
- Exams
- Fees
- Departments
- Hostel
- Library
- Placement
- Sports
"""