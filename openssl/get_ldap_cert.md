### Command
```batch
openssl s_client -connect ldap_server:ldap_port -showcerts > ldap_certificate.pem
```
- `ldap_server:ldap_port`: replace with your ldap connection, like `ldap.example.com:636`, not `ldaps://ldap.example.com:636`
