console.log("Hello!")

function doFunction() {
  // const data1 = {
  //   "name": "Golden Retriever in a flower crown",
  //   "url": "1",
  //   "views": 1
  //   }
  
  // const data2 = {
  //   "name": "Hello There",
  //   "url": "2",
  //   "views": 100000000000
  //   }
  
  const result = fetch(`http://127.0.0.1:5000/image/1`, {
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