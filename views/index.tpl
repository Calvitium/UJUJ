% rebase('base.tpl', title='Python')
<div class="row">
	<div class="col-md-12">
	<h3>Welcome to RatingPlatform!</h3>
	User: {{loginName}}
	</div>
</div>

<h2>RatingFinder</h2>
<h3>Case 1: Analysis for the choosing company</h3>
<body>
	<form>
		<table>					
			<tr>
				<td>
					Name of the company:
				</td>
				<td>
					<input type = "text" name="">
				</td>
			</tr>

			<tr>
				<td>
					From:
				</td>
				<td>
					<input type = "text" name="">
				</td>
			</tr>
			<tr>
				<td>
					To:
				</td>
				<td>
					<input type = "text" name="">
				</td>
			</tr>

							
		         </table>						
			<form>
			<a href="/base"><input value="Show the rating" type="submit"></a></form>
			
			
			<h3>Go to Case 2: Analysis for the choosing company against the background of a given market</h3>	
			<form><a href="/action2"><input value="Go to the Case 2" type="submit"></a></form>
<br><br>
    <form action="/logout" method="get">
        <input type="submit" value="Sign Out">
    </form>
			<div class="downleft"><a href="logout.php">Sign Out</a></div>		

<body style = "background: url(https://image.freepik.com/free-vector/orange-abstarct-background-with-lines_1123-45.jpg); background-size: cover; no-repeat">
</body>


	
	