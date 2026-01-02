# Guide d'utilisation pour Overleaf

## Comment copier-coller ce document dans Overleaf

### Étape 1 : Préparer le fichier
1. Ouvrez le fichier `document.tex` ou `improved_document.tex`
2. Copiez **tout le contenu** du fichier (Ctrl+A puis Ctrl+C)

### Étape 2 : Créer un nouveau projet sur Overleaf
1. Allez sur [www.overleaf.com](https://www.overleaf.com)
2. Connectez-vous à votre compte
3. Cliquez sur "New Project" (Nouveau projet)
4. Sélectionnez "Blank Project" (Projet vide)
5. Donnez un nom à votre projet, par exemple "Rapport Lean Manufacturing"

### Étape 3 : Coller le code
1. Overleaf créera automatiquement un fichier `main.tex`
2. **Supprimez tout le contenu** du fichier `main.tex`
3. **Collez** le contenu copié de `document.tex`
4. Cliquez sur "Recompile" en haut

### Étape 4 : Vérifier la compilation
- Le document devrait compiler sans erreur
- Vous verrez votre document formaté dans le panneau de droite
- Si vous voyez des erreurs, vérifiez que vous avez bien copié tout le contenu

## Ajouter des images

Pour ajouter vos propres images :

1. Cliquez sur l'icône "Upload" (Télécharger) dans Overleaf
2. Sélectionnez vos fichiers image (PNG, JPG, PDF)
3. Dans le code LaTeX, remplacez les placeholders par :
   ```latex
   \includegraphics[width=0.3\textwidth]{nom-de-votre-image.png}
   ```

## Personnalisation

### Changer les couleurs
Trouvez la section `% CUSTOM COLORS` et modifiez les valeurs RGB :
```latex
\definecolor{maincolor}{RGB}{0,82,147}  % Couleur principale
\definecolor{secondcolor}{RGB}{0,120,190}  % Couleur secondaire
```

### Modifier les informations personnelles
Cherchez la section "TITLE PAGE" et modifiez :
- Nom et prénom
- Année scolaire
- Encadrant
- Niveau, filière, etc.

### Ajouter du contenu
- Utilisez `\section{Titre}` pour ajouter une nouvelle section
- Utilisez `\subsection{Titre}` pour une sous-section
- Utilisez `\begin{itemize}...\end{itemize}` pour des listes à puces

## Exporter le PDF

1. Après compilation réussie, cliquez sur le bouton "Download PDF"
2. Le fichier PDF sera téléchargé sur votre ordinateur
3. Vous pouvez maintenant l'imprimer ou le partager

## Conseils

- **Sauvegarde automatique** : Overleaf sauvegarde automatiquement vos modifications
- **Historique** : Vous pouvez voir l'historique des versions dans le menu "History"
- **Partage** : Utilisez le bouton "Share" pour partager avec d'autres personnes
- **Compilation** : Si le document ne compile pas, vérifiez les messages d'erreur en cliquant sur l'icône d'alerte

## Support

Si vous rencontrez des problèmes :
1. Vérifiez que vous avez copié l'intégralité du fichier
2. Assurez-vous qu'il n'y a pas de caractères spéciaux mal encodés
3. Consultez la documentation Overleaf : [overleaf.com/learn](https://www.overleaf.com/learn)

## Résultat attendu

Votre document devrait avoir :
- ✓ Une page de titre professionnelle
- ✓ Une table des matières automatique
- ✓ Des sections bien formatées avec des couleurs
- ✓ Des tableaux professionnels avec des en-têtes colorés
- ✓ Des listes bien alignées
- ✓ Des marges adaptées au format A4
- ✓ Une numérotation des pages
- ✓ Des en-têtes et pieds de page

Bon travail !
