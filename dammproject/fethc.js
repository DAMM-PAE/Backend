const url = "http://nattech.fib.upc.edu:40540/api/bars/3/";

fetch(url).then((response) => {
    return response.json();
    }).then((data) => {
    console.log(data);
    })