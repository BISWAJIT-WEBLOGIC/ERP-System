function checkPassword() {
    var password = document.getElementById("password").value;
    var cPassword = document.getElementById("c-password").value;

    //minimum password length validation  
    if (password.length < 8 || cPassword.length < 8) {
        
        document.getElementById("error").innerHTML = "Password length must be atleast 8 characters";
        document.getElementById("from1").reset();
        return false;
        
    }
    
    if (password != cPassword) {
        document.getElementById("error").innerHTML = "Passwords don't Match";
        document.getElementById("from1").reset();
        return false;
    }
    else {
        return true;
    }

}