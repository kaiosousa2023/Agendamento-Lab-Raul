document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("form-agendamento");
    const tabela = document.getElementById("tabela-agendamentos").querySelector("tbody");
  
    // Carrega os dados salvos
    let agendamentos = JSON.parse(localStorage.getItem("agendamentos")) || [];
  
    function salvarLocalStorage() {
      localStorage.setItem("agendamentos", JSON.stringify(agendamentos));
    }
  
    function renderTabela() {
      tabela.innerHTML = "";
      agendamentos.forEach((agendamento, index) => {
        const tr = document.createElement("tr");
  
        tr.innerHTML = `
          <td>${agendamento.professor}</td>
          <td>${agendamento.materia}</td>
          <td>${new Date(agendamento.data_hora).toLocaleString("pt-BR")}</td>
          <td><button onclick="removerAgendamento(${index})">Remover</button></td>
        `;
  
        tabela.appendChild(tr);
      });
    }
  
    form.addEventListener("submit", (e) => {
      e.preventDefault();
  
      const novoAgendamento = {
        professor: document.getElementById("professor").value,
        materia: document.getElementById("materia").value,
        data_hora: document.getElementById("data_hora").value,
      };
  
      agendamentos.push(novoAgendamento);
      salvarLocalStorage();
      renderTabela();
      form.reset();
    });
  
    window.removerAgendamento = function(index) {
      if (confirm("Tem certeza que deseja remover esse agendamento?")) {
        agendamentos.splice(index, 1);
        salvarLocalStorage();
        renderTabela();
      }
    };
  
    // Inicializa a tabela
    renderTabela();
  });
  