<!DOCTYPE html>
<html >
<head>
<style>
body {
	background-image: url(css/b2.jpg);
	background-color: #0F0;
	background-size:95%;
}
</style>
  <meta charset="UTF-8">
  <title>Kopi Latte</title>
  
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">

  
      <link rel="stylesheet" href="css/style.css">

  
</head>

<body>
  <font face="La Rapidita"><h1>
  Data Stock Mobil
</h1>
<p>
  (Showroom Krian Tirto Agung)
</p></font>
<main>
  <table>
    <thead>
      <tr>
        <th width="65px">
          <center>ID</center>
        </th>
        <th>
         <center> BRAND</center>
        </th>
        <th>
          <center>MODEL</center>
        </th>
        <th>
		  <center>PRICE</center>
        </th>
      </tr>
    </thead>
    <tfoot>
      <tr>
        <th colspan='5'>
          <center>Tahun: 2023</center>
        </th>
      </tr>
    </tfoot>
    <tbody>
      <tr>
        %import sqlite3
    %conn = sqlite3.connect('cars515.db')
    %c = conn.cursor()
    %b = c.execute("SELECT * FROM cars515")
    
    %result = c.fetchall()
		%for row in result:
  			<tr>
		
  		%for col in row:
			<td>{{col}}</td>            
  		%end
  		%end
      </tr>
      %end
    </tbody>
  </table>
  <div class='detail'>
    <div class='detail-container'>
      <dl>
        <dt>
          Provider Name
        </dt>
        <dd>
          John Doe
        </dd>
        <dt>
          E-mail
        </dt>
        <dd>
          email@example.com
        </dd>
        <dt>
          City
        </dt>
        <dd>
          Detroit
        </dd>
        <dt>
          Phone-Number
        </dt>
        <dd>
          555-555-5555
        </dd>
        <dt>
          Last Update
        </dt>
        <dd>
          Jun 20 2014
        </dd>
        <dt>
          Notes
        </dt>
        <dd>
          Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Donec odio. Quisque volutpat mattis eros. Nullam malesuada erat ut turpis. Suspendisse urna nibh, viverra non, semper suscipit, posuere a, pede.
        </dd>
      </dl>
    </div>
    <div class='detail-nav'>
      <button class='close'>
        Close
      </button>
    </div>
  </div>
</main>
  <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>

    <script src="js/index.js"></script>

</body>
</html>
