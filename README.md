# Canvas Enrollment Management Script
## Purpose
This script performs bulk Canvas enrollment management using CSV files. It can:
- Add users to courses
- Remove enrollments from courses
- Process multiple course IDs in a single file
- Handle CSV files with or without headers
## Requirements
Install the required dependency:
```bash
pip install requests
```
## Configuration
Update the following values before running the script:
```python
BASE_URL = "https://example.beta.instructure.com"  # beta or production url
TOKEN = "token_goes_here"
```
Example:
```python
BASE_URL = "https://canvas.instructure.com"
TOKEN = "your_canvas_api_token"
```
## CSV Format
### Removing Enrollments
File: `enrollments.csv`
```csv
course_id,enrollment_id
12345,10001
12345,10002
67890,20001
```
or
```csv
12345,10001
12345,10002
67890,20001
```
### Adding Enrollments
File: `enrollments_needed.csv`
```csv
course_id,user_id
12345,5555
12345,6666
67890,7777
```
or
```csv
12345,5555
12345,6666
67890,7777
```
Headers are optional.
## Usage
### Remove Enrollments
Uncomment:
```python
filename = "enrollments.csv"
del_enrollments(filename)
```
### Add Enrollments
Uncomment:
```python
filename = "enrollments_needed.csv"
add_enrollments(filename)
```
## Testing Mode
The Canvas API calls are currently commented out. Running the script will only print the actions that would be performed.
Example:
```text
del 12345 10001
del 12345 10002
add 12345 5555
add 12345 6666
```
After validating the output, uncomment the appropriate `requests.delete()` or `requests.post()` code blocks to make actual changes in Canvas.
## Notes
- Supports multiple course IDs in the same CSV file.
- Automatically ignores header rows.
- Automatically skips blank rows.
- Displays an error if the input file cannot be found.
- Recommended to test in a Canvas Beta environment before running in Production.
## Example
CSV:
```csv
course_id,enrollment_id
12345,10001
12345,10002
67890,20001
```
Output:
```text
del 12345 10001
del 12345 10002
del 67890 20001
```
## Warning
Enrollment additions and removals affect real user access in Canvas. Always verify the CSV contents and test in a non-production environment before running against Production.

