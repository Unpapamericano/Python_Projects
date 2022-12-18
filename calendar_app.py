from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# A list to store appointments
appointments = []

@app.route('/')
def show_calendar():
  # Render the calendar template and pass in the list of appointments
  return render_template('calendar.html', appointments=appointments)

@app.route('/add', methods=['POST'])
def add_appointment():
  # Get the appointment details from the form submission
  title = request.form['title']
  date = request.form['date']
  time = request.form['time']

  # Convert the date and time to a datetime object
  appointment_time = datetime.strptime(f'{date} {time}', '%Y-%m-%d %H:%M')

  # Add the appointment to the list
  appointments.append({
    'title': title,
    'time': appointment_time
  })

  # Redirect the user back to the calendar page
  return redirect('/')

if __name__ == '__main__':
  app.run()