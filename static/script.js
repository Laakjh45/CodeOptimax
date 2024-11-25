<script>
    const ctx = document.getElementById('knapsackChart').getContext('2d');

    // Check if items_included has data
    const itemsIncluded = [
        {% if items_included %}
            {% for weight, value in items_included %}
            [{{ weight }}, {{ value }}]{% if not loop.last %},{% endif %}
            {% endfor %}
        {% else %}
            // Fallback to an empty array if no items are included
            []
        {% endif %}
    ];

    // Check if itemsIncluded has any data before proceeding
    if (itemsIncluded.length > 0) {
        const weights = itemsIncluded.map(item => item[0]);
        const values = itemsIncluded.map(item => item[1]);

        const knapsackChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: weights,
                datasets: [{
                    label: 'Values',
                    data: values,
                    backgroundColor: 'rgba(75, 192, 192, 0.6)',
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
        console.error("No items included for the knapsack chart.");
    }
</script>