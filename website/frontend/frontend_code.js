console.log("Website Online!")

const WEBSITE_URL = 'https://c16826034f51.ngrok.io'

function doFunction() {  
  const result = fetch(`${WEBSITE_URL}/image/1`, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        // body: JSON.stringify(data1),
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