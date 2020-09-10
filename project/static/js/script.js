function sendRequest() {
    var url = "https://api.github.com/zen";
    var XHR = new XMLHttpRequest();

    XHR.onreadystatechange = function() {
        if (XHR.readyState == 4) {
            document.getElementById('result').innerText = XHR.responseText
            console.log(XHR.responseText)
        }
    }

    XHR.open("GET", url);
    XHR.send();

}

function randomImgBtn() {
    var url = "https://dog.ceo/api/breeds/image/random"
    var XHR = new XMLHttpRequest();

    XHR.onreadystatechange = function() {
        if (XHR.readyState == 4 && XHR.status == 200) {
            var image_url = JSON.parse(XHR.responseText).message

            var img = document.querySelector('#photo')
            img.src = image_url

        }
    }

    XHR.open("GET", url)
    XHR.send()
}

function getBitcoinPrice() {
    var url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    var method = "GET"

    var XHR = new XMLHttpRequest()

    XHR.onreadystatechange = function() {
        if (XHR.readyState == 4 && XHR.status == 200) {
            var price = JSON.parse(XHR.responseText).bpi.USD.rate

            var spanId = document.querySelector('#bitcoin-price')
            spanId.innerHTML = price + " USD"
        }
    }


    XHR.open(method, url);
    XHR.send();
}