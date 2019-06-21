function check(){
	if(document.form1.username.value=="")
		
{
alert("请检查用户名是否为空！");
return false;
}

	  if(document.form1.myname.value=="")
		  {
alert("昵称不能为空");

		     return false
;}
	if(document.form1.password.value=="")
		  {alert("请检查您的密码是否为空！");

		     return false;
}

	  if(document.form1.password.value.length<6)
		  {
alert("您的密码长度小于6！");

		     return false
;}
	  if(document.form1.password.value!=document.form1.repassword.value)
		  {
alert("两次密码不一致");

		     return false
;
}
}


}