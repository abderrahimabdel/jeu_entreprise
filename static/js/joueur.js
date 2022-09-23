divId = document.querySelector("#temps");
const url = window.location.href
var minutes = Math.floor(temps/60)
var secondes = temps%60
var minutesText
var secondesText
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const runTime = setInterval(() => {
    
    minutesText = minutes
    if (minutes.toString().length < 2) {
        minutesText = "0" + minutes
    }
    secondesText = secondes
    if (secondes.toString().length < 2) {
        secondesText = "0" + secondes
    }

    divId.innerText = minutesText + ":" + secondesText
    
    if (secondes == 0) {secondes=59;minutes--}
    if (minutes < 0) {clearInterval(runTime);minutes=0;secondes=0}
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    data['temps'] = temps
    $.ajax({
        type: 'POST',
        url: `${url}/save`,
        data: data,
        success: function(response){
            const results = response.results
        }
    })
    secondes--
    temps--
},1000);