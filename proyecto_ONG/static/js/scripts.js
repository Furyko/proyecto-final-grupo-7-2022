window.onload = function() {
    // Obtiene la ventana del modal
    var modal = document.getElementById("event-modal")
    // Obtiene los botónes que abren el modal
    var btn = document.getElementsByClassName("event-button")
    // Obtiene el botón que cierra el modal 
    var span = document.getElementsByClassName("close")[0]
    // Obtiene el contenido del modal
    var modalContent = document.getElementsByClassName('modal-content')[0]

    /* Cuando el usuario toca cualquiera de los botones, abre el modal
       con la información especifica de ese día */
    for (i of btn) {
        i.onclick = function(event) {
            modal.style.display = "block"
            let modalParagraph = modalContent.querySelector('p')
            let targetClass = event.target.attributes.class.textContent
            // Obtiene la lista de elementos dependiendo del target que obtenga
            if (targetClass == 'date') {
                var lista = event.target.parentNode.childNodes[1]
            } else if (targetClass == 'event-button') {
                var lista = event.target.querySelector('ul')
            }
            modalParagraph.innerHTML = lista.innerHTML
        }
    }
    span.onclick = function() {
        modal.style.display = "none"
    }
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none"
        }
    }
}
