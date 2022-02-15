function $(id){ return document.getElementById(id);}

function checkvalue(id) {
    var inputValue = $(id);
    if(inputValue.value == "Basic"){
        window.location.href = "http://127.0.0.1:8000/?level=Basic"

    }
    else if(inputValue.value == "Intermediate"){
        window.location.href = "http://127.0.0.1:8000/?level=Intermediate"
    }
    else if(inputValue.value == "Advanced"){
        window.location.href = "http://127.0.0.1:8000/?level=Advanced"
    }

}

