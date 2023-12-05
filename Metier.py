# Créer une instance de la classe Metier
metier1 = Metier("Développeur", [1, 2, 3])

# Créer une instance de la classe Independant
independant1 = Independant(1, "Dupont", "Jean", "75001", "jean.dupont@example.com", metier1)

# Appeler la méthode __str__ de la classe Metier
print(metier1)

# Appeler la méthode get_nb_independants de la classe Metier
print(metier1.get_nb_independants())

# Appeler la méthode __str__ de la classe Independant
print(independant1)

# Appeler la méthode statique get_emails_by_speciality_and_sector de la classe Independant
print(Independant.get_emails_by_speciality_and_sector("Développeur", "75001"))

# Appeler la méthode statique get_nb_independants_by_speciality_and_sector de la classe Independant
print(Independant.get_nb_independants_by_speciality_and_sector("Développeur", "75001"))
