const ulElement = document.querySelector("ul");

fetch("http://127.0.0.1:5000/api/etudiant").then(
            response => {
                response.json();
            }
        ).then((etudiants) => {
            for(const etudiant in etudiants){
                const liElement = document.createElement("li");
                liElement.innerText = etudiant.nom;
                ulElement.appendChild(liElement);
            }
        })