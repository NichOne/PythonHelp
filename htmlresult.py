import urllib3

words = ['apple', 'banana', 'cheese']
results = {}

# Create an HTTP connection pool
http = urllib3.PoolManager()

for word in words:
    url = "http://www.example.com/look.php?w=" + word
    response = http.request('GET', url)
    result = response.data.decode('utf-8')
    results[word] = result

# Write results to an HTML file
with open('results.html', 'w') as file:
    file.write("<html>\n")
    file.write("<body>\n")
    for word, result in results.items():
        file.write(f"<h3>Word: {word}</h3>\n")
        file.write(f"<pre>{result}</pre>\n")
    file.write("</body>\n")
    file.write("</html>\n")

print("Results written to 'results.html'")