function $(id){ return document.getElementById(id);}

myStorage = window.sessionStorage;

function checkvalue(id) {
    var inputValue = $(id);
    if(inputValue.value == "Basic"){
        // inputValue.style.background-color = red;
        // inputValue.style.backgroundColor =#444;
        // inputValue.checked = true;
        // document.getElementById("Basic").checked = true;
        window.location.href = "http://127.0.0.1:8000/?level=Basic"
        // inputValue.checked = true;
        document.getElementById("Basic").checked = true;
        // inputValue.check()
        // inputValue.prop('checked',true);
        // alert("hee")

        sessionStorage.setItem('key', 'Basic');

    }
    else if(inputValue.value == "Intermediate"){
        window.location.href = "http://127.0.0.1:8000/?level=Intermediate"
        // inputValue.check()
        // placeholder="Intermediate"
        // inputValue.prop('checked',true);
        sessionStorage.setItem('key', 'Intermediate');
    }
    else if(inputValue.value == "Advanced"){
        window.location.href = "http://127.0.0.1:8000/?level=Advanced"
        // inputValue.prop('disabled',true);
        // inputValue.prop('checked',true);
        sessionStorage.setItem('key', 'Advanced');
    }

}

document.getElementById(sessionStorage.getItem('key')).prop('checked',true);

