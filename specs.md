# life Blog Specification
<p>I have tried to make the specifications as easy to read and understand.</p>
<p>Last modified: <b>10/5/2020</b></p>
<p>Version : python3.6</p>


## TABLE OF CONTENTS
<ul>
<li>Introduction</li>
<li>System Overview</li>
<li>Usage</li>
<li>Future Directions and open Questions</li>
</ul>

<h2> 1. Introduction </h2><hr>
<ol>
<li><b> Scope</b></li>
<p>This is a Flask application where you can create and share your opinions and other users can read and comment on them as well as display random quotes to inspire your users.</p>

<li><b> Goals</b></li>
<ul>
<li>Gives information on a particular pitch</li>
<li>Easily accessible</li>
<li>You can like, dislike as well as comment on a pitch.</li>
<ul>

<li><b> Goals for implementation</b></li>
<pre>
<code>This app must be secure in all environments. We do this by using the SECRET_API_KEY to avoid explicity as well as forgery.</code>
</pre>
</ol>

<h2> 2. System Overview </h2><hr>
<p>This app follows the following steps to ensure it outputs the latest pitch in different categories </p>
<ol>
<li><b> How the System Works</b></li>
<pre><code> 
<b>Sign up or login:</b>
A new user will be prompted to register following the instructions on the form. 
They can also sign in if they already have an account.
Once they login they can see their profile and update it as well.

<b>Creating and Updating data:</b>
Periodically, the Pitch app gets data from its input forms. It has input fields where users can fill.
The data is then published when the user clicks the submit data.
<code></code>
</ul>
<h2> 3. Usage </h2><hr>
<ol type ='a'>
<li><b> Requirements</b></li>
<p>Fair or good Internet Connection.</p>
<p>You can choose to use the live link provided in the README. Click it and follow instructions given on readme.</p>
<p>The app should work fine but if it doesn't feel free to raise a compability issue </p>
</ol>
<pre>
<code>** Disclaimer **
The data contained is not filtered by contents, hence the pitch app won't be responsible for any rude or explicit wordings or images.
</code>
</pre>

<h2> 4. Future Directions and Open Questions </h2><hr>
<p>NOTE : this app has been designed and implemented using Flask. It also allows flexibility for different uses.</p>
<p>If you have any questions feel free to <a href ='nimz69509@gmail.com'>Email me</a>. Your suggestions are welcomed.</p>