function myFunction(){
    var password = document.querySelector("#generatedpassword").textContent;
    var dummy = document.createElement("textarea");
    document.body.appendChild(dummy);
    dummy.value = password;
    dummy.select();
    document.execCommand("copy");
    document.body.removeChild(dummy);
}