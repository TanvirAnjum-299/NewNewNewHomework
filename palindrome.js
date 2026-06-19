function checkpalindrome (mystring){

var inputstring=mystring.replace(/[^A-Z0-9]/ig, "").toLowerCase();

var reversedinput=inputstring.split('').reverse().join('');

if(inputstring===reversedinput){
    document.write(mystring+"Is a palindrome");
}else{
    document.write(mystring+"Is a palindrome");
}



}


checkpalindrome('madam')