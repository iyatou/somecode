function check(){
	if(document.form1.username.value=="")
		
{
alert("�����û����Ƿ�Ϊ�գ�");
return false;
}

	  if(document.form1.myname.value=="")
		  {
alert("�ǳƲ���Ϊ��");

		     return false
;}
	if(document.form1.password.value=="")
		  {alert("�������������Ƿ�Ϊ�գ�");

		     return false;
}

	  if(document.form1.password.value.length<6)
		  {
alert("�������볤��С��6��");

		     return false
;}
	  if(document.form1.password.value!=document.form1.repassword.value)
		  {
alert("�������벻һ��");

		     return false
;
}
}


}