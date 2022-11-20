<!DOCTYPE html>
<html>
<head>
	<title>Data Mobil</title>
</head>
<style>
body {
	background-image: url(css/bggdb.jpg);
	background-color: #0F0;
	background-size:95%;
}
.roto{
	margin-top:80px;
	}
.roto1{
	margin-left:465px;
	}
</style>
<body>
<font color="#000000">
<h3>Selamat Datang <font face="Comic Sans MS, cursive" size="+2"> Kopi Latte's' Team</font>! || 
	<br><a href=#> Logout                   ||</a></h3>
    
<div class="roto" align="center" >
	<header>
		<h1><b>Data Stock Mobil</b></h1>
	</header>
    </div>
    <div class="roto1">
	<nav>
		<a href=#>[+] Tambah Data</a>
	</nav>
    </div>
    <div align="center">
	<br>
	<table border="1" cellpadding="8">
		<tr>	
			<td><b>ID</b></td>
			<td><b>BRAND</b></td>
			<td><b>MODEL</b></td>
			<td><b>PRICE</b></td>
		</tr>
    %import sqlite3
    %conn = sqlite3.connect('cars51.db')
    %c = conn.cursor()
    %b = c.execute("SELECT * FROM cars51")
    
    %result = c.fetchall()
		%for row in result:
  			<tr>
		
  		%for col in row:
			<td>{{col}}</td>
  		%end
  		%end
  			</tr>
	%end
	</table>
    </div> 
    <div class="roto1">
    
	<p>Jumlah Jenis Mobil :  </p> 
    
   </div>
   </font>
</body>
</html>