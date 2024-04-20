<body>
  <header>
    <h1>Smart AI Chatbot for FAQ Search</h1>
  </header>
  <div class="container">
    <h2>Features</h2>
    <ul class="feature-list">
      <li><strong>Code Search:</strong> The chatbot can search through a dataset of FAQ snippets and return relevant results based on user queries.</li>
      <li><strong>Natural Language Understanding:</strong> It understands user queries in natural language and retrieves the most appropriate responses.</li>
      <li><strong>Scalable:</strong> The chatbot is built using Flask, making it easy to deploy and scale for production environments.</li>
    </ul>
    <h2>Full Procedure</h2>
    <ul class="feature-list">
      <li><strong>Prepare search data (once)</strong>
        <ol>
          <li>Collect: FAQ document's in the data folder are given</li>
          <li>Chunk: Documents are split into short, mostly self-contained sections to be embedded</li>
          <li>Embed: Each section is embedded with the OpenAI API</li>
          <li>Store: Embeddings are saved (for large datasets, use a vector database)</li>
        </ol>
      </li>
    </ul>
    <h2>Why Search Is Better Than Fine-Tuning</h2>
    <p>GPT has two methods for acquiring knowledge:</p>
    <p>By using model weights, the model may be adjusted on a training set. Through the use of model inputs, or inserting the information into an input message</p>
    <p>Fine-tuning may seem like the most sensible choice after all, GPT acquired all of its other information through data training but we don't usually advise using it to impart model expertise. Fine-tuning is less effective for factual recollection and is better suited for teaching specific activities or styles.</p>
    <p>Model weights can be compared to long-term memory. Fine-tuning a model is similar to preparing for a test that is just a week away. When the test day comes, the model can misremember information it has never read or forget specifics.</p>
    <p>Message inputs on the other hand resemble short-term memory. Integrating information into a message is similar to taking an open-book test. The model is more likely to get the right answers if it has notes.</p>
    <h2>Model Maximum Text Length</h2>
    <table>
      <tr>
        <th>Model</th>
        <th>Maximum Text Length</th>
      </tr>
      <tr>
        <td>gpt-3.5-turbo</td>
        <td>4,096 tokens (~5 pages)</td>
      </tr>
      <tr>
        <td>gpt-4</td>
        <td>8,192 tokens (~10 pages)</td>
      </tr>
      <tr>
        <td>gpt-4-32k</td>
        <td>32,768 tokens (~40 pages)</td>
      </tr>
    </table>
    <h2>Usage</h2>
    <ul class="feature-list">
      <li><strong>To run the chatbot locally, follow these steps:</strong>
        <ol>
<li>Clone the repository to your local machine.</li>
<li>Install the required dependencies listed in requirements.txt using pip install -r requirements.txt.</li>
<li>Set up your OpenAI API key in the openai.api_key variable.</li>
<li>Run the Flask server by executing python app.py in your terminal.</li>
<li>Access the chatbot interface by navigating to http://localhost:5000/test in your web browser.</li>
    <h2>Examples</h2>
    <ul class="feature-list">
      <li>"how to make a normal account and what permission will i have?"</li>
      <li>"how to access admin detail?"</li>
      <li>"how much data is allowed to save?"</li>
    </ul>
    <h2>Contributions</h2>
    <p>Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request..</p>
  </div>
</body>
