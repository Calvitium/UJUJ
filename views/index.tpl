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
	<form action="/index" method="get">
		<table>
			<tr>
				<td>
					Name of the company:
				</td>
				<td>
					<input type = "text" name="name">
				</td>
			</tr>

			<tr>
				<td>
					From:
				</td>
				<td>
					<input type = "text" name="yearFrom">
				</td>
			</tr>
			<tr>
				<td>
					To:
				</td>
				<td>
					<input type = "text" name="yearTo">
				</td>
			</tr>


		         </table>
			<input value="Show the rating" type="submit">

    </form>
			
			

<br><br>
    <form action="/logout" method="get">
        <input type="submit" value="Sign Out">
    </form>

<body style = "background: url(https://image.freepik.com/free-vector/orange-abstarct-background-with-lines_1123-45.jpg); background-size: cover; no-repeat">
</body>


	
	