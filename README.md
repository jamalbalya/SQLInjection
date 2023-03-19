# SQLInjection
Code for check SQL injection


In this code, we first create a new instance of the SQLMap class from the sqlmap library. We then set the target URL of the web application that we want to test for SQL injection vulnerabilities.

Next, we use the scan() method of the SQLMap class to check for SQL injection vulnerabilities in the target URL. The scan() method returns a dictionary that contains information about the vulnerabilities found, 
including the severity of the vulnerability and the type of vulnerability.

Finally, we print the result of the scan to the console using the print() function.

Note that the sqlmap library is a powerful tool that should only be used for ethical and legitimate purposes. 
It is important to obtain the necessary permissions and authorizations before testing any web application for SQL injection vulnerabilities. 
Additionally, the code above is just an example, and more sophisticated testing may be required to identify and mitigate SQL injection vulnerabilities.
