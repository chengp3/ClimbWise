# climbwise

A site coded from scratch to include climbing data scraped from Mountain Project. 

Mountain Project tracks climbing routes and the climbers that climb them around the world. Route data includes location, difficulty, type (ice, rock, bouldering, trad, sport, etc.), along with popularity ratings and other miscellaneous information. As a climber, you can tick the routes off as you climb them.

My goal was to integrate the tick data into an analyzed format for climbers to understand how they climb. Are they climbing harder grades over time? Are they overcommitting time to a certain type of climb while ignoring others? Etc.

Unfortunately Mountain Project was bought by private investors, and their public API promptly shut down (who's bitter? not me). So I manually scraped the entire website into my own database. 

# The framework

Route data (SQL) -> Tick data (also SQL) -> Python -> Flask -> HTML/CSS/Bootstrap/Chartjs

# The site

The site has capability to run anyone's tick data but MP has user data download throttled. So this is short circuited at the moment. Click through to see my buddy's climbing charts...

<a href="pcheng3.pythonanywhere.com">Here</a>
