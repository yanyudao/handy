import ssl
import socket

hostname = 'ldap.example.com'
port = 636

context = ssl.create_default_context()
with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        cert = ssock.getpeercert(binary_form=True)
        with open('ldap.crt', 'wb') as f:
            f.write(cert)
