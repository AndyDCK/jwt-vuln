# Flask JWT Vulnerable - Exploitation de failles classiques JWT

Ce projet Flask simule une application vulnérable aux failles **JWT** couramment rencontrées en CTF :

- Acceptation de àlg: none`(aucune signature requise)
- Signature HMAC avec **clé faible** (`"secret"`)

---

## Objectif pédagogique

Apprendre à :
- Forger un token JWT sans signature (`alg: none`)
- Modifier un token dans les cookies du navigateur
- Utiliser `pyjwt` pour exploiter ou sécuriser une application

---
## Lancer l'application
### Build du docker
```bash
docker build -t flask-jwt-vuln .
docker run -p 8080:80 flask-jwt-vuln
```
Accessible sur `http://localhost:8080`

Objectif : Réussir à accéder à `http://localhost:8080/dashboard` en tant qu'admin
