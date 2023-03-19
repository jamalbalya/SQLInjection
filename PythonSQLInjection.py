import sqlmap

# Create a new sqlmap instance
sqlmap_instance = sqlmap.SQLMap()

# Set the target URL
target_url = "http://example.com/login.php"

# Check for SQL injection vulnerabilities
result = sqlmap_instance.scan(target_url)

# Print the result
print(result)
