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

function getFetchBitcoinPrice() {
    var url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    var price = "";
    var spanId = document.querySelector('#bitcoin-price')

    fetch(url)
        .then(function(respone) {
            return respone.json()
        })
        .then(function(data) {
            console.log(data.bpi.USD.rate)
            price = data.bpi.USD.rate
            spanId.innerHTML = price + " USD"
        })
        .catch(function(err) {
            console.log(err)
        })

}

function findClot() {
    var url = "https://api.github.com/users/clot"
    var avatarId = document.querySelector('#avatarId')
    var status = document.querySelector('#status')

    fetch(url)
        .then(handleErrors)
        .then(function(data) {
            console.log(data.name)
            avatarId.src = data.avatar_url
        })
        .catch(function(error) {
            status.innerHTML = error;
        })
}

function handleErrors(response) {
    if (!response.ok) {
        throw Error(response.status)
    }
    return response.json()
}


function randomUser() {
    var url = "https://randomuser.me/api/"
    var fullname = document.querySelector('#name')
    var title_id = document.querySelector('#title')
    var email_id = document.querySelector('#email')
    var city_id = document.querySelector('#city')
    var profile_id = document.querySelector('#profile_avatar')

    fetch(url)
        .then(handleErrors)
        .then(function(response) {
            console.log(response.results[0].name.first)
            var firstname = response.results[0].name.first
            var lastname = response.results[0].name.last
            var title = response.results[0].name.title
            var email = response.results[0].email
            var city = response.results[0].location.city
            var profile = response.results[0].picture.large

            fullname.innerHTML = firstname + " " + lastname
            title_id.innerHTML = title
            email_id.innerHTML = email
            city_id.innerHTML = city
            profile_id.src = profile

        })
        .catch(function(error) {
            console.log(error)
        })
}


$(document).ready(function() {
    var cat_url = "https://api.thecatapi.com/v1/images/search";
    $("#randomCatBtn").click(function() {


        $.ajax({
                method: "GET",
                url: cat_url
            })
            .done(function(msg) {
                var cat_img_url = msg[0].url
                $('#cat_photo').attr('src', cat_img_url)
            });
    });
});