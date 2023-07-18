import urllib3

words = ['apple', 'banana', 'cheese']
results = {}

for word in words:
    url = "http://www.example.com/look.php?w=" + word
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    result = response.data.decode('utf-8')
    results[word] = result

# Write results to a text file
with open('results.txt', 'w') as file:
    for word, result in results.items():
        file.write(f"Word: {word}\n")
        file.write(f"Result: {result}\n\n")

print("Results written to 'results.txt'")
