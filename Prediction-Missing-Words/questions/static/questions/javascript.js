function $(id){ return document.getElementById(id);}

// var level = $(id)


function checkvalue(id) {
    var inputValue = $(id);
    if(inputValue.value == "Basic"){
        window.location.href = "http://127.0.0.1:8000/?level=Basic"
        inputValue.style.backgroundColor = "#5aa469";
        inputValue.check()
        inputValue.prop('checked',true);
        // alert("hee")
    }
    else if(inputValue.value == "Intermediate"){
        alert("2")
        window.location.href = "http://127.0.0.1:8000/?level=Intermediate"
        console("sjj")
        inputValue.check()
        placeholder="Intermediate"
    }
    else if(inputValue.value == "Advanced"){
        // alert("3")
        window.location.href = "http://127.0.0.1:8000/?level=Advanced"
        inputValue.prop('disabled',true);
    }
    // else if(inputValue.value != ""){
    //     inputValue.style.backgroundColor = "#d35d6e";
    //     // display_unsuccess();
    //
    // }
}
