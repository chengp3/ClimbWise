# climbwise

A site coded from scratch to include climbing data scraped from Mountain Project. 

Mountain Project tracks climbing routes and the climbers that climb them around the world. Route data includes location, difficulty, type (ice, rock, bouldering, trad, sport, etc.), along with popularity ratings and other miscellaneous information. As a climber, you can tick the routes off as you climb them.

My goal was to integrate the tick data into an analyzed format for climbers to understand how they climb. Are they climbing harder grades over time? Are they overcommitting time to a certain type of climb while ignoring others? Etc.

Unfortunately Mountain Project was bought by private investors, and their public API promptly shut down (who's bitter? not me). So I manually scraped the entire website into my own database. 

# The framework

Route data (SQL) -> Tick data (also SQL) -> Python -> Flask -> HTML/CSS/Bootstrap/Chartjs

# The site

pcheng3.pythonanywhere.com

Even accessing tick data on MP is throttled heavily and takes a long minute. So currently example tick data is stored in its own SQLite table. Don't bother with copying a ticklist URL into the splash page. Just click Submit and it will run the numbers from my buddy Ryan...
