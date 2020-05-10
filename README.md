# LIFE BLOG

## Description
This is a Flask application where you can create and share your opinions and other users can read and comment on them as well as display random quotes to inspire your users. 
## By: Maureen Wairimu

## User Story
<ul>
<li>Users can view the blog posts on the site.</li>
<li>Users can comment on blog posts.</li>
<li>Users can view the most recent posts.</li>
<li>Users recieve an email alert when a new post is made by joining a subscription.</li>
<li>Users can see random quotes on the site.</li>
<li>Users can create a blog from the application.</li>
<li>Users can delete comments that I find insulting or degrading.</li>
<li>Users can sign in to the blog, update or delete blogs they have created.</li>
</ul>

### Brief Webpage Overview.
<ul>
<li>Below is the landing page once the web browser is loaded</li>
<img src="/home.jpg" alt="Pitch landing page" width="1000"/>
</ul>

### Live link : 

## Setup Instructions
<ol>
<li>Clone or download the repository <code> https://github.com/maureen28/Blog.git</code> </li>
<li>Create a virtual environment aand activate it.
<pre>
<code>
pip install virtualenv
source virtual/bin/activate
</code></pre>
</li>
<li>Install all the requirements <code> pip install -r requirements.txt</code></li>
<li>Go to config.py and set the SQLALCHEMY_DATABASE_URI to your own, you may use Postgres or any other SQL database client.
</li>
<li>Create a file in your root directory and store a generated SECRET key <code>export SECRET_KEY="<your-key>"</code></li>
<li>Run <code>python3 manage.py server</code></li>
<li>Run test at <code>python3 manage.py test</code></li>
</ol>


## Technology & Dependency
<ol>
<li>python3.6</li>
<li>Pip & pyperclip</li>
<li>CSS(Bootstrap, FontAwesome)</li>
<li>Flask Framework</li>
<li>PostgreSQL</li>
</ol>


## Behavior Driven Deveopment
<table>
<tr>
<th>Behaviour</th>
<th>Input</th>
<th>Output</th>
</tr>
<tr>
<td><strong>User login</strong></td>
<td>User enters email address and password</td>
<td>User is logged into the system</td>
</tr>
<tr>
<td><strong>Register as a new user</strong></td>
<td>A form containing username, email, password and confirm password </td>
<td>User is registered</td>
</tr>
<tr>
<td><strong>Adds a new pitch</strong></td>
<td>A form containing input fields for heading, pitch text and comment</td>
<td>New pitch is added.</td>
</tr>
</table>

### Known Bugs
If you find a bug please feel free to alert me.
To fix the bug:
<ul list-style-type=circle;>
<li>Fork the repository</li>
<li>Create a new branch(git branch my-contribution)</li>
<li>Make the changes, then (git add) to add changes</li>
<li>Commit the changes you have made(git commit -m"Fix bug") </li>
<li>Push changes made and click pull request so that I can access the changes made.</li>
</ul>

## Contact Information

To get in touch E-MAIL me on nimz69509@gmail.com

## License

MIT License
<b>Copyright (c) 2020 maureen28<b>