BACKEND_URL = "127.0.0.1/5000"

async function loadStudentDashboard(student_id){
  // redirect to url
  // {URL}/studentdashboard/{student_id}
  const response = await fetch(`${BACKEND_URL}/get_student_info/${student_id}`, {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({'auth_token': document.cookie}),
  })

  if (!response.ok) {
    const message = `Error: ${response.status}`;
    throw new Error(message);
  } else {
    const result = await response.json();

    const first_name = response['fname'];
    const edu_category = response['edu_category'];
    const teach_level = response['teach_level'];
    const mentor_connections = response['mentor_connections'];
    
    // load content onto page with above variables
  }
}

async function loadMentorDashboard(mentor_id){
  // redirect to url
  // {URL}/mentordashboard/{mentor_id}
  const response = await fetch(`${BACKEND_URL}/get_mentor_info/${mentor_id}`, {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({'auth_token': document.cookie}),
  })

  if (!response.ok) {
    const message = `Error: ${response.status}`;
    throw new Error(message);
  } else {
    const result = await response.json();

    const first_name = response['fname'];
    const edu_category = response['edu_category'];
    const teach_level = response['teach_level'];
    const student_connections = response['student_connections'];
    
    // load content onto page with above variables
  }
}

