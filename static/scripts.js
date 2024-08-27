document.addEventListener("DOMContentLoaded", function() {
    // Check if canvas element exists before initializing Chart.js
    var ctx = document.getElementById('myChart').getContext('2d');
    if (ctx) {
        var myChart = new Chart(ctx, {
            type: 'bar', // Choose chart type: 'bar', 'line', 'pie', etc.
            data: {
                labels: ['January', 'February', 'March', 'April', 'May', 'June'],
                datasets: [{
                    label: 'Sample Data',
                    data: [12, 19, 3, 5, 2, 3],
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    } else {
        console.error("Canvas element with ID 'myChart' not found.");
    }
});
