<!DOCTYPE html>
<html>
<body>
	<h1>Google Maps API Program</h1>
	<p>This Python program uses the Google Maps API to search for businesses within a given radius of a set of addresses. The program outputs a list of businesses with their name, website, formatted address, and rating. The results are saved to an Excel file.</p>
less
Copy code
<h2>Dependencies</h2>
<ul>
	<li>time</li>
	<li>requests</li>
	<li>json</li>
	<li>googlemaps</li>
	<li>bs4</li>
	<li>numpy</li>
	<li>pandas</li>
</ul>

<h2>Installation</h2>
<p>To use this program, you will need to have a Google Maps API key. Replace the value of the <code>API_KEY</code> variable with your own key.</p>

<p>You will also need an input file named <code>address.xlsx</code>, which should contain a list of addresses to search. The file should have two columns: <code>Address</code> and <code>Place ID</code>. The <code>Place ID</code> column should be left blank, as it will be populated by the program.</p>

<p>Finally, you will need to install the required dependencies. You can use pip to install the dependencies:</p>

<pre><code>pip install -r requirements.txt</code></pre>

<h2>Usage</h2>
<p>To run the program, simply execute the Python file:</p>

<pre><code>python google_maps.py</code></pre>

<p>The program will output the progress of the search and the final results to the console. The results will also be saved to a file named after the search string, in this case, <code>builder.xlsx</code>.</p>

</body>
</html>
