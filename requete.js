
db.produits.find({ ID: 2 })

db.avis.find({ produitID: 4 })

db.commandes.find({ ID: 5 })

db.produits.find({ $and: [{ prix: { $gte:10, $lte: 30 } }, { fournisseurID: 3 }] })

//db.utilisateurs.updateOne({ ID: 17 }, 
 //{ $set: { email: , mot_de_passe:  } })

//db.inventaires.find({ produitID:7})

//db.commandes.find({ userID: 3, statut: "en cours" })

//db.produits.updateOne(
    //{ _id: 1 }, 
    //{ $set: { prix: 90.00 } } );
    