import requests
import csv
import time

# Function to generate the URL with answers
def generate_url(base_url, answers, name):
    query_params = "&".join([f"question{i+1}={answer}" for i, answer in enumerate(answers)])
    return f"{base_url}&name={name}&{query_params}"

# Function to read the student names from the CSV file
def read_student_names(filename='students.csv'):
    student_names = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                if row and len(row) > 0 and row[0].strip():  # Ensure non-empty and valid name
                    student_names.append(row[0])  # Add the student name to the list
    except FileNotFoundError:
        print(f"{filename} not found. Please make sure the file exists.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    
    return student_names

# Main function to submit answers
def submit_answers():
    # Read student names from the CSV file
    student_names = read_student_names()

    # List of subjects with their base URLs and answers
    subjects = [
        {
            "base_url": "http://122.3.185.245:8081/ROXRUQA/submitprocess.php?grade=11&schoolid=303988&subject=English+11-12+Q2+-+FINAL+COPY.pdf",
            "answers": [
                'c', 'a', 'a', 'b', 'b', 'b', 'c', 'a', 'b', 'c',
                'a', 'c', 'b', 'b', 'c', 'b', 'c', 'a', 'c', 'b',
                'c', 'a', 'c', 'b', 'b', 'c', 'c', 'b', 'a', 'a',
                'b', 'd', 'c', 'c', 'b', 'a', 'c', 'b', 'b', 'a',
                'c', 'c', 'c', 'b', 'b', 'c', 'a', 'd', 'b', 'a'
            ]
        },
        {
            "base_url": "http://122.3.185.245:8081/ROXRUQA/submitprocess.php?grade=11&schoolid=303988&subject=MATH+11+Q2+RUQA+FINAL.pdf",
            "answers": [
                'd', 'a', 'b', 'c', 'b', 'a', 'b', 'a', 'c', 'a',
                'd', 'b', 'a', 'c', 'c', 'b', 'b', 'b', 'd', 'a',
                'd', 'a', 'b', 'c', 'd', 'a', 'a', 'c', 'c', 'a',
                'd', 'b', 'a', 'd', 'd', 'b', 'c', 'b', 'c', 'b',
                'c', 'b', 'b', 'b', 'a', 'd', 'd', 'd', 'a', 'd',
            ]
        },
        {
            "base_url": "http://122.3.185.245:8081/ROXRUQA/submitprocess.php?grade=11&schoolid=303988&subject=Komunikasyon+at+Pananaliksik+Baitang+11.pdf",
            "answers": [
                "c", "d", "d", "c", "b", "b", "a", "d", "c", "b", 
                "d", "a", "a", "a", "c", "c", "c", "b", "a", "c", 
                "b", "a", "d", "c", "a", "c", "a", "c", "a", "a",
                "a", "a", "a", "a", "c", "c", "c", "b", "b", "c", 
                "b", "c", "c", "b", "c", "b", "b", "a", "a", "b",
                "c", "b", "c", "b", "c", "c", "c", "b", "b", "c", 
                "b"
            ]
        },
        {
            "base_url": "http://122.3.185.245:8081/ROXRUQA/submitprocess.php?grade=11&schoolid=303988&subject=Science+11Earth%26Life_2nd+Quarter+Final+RUQA.pdf",
            "answers": [
                'a', 'c', 'd', 'b', 'b', 'b', 'c', 'd', 'a', 'd',
                'a', 'd', 'a', 'a', 'b', 'd', 'a', 'a', 'c', 'c',
                'a', 'd', 'd', 'd', 'd', 'b', 'a', 'c', 'c', 'd',
                'c', 'd', 'd', 'a', 'a', 'c', 'a', 'a', 'a', 'a',
                'a', 'a', 'c', 'd', 'c', 'd', 'a', 'd', 'c', 'c'
            ]
        },
        {
            "base_url": "http://122.3.185.245:8081/ROXRUQA/submitprocess.php?grade=11&schoolid=303988&subject=Science+11PhysicalScience_2nd+Quarter+Final+RUQA.pdf",
            "answers": [
                "c", "c", "a", "b", "b", "c", "a", "a", "c", "a",
                "a", "a", "a", "c", "c", "c", "b", "a", "c", "b",
                "a", "d", "c", "a", "c", "a", "c", "a", "a", "a",
                "a", "a", "a", "c", "c", "c", "b", "b", "c", "b",
                "c", "c", "b", "c", "b", "b", "a", "a", "b", "c",
                "b", "c", "b", "c", "c", "c", "b", "b", "c", "b"
            ]
        },
        {
            "base_url": "http://122.3.185.245:8081/ROXRUQA/submitprocess.php?grade=11&schoolid=303988&subject=Grade+11+-+Values+Education+2Q+RUQA+FINAL+QUESTIONS.pdf",
            "answers": [
                "b", "b", "b", "b", "b", "b", "a", "b", "b", "b",
                "b", "b", "b", "b", "b", "b", "b", "a", "b", "b",
                "b", "b", "b", "b", "b", "b", "b", "b", "b", "b",
                "b", "b", "b", "b", "b", "b", "b", "b", "b", "b",
                "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"
            ]
        }
    ]
    
    # Iterate over all students and submit answers for each student
    for student_name in student_names:
        # Iterate over all subjects and submit answers
        for subject in subjects:
            # Generate the complete URL for the current subject
            full_url = generate_url(subject["base_url"], subject["answers"], student_name)
            
            # Print the final URL for debugging purposes
            print(f"Generated URL for {student_name} - subject: {subject['base_url'].split('subject=')[1]}:")
            print(full_url)

            # Retry mechanism for sending the request until successful
            while True:
                try:
                    response = requests.get(full_url, timeout=10)  # Set timeout to 10 seconds
                    if response.status_code == 200:
                        print(f"Answers submitted successfully for {student_name} - {subject['base_url'].split('subject=')[1]}!")
                        break  # Exit the loop if successful
                    else:
                        print(f"Failed to submit answers for {student_name} - {subject['base_url'].split('subject=')[1]}. HTTP Status Code: {response.status_code}")
                        break  # Exit the loop if the server responded with an error
                except requests.exceptions.Timeout:
                    print(f"Connection timed out for {student_name} - {subject['base_url'].split('subject=')[1]}. Retrying...")
                    time.sleep(2)  # Wait for 2 seconds before retrying
                except Exception as e:
                    print(f"An error occurred for {student_name} - {subject['base_url'].split('subject=')[1]}: {e}")
                    break  # Exit the loop if there's an unexpected error

# Run the function
if __name__ == "__main__":
    submit_answers()
