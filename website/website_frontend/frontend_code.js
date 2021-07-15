console.log("Hello!")

function doFunction() {
  const data1 = {
    "name": "Golden Retriever in a flower crown",
    "url": "1",
    "views": 1
    }
  
  const result = fetch(`http://127.0.0.1:5000/image/1`, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        // body: JSON.stringify(data1),
    }).then((data) => {
        if (data.status === 400) {
            alert('Please enter into ALL fields')
        } else if (data.status === 403) {
            alert('Incorrect Username or Password')
        } else if (data.status === 409) {
            alert('Username taken')
        } else if (data.status === 200) {
            data.json().then(result => {
                console.log(result)
            })
        }
    }).catch((error) => {
        console.log('Error: ', error);
    });

}