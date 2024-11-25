from flask import Flask, render_template, request
from lcs import longest_common_subsequence
from knapsack import knapsack_solution
from sorting import merge_sort, quick_sort, bubble_sort# Import sorting functions
from huffman import huffman_encoding, huffman_decoding  # Import Huffman functions
from collections import defaultdict

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/lcs', methods=['GET', 'POST'])
def lcs():
    if request.method == 'POST':
        string1 = request.form['string1']
        string2 = request.form['string2']
        
        # Unpack all returned values
        lcs_result, lcs_matrix = longest_common_subsequence(string1, string2)
        
        # Render the result template with the necessary context
        return render_template('result_lcs.html', lcs=lcs_result, matrix=lcs_matrix)
    
    return render_template('lcs.html')

@app.route('/knapsack', methods=['GET', 'POST'])
def knapsack():
    if request.method == 'POST':
        weights = list(map(int, request.form['weights'].split(',')))
        values = list(map(int, request.form['values'].split(',')))
        capacity = int(request.form['capacity'])
        max_value, items_included = knapsack_solution(weights, values, capacity)
        return render_template('result_knapsack.html', max_value=max_value, items_included=items_included)
    return render_template('knapsack.html')

@app.route('/sorting', methods=['GET', 'POST'])
def sorting():
    if request.method == 'POST':
        numbers = list(map(int, request.form['numbers'].split(',')))
        algorithm = request.form['algorithm']
        
        if algorithm == 'merge':
            sorted_numbers = merge_sort(numbers)
        elif algorithm == 'quick':
            sorted_numbers = quick_sort(numbers)
        elif algorithm == 'bubble':
            sorted_numbers = bubble_sort(numbers)
        
        return render_template('result_sorting.html', sorted_numbers=sorted_numbers)
    
    return render_template('visualize_sorting.html')

@app.route('/huffman', methods=['GET', 'POST'])
def huffman():
    if request.method == 'POST':
        input_string = request.form['inputString'].upper()
        encoded_string, huffman_codes = huffman_encoding(input_string)

        # Prepare the data for the table
        frequency = defaultdict(int)
        for char in input_string:
            frequency[char] += 1

        # Create a list for the table
        huffman_table = []
        total_cost = 0

        for char in sorted(frequency.keys()):  # Sort characters
            count = frequency[char]
            code = huffman_codes[char]
            bits_used = count * len(code)
            total_cost += bits_used
            huffman_table.append((char, count, code, bits_used))

        return render_template('result_huffman.html', 
                               encoded_string=encoded_string, 
                               huffman_codes=huffman_codes, 
                               huffman_table=huffman_table, 
                               total_cost=total_cost)
    return render_template('huffman.html')

if __name__ == '__main__':
    app.run(debug=True, port=5009)
