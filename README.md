# 🚀 Startup App - Automatisation du Déploiement

## 📋 Contexte
Migration d'un déploiement manuel FTP vers un pipeline CI/CD automatisé.

**Problème client :** Déploiement manuel via FTP, 2h par mise en prod, instable.  
**Solution apportée :** Conteneurisation Docker + Pipeline CI/CD GitHub Actions.

## 🛠️ Stack Technique
- **Langage :** Python / Flask
- **Conteneurisation :** Docker
- **CI/CD :** GitHub Actions
- **VPS :** Linux Ubuntu

## 📁 Structure du projet
```
startup-app1/
├── app.py              # Application Flask
├── Dockerfile          # Conteneurisation
├── requirements.txt    # Dépendances Python
├── .github/
│   └── workflows/
│       └── deploy.yml  # Pipeline CI/CD
└── README.md
```

## ⚙️ Installation locale
```bash
git clone git@github.com:Nguessdevops/startup-app1.git
cd startup-app1
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

## 🐳 Lancer avec Docker
```bash
docker build -t startup-app .
docker run -d -p 5000:5000 startup-app
```

## 🔄 Pipeline CI/CD
A chaque `git push` sur la branche `main` :
1. GitHub Actions se déclenche automatiquement
2. Construction de l'image Docker
3. Lancement des tests
4. Déploiement automatique

## 📈 Résultats
| Avant | Après |
|-------|-------|
| Déploiement FTP manuel | Déploiement automatique |
| 2h par mise en prod | 5 minutes |
| Instable, casse souvent | Pipeline testé et fiable |

## 👨‍💻 Auteur
**Nguessdevops** - DevOps Engineer
