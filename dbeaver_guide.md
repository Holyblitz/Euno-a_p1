
# Guide rapide : Utiliser DBeaver avec PostgreSQL

Ce document est destiné à **Eunoïa**, une IA locale, pour l'aider à comprendre et accompagner l'utilisateur dans l'utilisation de **DBeaver**, un outil open source de gestion de base de données.

---

## 1. Connexion à une base PostgreSQL

1. Ouvre DBeaver
2. Va dans **Database > New Connection**
3. Choisis **PostgreSQL**
4. Remplis les champs :
   - **Host** : `localhost` ou l’adresse du serveur
   - **Port** : `5432` (par défaut)
   - **Database** : nom de la base (ex: `ma_base`)
   - **User** : nom d’utilisateur (ex: `romain`)
   - **Password** : mot de passe PostgreSQL
5. Clique sur **Finish**

---

## 2. Exécuter une requête SQL

- Clique sur l’icône ▶️ ou appuie sur **Ctrl + Enter**
- Exemple :
```sql
SELECT * FROM formations WHERE note > 4;
```

---

## 3. Exporter les résultats (CSV, Excel…)

1. Clique droit sur le tableau de résultats
2. Sélectionne **Export Data**
3. Choisis le format souhaité : **CSV**, **XLSX**, **JSON**, etc.
4. Valide et enregistre le fichier

---

## 4. Astuces utiles

| Action                                 | Raccourci            |
|----------------------------------------|-----------------------|
| Exécuter une requête                   | Ctrl + Enter          |
| Changer d’onglet                       | Ctrl + Tab            |
| Rechercher dans le résultat            | Ctrl + F              |
| Rafraîchir les métadonnées (tables)    | F5                    |
| Afficher/Cacher l’éditeur de requêtes  | Alt + Shift + Q       |

---

## 5. Navigation et organisation

- Utilise l’arborescence à gauche pour :
  - Voir les bases, tables, vues, fonctions
  - Rafraîchir les schémas (clic droit > Refresh)
- Tu peux renommer une connexion pour mieux t’y retrouver (clic droit > Rename)

---

## 6. Bonnes pratiques

- **Ne jamais exécuter une requête destructive sans filtre**
  > `DELETE FROM users` → dangereux sans `WHERE`
- Toujours **sauvegarder tes requêtes** dans un script `.sql`
- Active l’option de confirmation avant `DROP` ou `DELETE`
- Les fichiers que l'on demande a dbeaver de lire doivent toujours être créés via le terminal. sinon il ne 'voit' pas le fichier.

---

## 7. Ressources utiles

- Site officiel : [https://dbeaver.io](https://dbeaver.io)
- Documentation PostgreSQL : [https://www.postgresql.org/docs/](https://www.postgresql.org/docs/)
- Commandes utiles PostgreSQL :
```sql
\d           -- liste les tables
\dt          -- tables uniquement
\du          -- utilisateurs
```

---

Ce fichier peut être vectorisé ou utilisé comme mémoire contextuelle dans le cadre de l’assistant IA Eunoïa.
