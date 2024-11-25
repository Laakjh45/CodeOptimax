// Function to visualize sorting based on the selected algorithm
document.getElementById('sortForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const numbers = document.getElementById('numbers').value.split(',').map(Number);
    const algorithm = document.getElementById('algorithm').value;
    visualizeSorting(numbers, algorithm);
});

// Function to visualize sorting
function visualizeSorting(arr, algorithm) {
    const ctx = document.getElementById('sortChart').getContext('2d');
    const chartData = {
        labels: arr.map((_, index) => index + 1),
        datasets: [{
            label: 'Sorting Visualization',
            data: arr,
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }]
    };

    const myChart = new Chart(ctx, {
        type: 'bar',
        data: chartData,
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Call the sorting function based on the selected algorithm
    if (algorithm === 'merge') {
        mergeSort(arr, myChart);
    } else if (algorithm === 'quick') {
        quickSort(arr, myChart);
    } else if (algorithm === 'bubble') {
        bubbleSort(arr, myChart);
    }
}

// Bubble Sort visualization
function bubbleSort(arr, chart) {
    let n = arr.length;

    const updateChart = (data) => {
        chart.data.datasets[0].data = data;
        chart.update();
    };

    const sortStep = (i, j) => {
        if (i < n) {
            if (j < n - i - 1) {
                if (arr[j] > arr[j + 1]) {
                    [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]]; // Swap
                }
                updateChart(arr);
                setTimeout(() => sortStep(i, j + 1), 100);
            } else {
 sortStep(i + 1, 0);
            }
        }
    };

    sortStep(0, 0);
}

// Merge Sort visualization
function mergeSort(arr, chart) {
    const updateChart = (data) => {
        chart.data.datasets[0].data = data;
        chart.update();
    };

    const merge = (left, right) => {
        const result = [];
        let leftIndex = 0;
        let rightIndex = 0;

        while (leftIndex < left.length && rightIndex < right.length) {
            if (left[leftIndex] < right[rightIndex]) {
                result.push(left[leftIndex]);
                leftIndex++;
            } else {
                result.push(right[rightIndex]);
                rightIndex++;
            }
        }

        return result.concat(left.slice(leftIndex)).concat(right.slice(rightIndex));
    };

    const sortStep = (array) => {
        if (array.length <= 1) return array;

        const mid = Math.floor(array.length / 2);
        const left = sortStep(array.slice(0, mid));
        const right = sortStep(array.slice(mid));

        const merged = merge(left, right);
        updateChart(merged);
        return merged;
    };

    sortStep(arr);
}

// Quick Sort visualization
function quickSort(arr, chart) {
    const updateChart = (data) => {
        chart.data.datasets[0].data = data;
        chart.update();
    };

    const sortStep = (array) => {
        if (array.length <= 1) return array;

        const pivot = array[array.length - 1];
        const left = [];
        const right = [];

        for (let i = 0; i < array.length - 1; i++) {
            if (array[i] < pivot) {
                left.push(array[i]);
            } else {
                right.push(array[i]);
            }
        }

        const sortedArray = [...sortStep(left), pivot, ...sortStep(right)];
        updateChart(sortedArray);
        return sortedArray;
    };

    sortStep(arr);
}