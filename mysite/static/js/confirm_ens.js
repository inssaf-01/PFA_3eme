function openDialog() {
    document.getElementById("myDialog").showModal();
    document.getElementById("myDialog").removeAttribute("hidden");
  }
  
  function closeDialog() {
    document.getElementById("myDialog").close();
  }
  
  function confirmAction() {
    
    var form = document.getElementById("deleteForm");
    var cinInput = form.querySelector('input[name="cin"]');
    var confirmationMessage = document.getElementById("confirmationMessage");
  
    // Vérifier si le champ CIN est vide
    if (cinInput.value === "") {
      confirmationMessage.textContent = "Veuillez entrer le CIN de l'enseignant.";
    } else {
      confirmationMessage.textContent = "Enseignant avec CIN " + cinInput.value + " supprimé.";
      form.submit(); // Soumettre le formulaire pour supprimer l'enseignant
    }
  
    closeDialog(); // Fermer la boîte de dialogue
  }
  
  
  