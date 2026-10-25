import csv
import requests

BASE_URL = "https://example.beta.instructure.com"  # beta or production url
TOKEN = "token_goes_here"  # Replace with your actual token
headers = {"Authorization": f"Bearer {TOKEN}"}


def read_file(filename):
    """
    Reads a CSV file and returns a list of (course_id, enrollment_id) tuples.
    Handles CSVs with or without headers.
    """
    enrollments = []

    with open(filename, newline="") as f:
        reader = csv.reader(f)

        for row in reader:
            # Skip blank rows
            if not row or len(row) < 2:
                continue

            try:
                course_id = int(row[0].strip())
                enrollment_id = int(row[1].strip())

                enrollments.append((course_id, enrollment_id))

            except ValueError:
                # Header row or invalid data e.g. "course_id,enrollment_id"
                continue

    return enrollments


def del_enrollments(filename):
    """
    @param filename: Path to the CSV file containing course_id and enrollment_id pairs.
    @return None. course_id and enrollment_id pairs to be deleted.
    """
    try:
        enrollments = read_file(filename)

        for course_id, enrollment_id in enrollments:
            # url = f"{BASE_URL}/api/v1/courses/{course_id}/enrollments/{enrollment_id}"

            # response = requests.delete(
            #     url,
            #     headers=headers,
            #     params={"task": "delete"}
            # )

            # print(f"del {course_id} {enrollment_id} {response.status_code}")  # print confirmation 
            print(f"del {course_id} {enrollment_id}")  # debugging 

    except FileNotFoundError:
        print(f"Error: '{filename}' does not exist.")


def add_enrollments(filename):
    """
    @param filename: Path to the CSV file containing course_id and user_id pairs.
    @return None. course_id and user_id pairs to be added.
    """
    try:
        enrollments_needed = read_file(filename)

        for course_id, user_id in enrollments_needed:
            # url = f"{BASE_URL}/api/v1/courses/{course_id}/enrollments"

            # payload = {
            #         "enrollment[user_id]": user_id,
            #         "enrollment[type]": "StudentEnrollment",
            #         "enrollment[enrollment_state]": "active"
            #     }
            
            # response = requests.post(url, headers=headers, data=payload)

            # print("add", user_id, response.status_code)  # print confirmation
            print("add", course_id, user_id)  # debugging

    
    except FileNotFoundError:
        print(f"Error: '{filename}' does not exist.")


###
filename = "enrollments.csv"  # remove
# del_enrollments(filename)
# filename = "enrollments_needed.csv"  # add
add_enrollments(filename)