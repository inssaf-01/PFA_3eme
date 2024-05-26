function openDialog() {
    document.getElementById("myDialog").showModal();
    document.getElementById("myDialog").removeAttribute("hidden");
  }

  function closeDialog() {
    event.preventDefault();
    document.getElementById("myDialog").setAttribute("hidden", "true");
    
  }

  function confirmAction() {

    var form = document.getElementById("deleteForm");
    var cneInput = form.querySelector('input[name="cne"]');
    etudiant = Etudiant.objects.get(CNE='input[name="cne"]')
    
    var confirmationMessage = document.getElementById("confirmationMessage");

    

    // Vérifier si le champ CNE est vide
     if (cneInput.value === "") {
      confirmationMessage.textContent = "Veuillez entrer le CNE de l'etudiant.";
    } else   {
      
      confirmationMessage.textContent = "Etudiant avec CNE " + cneInput.value + " supprimé.";
      form.submit(); // Soumettre le formulaire pour supprimer l'enseignant
    }

    closeDialog(); // Fermer la boîte de dialogue 
  }