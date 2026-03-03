let monthlyChart;
let projectChart;
let userChart;

function loadCharts() {

    fetch('/api/kanban/')
    .then(res => res.json())
    .then(data => {

        // ===== MONTHLY =====
        if (monthlyChart) {
            monthlyChart.data.labels = data.months;
            monthlyChart.data.datasets[0].data = data.monthly;
            monthlyChart.update();
        } else {
            monthlyChart = new Chart(document.getElementById('monthlyChart'), {
                type: 'line',
                data: {
                    labels: data.months,
                    datasets: [{
                        label: 'Évolution mensuelle',
                        data: data.monthly,
                        borderColor: '#00ff99',
                        tension: 0.4
                    }]
                },
                options: {
                    responsive: true,
                    plugins: { legend: { display: true } }
                }
            });
        }

        // ===== PROJECT =====
        if (projectChart) {
            projectChart.data.labels = data.projects;
            projectChart.data.datasets[0].data = data.tasks;
            projectChart.update();
        } else {
            projectChart = new Chart(document.getElementById('projectChart'), {
                type: 'bar',
                data: {
                    labels: data.projects,
                    datasets: [{
                        label: 'Tâches par projet',
                        data: data.tasks,
                        backgroundColor: '#3498db'
                    }]
                }
            });
        }

        // ===== USER =====
        if (userChart) {
            userChart.data.labels = data.users;
            userChart.data.datasets[0].data = data.productivity;
            userChart.update();
        } else {
            userChart = new Chart(document.getElementById('userChart'), {
                type: 'bar',
                data: {
                    labels: data.users,
                    datasets: [{
                        label: 'Productivité utilisateur',
                        data: data.productivity,
                        backgroundColor: '#e67e22'
                    }]
                }
            });
        }

    });
}

// chargement initial
loadCharts();

// refresh toutes les 5 secondes
setInterval(loadCharts, 5000);