import tkinter as tk
from tkinter import messagebox

class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface utilisateur")
        self.root.geometry("400x400")  # Augmenter la hauteur pour tenir compte du texte ajouté

        # Couleurs
        self.bg_color = "#f0f0f0"
        self.button_color = "#4CAF50"
        self.button_hover_color = "#45a049"

        # Création des widgets
        self.creer_widgets()

    def creer_widgets(self):
        # Titre
        self.titre_label = tk.Label(self.root, text="Pourquoi NoSQL est un Bon Choix pour un catalogue des produits?", font=("Helvetica", 14, "bold"), bg=self.bg_color)
        self.titre_label.pack(pady=10)

        # Texte
        texte = """Flexibilité du Schéma : La base de données NoSQL permet une modélisation flexible, idéale pour gérer les variations des attributs des produits.
        Évolutivité Horizontale : NoSQL offre une évolutivité sans effort pour gérer la croissance des données et du trafic.
        Performances : Les opérations de lecture et d'écriture rapides sont cruciales pour un catalogue de produits, ce que NoSQL assure.
        Modèle de Données Dénormalisé : Les données peuvent être dénormalisées pour améliorer les performances des requêtes, ce qui est mieux supporté par NoSQL par rapport aux SGBD SQL traditionnels."""
        self.texte_label = tk.Label(self.root, text=texte, wraplength=380, justify=tk.LEFT, bg=self.bg_color)
        self.texte_label.pack(pady=10)

        # Cadre principal
        self.cadre_principal = tk.Frame(self.root, bg=self.bg_color)
        self.cadre_principal.pack(expand=True, fill=tk.BOTH)

        # Bouton lié à la base de données
        self.bouton_bd = tk.Button(self.cadre_principal, text="Bouton lié à la base de données", bg=self.button_color, fg="white", relief=tk.FLAT, command=self.action_bouton_bd)
        self.bouton_bd.pack(pady=10)

        # Bouton besoins d'utilisateur
        self.bouton_besoins_utilisateur = tk.Button(self.cadre_principal, text="Bouton besoins d'utilisateur", bg=self.button_color, fg="white", relief=tk.FLAT, command=self.action_bouton_besoins_utilisateur)
        self.bouton_besoins_utilisateur.pack(pady=10)

        # Bouton démontrant l'utilisation des requêtes créées
        self.bouton_requetes = tk.Button(self.cadre_principal, text="Bouton démontrant l'utilisation des requêtes créées", bg=self.button_color, fg="white", relief=tk.FLAT, command=self.action_bouton_requetes)
        self.bouton_requetes.pack(pady=10)

    def action_bouton_bd(self):
        messagebox.showinfo("Bouton lié à la base de données", "Fonctionnalité en cours de développement.")

    def action_bouton_besoins_utilisateur(self):
        fenetre_besoins_utilisateur = tk.Toplevel(self.root)
        fenetre_besoins_utilisateur.title("Besoin Utilisateur")

        questions = [
            "Quels produits sont disponibles dans une catégorie spécifique ?",
            "Comment puis-je trouver les détails d'un produit spécifique ?",
            "Quels sont les produits les mieux notés dans chaque catégorie ?",
            "Comment puis-je voir tous les avis laissés pour un produit particulier ?",
            "Est-ce que je peux recevoir des notifications sur les promotions pour des produits qui m'intéressent ?",
            "Comment puis-je suivre ma commande et voir son statut actuel ?",
            "Y a-t-il une option pour filtrer les produits par prix ou par fournisseur ?",
            "Peut-on recommander des produits basés sur mes achats précédents ou sur ma navigation ?",
            "Comment puis-je mettre à jour mes informations de contact ou de paiement ?",
            "Quelle est la politique de retour pour les produits achetés ?",
            "Comment puis-je comparer plusieurs produits ?",
            "Peut-on voir la disponibilité des stocks pour un produit avant de passer commande ?",
            "Y a-t-il une limite à la quantité d'un produit que je peux commander ?",
            "Comment puis-je contacter le service client pour une question ou un problème ?",
            "Y a-t-il des avis ou des évaluations disponibles pour les fournisseurs ?"
        ]

        for question in questions:
            label_question = tk.Label(fenetre_besoins_utilisateur, text=question, wraplength=300, justify=tk.LEFT)
            label_question.pack(anchor=tk.W)

    def action_bouton_requetes(self):
        messagebox.showinfo("Bouton démontrant l'utilisation des requêtes créées", "Fonctionnalité en cours de développement.")

if __name__ == "__main__":
    root = tk.Tk()
    interface = Interface(root)
    root.mainloop()
