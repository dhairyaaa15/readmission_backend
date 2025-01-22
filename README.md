 <h2>Features</h2>
    <ul>
        <li>Predicts whether a patient will be readmitted to the hospital.</li>
        <li>Provides probability scores for the prediction.</li>
        <li>Accepts JSON input and returns results in JSON format.</li>
        <li>CORS enabled for cross-origin requests.</li>
    </ul>
<h2>Requirements</h2>
<h3>Python Version</h3>
<p>Python 3.7+</p>
<h3>Python Dependencies</h3>
<p>The required Python packages are listed in the <code>requirements.txt</code> file. Install them using pip:</p>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>Sample <code>requirements.txt</code></h3>
<pre>
<code>
Flask
Flask-Cors
joblib
pandas
scikit-learn
</code>
</pre>

<h2>Usage</h2>

<h3>1. Clone the Repository</h3>

<p>Clone the repository to your local system:</p>
<pre><code>git clone &lt;repository_url&gt;</code></pre>
<h3>2. Set Up Virtual Environment</h3>
<p>Create and activate a virtual environment:</p>
<pre><code>python -m venv env</code></pre>

<h3>3. Install Dependencies</h3>
<p>Install the required packages:</p>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>4. Add Your Model</h3>
<p>Place the trained model file (<code>logisticmodel.sav</code>) in the project directory.</p>

<h3>5. Run the Application</h3>
<p>Start the Flask application:</p>
<pre><code>python app.py</code></pre>
<p>The application will be available at <code>http://0.0.0.0:5000/</code>.</p>
