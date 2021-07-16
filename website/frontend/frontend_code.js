console.log("Website Online!")

const WEBSITE_URL = 'http://127.0.0.1:5000'

const dummy_image_data = {
  "name": "Golden Retriever in a flower crown",
  "url": "1",
  "views": 1
}

function getImage() {  
  const result = fetch(`${WEBSITE_URL}/image/1`, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
    }).then((data) => {
        if (data.status === 200) {
            data.json().then(result => {
                console.log(result)
            })
        }
    }).catch((error) => {
        console.log('Error: ', error);
    });
}

function postImage() {  
  const result = fetch(`${WEBSITE_URL}/image/1`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dummy_image_data),
    }).then((data) => {
        if (data.status === 200) {
            data.json().then(result => {
                console.log(result)
            })
        }
    }).catch((error) => {
        console.log('Error: ', error);
    });
}

function sendSMS() {
  const dummy_sms_data = {
    "number": document.getElementById('phone_input').value,
    "message": document.getElementById('sms_message_input').value
  }
  const result = fetch(`${WEBSITE_URL}/sms`, {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(dummy_sms_data),
  }).then((data) => {
      if (data.status === 200) {
          data.json().then(result => {
              console.log(result)
          })
      }
  }).catch((error) => {
      console.log('Error: ', error);
  });
}