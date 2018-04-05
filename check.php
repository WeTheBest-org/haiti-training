
<?php
$db=pg_connect('dbname=db_projet user=postgres password=cnigs port=5432');
 if (isset($_POST['Submit'])){
  $username =pg_escape_string($_POST['username']);
   
   $password=md5($_POST['password']);
try{
 $r=pg_exec ($db , "SELECT username,password,acces_level FROM login_detail WHERE username='$username' and password='$password' ");
  for ($i=0; $i<pg_numrows($r); $i++) {
  $l=pg_fetch_array($r,$i); echo "<br />";
   }

	
	if($l){  
 
  session_start();
  $access_level=$l['acces_level'];
 
  $_SESSION['acces_level']=$access_level;
  if ($access_level==0){
   header("Location:recherche.phtml");
   }
   
  else if($access_level==1|| $access_level==2)  {
   header("Location:map_default.phtml");
   }
   if ($access_level==3){
   header("Location:recherche1.phtml");
   }
   
  }
  
	else{
  header("Location:check.phtml?err=1");
  }
	
	 }
	 catch(Exception $e){
  die("Database error: ".$e->getMessage());
 }
 
} 
  
?>



<html>
<head>
<link rel="stylesheet" href="php_checkbox.css" />
<title>initiative_connexion</title>
<style>
.textfield{
 opacity:0.7;
}
.container{
 margin:0px auto;
 width:450px;
 height:250px;
 text-align:center;
 background-color:#F7F7F7;
 border:1px solid #BFBFBF;
 box-shadow:0px 0px 3px #BFBFBF;
}

</style>
</head>
<body>

<div class="container"> 
<form action="check.phtml" method="post">
<h2>Page de connexion</h2>
<table style="margin:0px auto">
<tr>
<td>Identifiant: </td><td width="50px"><input class="textfield" type="text" name="username"/></td>
</tr>
<tr>
<td>Mot de passe: </td><td width="50px"><input class="textfield" type="password" name="password"/></td>
</tr>
<tr><td></td><td width="50px"><span style="color:#E21111;font-size:12px;">
<?php // To display Error messages
if(isset($_GET['err'])){
if ($_GET['err']==1){
echo "L'indentifiant ou le mot de passe est incorrect";}
else if($_GET['err']==2){
echo "Veuillez vous connecter..";}
else if ($_GET['err']==5){
echo "Vous essayez d'acceder a une page non-autorisée, connectez-vous d'abord";
}
}

?>





</span></td></tr>
</table>

<input type="submit" value="Valider" name="Submit"  />
</form>


</div>
</body>
</html>