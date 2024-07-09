/* -----------------------------------------
FULL VALIDATION FORM
------------------------------------------*/
//  1) iNPUT MASK (PHONE)

$(document).ready(function(){

    $(".phone").inputmask("(999) 999-999-9999",{"onincomplete":function(){
       $(".phone").val("");
       swal("Oops !", "Incomplete phone, Please review !","info");
       return false;
    }});
   
   });
   
   // 2) iNPUT VALIDATION
   // a) Frontend form
   
   function validateEmail(email){
       const regex =  /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
       return regex.test(email);
   }
   function validateForm(){
       const name = document.getElementById("name").value;
       const age = document.getElementById("age").value;
       const phone = document.getElementById("phone").value;
       const email = document.getElementById("email").value;
       const address = document.getElementById("address").value;
       const experience = document.getElementById("experience").value;
       const skills = document.getElementById("skills").value;
       const file = document.getElementById("file").value;
   
       if(name == ""){
           document.getElementById("bg-spinner").style.display ="none";
           swal("Opsss !","Name field cannot be empty.","error");
           return false;
       }
   
       else if(name == name.toUpperCase()){
        document.getElementById("bg-spinner").style.display ="none";
           document.getElementById("name").value=" ";
           swal("Opsss !","Name field cannot be UPPERCASE.","info");
           return false;
       }
   
       else if(name.split(' ').length < 2){
        document.getElementById("bg-spinner").style.display ="none";
           
           swal("Opsss !","Your fullname is REQUIRED","info");
           return false;
       }
   
       else if(age == ""){
        document.getElementById("bg-spinner").style.display ="none";
           swal("Opsss !","Age field cannot be empty.","error");
           return false;
       }
   
       else if((age < 18) || (age > 50)){
        document.getElementById("bg-spinner").style.display ="none";
           document.getElementById('age').value='';
           swal("Opsss !","Age only between 18 and 50 years old","info");
           return false;
       }
   
       else if(email == ""){
        document.getElementById("bg-spinner").style.display ="none";
           swal("Opsss !","Email field cannot be empty.","error");
           return false;
       }
   
       else if(!(validateEmail(email))){
        document.getElementById("bg-spinner").style.display ="none";
           document.getElementById('email').value='';
           swal("Opsss !","Put a valid email address.","error");
           return false;
       }
   
       else if(phone == ""){
        document.getElementById("bg-spinner").style.display ="none";
           swal("Opsss !","Phone field cannot be empty.","error");
           return false;
       }
   
       else if(experience == ""){
        document.getElementById("bg-spinner").style.display ="none";
           swal("Opsss !","Experience field cannot be empty.","error");
           return false;
       }
       
       else if(skills == ""){
        document.getElementById("bg-spinner").style.display ="none";
           swal("Opsss !","Skills field cannot be empty.","error");
           return false;
       }
   
       else if(file == ""){
        document.getElementById("bg-spinner").style.display ="none";
           swal("Opsss !","File field cannot be empty.","error");
           return false;
       }
   
       else{
           return true;
       }
   }
   
   
   
   
   // b) Backend form
   
   function validateEmail2(email2){
       const regex =  /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
       return regex.test(email2);
   }
   function validateForm2(){
       const name2 = document.getElementById("name2").value;
       const age2 = document.getElementById("age2").value;
       const phone2 = document.getElementById("phone2").value;
       const email2 = document.getElementById("email2").value;
       const address2 = document.getElementById("address2").value;
       const experience2 = document.getElementById("experience2").value;
       const skills2 = document.getElementById("skills2").value;
       const file2 = document.getElementById("file2").value;
   
       if(name2 == ""){
        document.getElementById("bg-spinner").style.display ="none";
           swal("Opsss !","Name field cannot be empty.","error");
           return false;
       }
   
       else if(name2 == name2.toUpperCase()){
        document.getElementById("bg-spinner").style.display ="none";
           document.getElementById("name2").value=" ";
           swal("Opsss !","Name field cannot be UPPERCASE.","info");
           return false;
       }
   
       else if(name2.split(' ').length < 2){
        document.getElementById("bg-spinner").style.display ="none";
           
           swal("Opsss !","Your fullname is REQUIRED","info");
           return false;
       }
   
       else if(age2 == ""){
        document.getElementById("bg-spinner").style.display ="none";
           swal("Opsss !","Age field cannot be empty.","error");
           return false;
       }
   
       else if((age2 < 18) || (age2 > 50)){
        document.getElementById("bg-spinner").style.display ="none";
           document.getElementById('age2').value='';
           swal("Opsss !","Age only between 18 and 50 years old","info");
           return false;
       }
   
       else if(email2 == ""){
        document.getElementById("bg-spinner").style.display ="none";
           swal("Opsss !","Email field cannot be empty.","error");
           return false;
       }
   
       else if(!(validateEmail2(email2))){
        document.getElementById("bg-spinner").style.display ="none";
           document.getElementById('email2').value='';
           swal("Opsss !","Put a valid email address.","error");
           return false;
       }
   
       else if(phone2 == ""){
        document.getElementById("bg-spinner").style.display ="none";
           swal("Opsss !","Phone field cannot be empty.","error");
           return false;
       }
   
       else if(experience2 == ""){
        document.getElementById("bg-spinner").style.display ="none";
           swal("Opsss !","Experience field cannot be empty.","error");
           return false;
       }
       
       else if(skills2 == ""){
        document.getElementById("bg-spinner").style.display ="none";
           swal("Opsss !","Skills field cannot be empty.","error");
           return false;
       }
   
       else if(file2 == ""){
        document.getElementById("bg-spinner").style.display ="none";
           swal("Opsss !","File field cannot be empty.","error");
           return false;
       }
   
       else{
           return true;
       }
   }
   
   
   // c) Fullstack form
   
   function validateEmail3(email3){
       const regex =  /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
       return regex.test(email3);
   }
   function validateForm3(){
       const name3 = document.getElementById("name3").value;
       const age3 = document.getElementById("age3").value;
       const phone3 = document.getElementById("phone3").value;
       const email3 = document.getElementById("email3").value;
       const address3 = document.getElementById("address3").value;
       const experience3 = document.getElementById("experience3").value;
       const skills3 = document.getElementById("skills3").value;
       const file3 = document.getElementById("file3").value;
   
       if(name3 == ""){
        document.getElementById("bg-spinner").style.display ="none";
           swal("Opsss !","Name field cannot be empty.","error");
           return false;
       }
   
       else if(name3 == name3.toUpperCase()){
           document.getElementById("name3").value=" ";
           swal("Opsss !","Name field cannot be UPPERCASE.","info");
           return false;
       }
   
       else if(name3.split(' ').length < 2){
        document.getElementById("bg-spinner").style.display ="none";
           swal("Opsss !","Your fullname is REQUIRED","info");
           return false;
       }
   
       else if(age3 == ""){
        document.getElementById("bg-spinner").style.display ="none";
           swal("Opsss !","Age field cannot be empty.","error");
           return false;
       }
   
       else if((age3 < 18) || (age3 > 50)){
        document.getElementById("bg-spinner").style.display ="none";
           document.getElementById('age3').value='';
           swal("Opsss !","Age only between 18 and 50 years old","info");
           return false;
       }
   
       else if(email3 == ""){
        document.getElementById("bg-spinner").style.display ="none";
           swal("Opsss !","Email field cannot be empty.","error");
           return false;
       }
   
       else if(!(validateEmail3(email3))){
        document.getElementById("bg-spinner").style.display ="none";
           document.getElementById('email3').value='';
           swal("Opsss !","Put a valid email address.","error");
           return false;
       }
   
       else if(phone3 == ""){
        document.getElementById("bg-spinner").style.display ="none";
           swal("Opsss !","Phone field cannot be empty.","error");
           return false;
       }
   
       else if(experience3 == ""){
        document.getElementById("bg-spinner").style.display ="none";
           swal("Opsss !","Experience field cannot be empty.","error");
           return false;
       }
       
       else if(skills3 == ""){
        document.getElementById("bg-spinner").style.display ="none";
           swal("Opsss !","Skills field cannot be empty.","error");
           return false;
       }
   
       else if(file3 == ""){
        document.getElementById("bg-spinner").style.display ="none";
           swal("Opsss !","File field cannot be empty.","error");
           return false;
       }
   
       else{
           return true;
       }
       
   }
   
   
   // c) Intern form
   
   function validateEmail4(email4){
    const regex =  /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email4);
}
function validateForm4(){
    const name4 = document.getElementById("name4").value;
    const age4 = document.getElementById("age4").value;
    const phone4 = document.getElementById("phone4").value;
    const email4 = document.getElementById("email4").value;
    const address4 = document.getElementById("address4").value;
    const experience4 = document.getElementById("experience4").value;
    const skills4 = document.getElementById("skills4").value;
    const file4 = document.getElementById("file4").value;

    if(name4 == ""){
     document.getElementById("bg-spinner").style.display ="none";
        swal("Opsss !","Name field cannot be empty.","error");
        return false;
    }

    else if(name4 == name4.toUpperCase()){
        document.getElementById("name4").value=" ";
        swal("Opsss !","Name field cannot be UPPERCASE.","info");
        return false;
    }

    else if(name4.split(' ').length < 2){
     document.getElementById("bg-spinner").style.display ="none";
        swal("Opsss !","Your fullname is REQUIRED","info");
        return false;
    }

    else if(age4 == ""){
     document.getElementById("bg-spinner").style.display ="none";
        swal("Opsss !","Age field cannot be empty.","error");
        return false;
    }

    else if((age4 < 18) || (age4 > 50)){
     document.getElementById("bg-spinner").style.display ="none";
        document.getElementById('age4').value='';
        swal("Opsss !","Age only between 18 and 50 years old","info");
        return false;
    }

    else if(email4 == ""){
     document.getElementById("bg-spinner").style.display ="none";
        swal("Opsss !","Email field cannot be empty.","error");
        return false;
    }

    else if(!(validateEmail4(email4))){
     document.getElementById("bg-spinner").style.display ="none";
        document.getElementById('email4').value='';
        swal("Opsss !","Put a valid email address.","error");
        return false;
    }

    else if(phone4 == ""){
     document.getElementById("bg-spinner").style.display ="none";
        swal("Opsss !","Phone field cannot be empty.","error");
        return false;
    }

    else if(experience4 == ""){
     document.getElementById("bg-spinner").style.display ="none";
        swal("Opsss !","Experience field cannot be empty.","error");
        return false;
    }
    
    else if(skills4 == ""){
     document.getElementById("bg-spinner").style.display ="none";
        swal("Opsss !","Skills field cannot be empty.","error");
        return false;
    }

    else if(file4 == ""){
     document.getElementById("bg-spinner").style.display ="none";
        swal("Opsss !","File field cannot be empty.","error");
        return false;
    }

    else{
        return true;
    }
    
}

   
   
   // ) Maximum size of  allowed uploadable file
   $(document).ready(function(){
   
       $("#file,#file2,#file3,#file4,#file5").bind('change', function(){
       var a = (this.files[0].size);
       if(a > 2 * 1048576){
           swal("Attention !", "Maximum allowed size is 2mb.","info");
           this.value = "";
       }
       });
   });
   
   
   // 4) Allow only letters in NAME
   
   $(".name").keyup(function(){
   
       if(!/^[a-zA-Z _]*$/.test(this.value)){
           this.value = this.value.split(/[^a-zA-Z _]/).join('');
       }
   });

   // 5) function that allows only two white space in the NAME input

   $(".name").on("keydown",function(){

    var $this = $(this);
    $(this).val($this.val().replace(/(\s{2,}) | [^a-zA-Z0-9_']/g,   ' ').replace(/^\s*/, ''));



   });


   // 6) Prevent starting with space in all inputs (including textarea)

   $("input[type='text'], input[type='tel'], textarea").on("keypress",function(e){
        if(e.which === 32 && !this.value.length){
             e.preventDefault();
            }
   });

   // 7) Allow only numbers in AGE

   $(".age").keyup(function(){
    if(!/^[0-9]*$/.test(this.value)){
       this.value = this.value.split(/[^0-9]/).join(''); 
    }
   });


   //8) Limiting the AGE INPUT to two,if age is greater than 50 auto clear

   $(".age").keyup(function(){
    if((this.value) > 50){
        this.value = '';
    }

   });



   //9) Prevent starting age by zero in AGE field
$(".age").on("input",function(){
    if(/^0/.test(this.value)){
        this.value = this.value.replace(/^0/, "");
    }

});

   //10) Script to LOWERCASE input email

   $(document).ready(function(){
    $(".email").keyup(function(){
        this.value = this.value.toLowerCase();

    });
   });