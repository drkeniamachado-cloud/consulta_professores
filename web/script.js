async function buscar() {
    const termo = document.getElementById("search").value 
    const reposta = await fetch("/api professores?nome="+termo)
    const dados = await resposta.jsom()
    const div = document.getElementById("resultados")


    div.innerHTML = ""
    dados.forEach(p => {
        const item = document.createElement("p")
        item. textContent = p.nome 
        div.appendChild(item)
    });

    
}
