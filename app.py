from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_love_percentage(name, name1):
    name = name.lower()
    name1 = name1.lower()
    love_list = []

    for char in name:
        if char in name1:
            love_list.append(2)
        else:
            love_list.append(1)
    
    for char in name1:
        if char not in name:
            love_list.append(1)

    while len(love_list) > 4:
        result = [love_list[i] + love_list[~i] for i in range(len(love_list) // 2)]
        if len(love_list) % 2 == 1:
            result.append(love_list[len(love_list) // 2])
        love_list = result

    if len(love_list) == 3:
        first = love_list[0] + love_list[2]
        second = love_list[1]
    else:
        first = love_list[0] + love_list[3]
        second = love_list[1] + love_list[2]

    final = int(str(first) + str(second))
    while len(str(final)) > 2:
        string = str(final)
        new_final = [int(string[i]) + int(string[~i]) for i in range(len(string) // 2)]
        if len(string) % 2 == 1:
            new_final.append(int(string[len(string) // 2]))
        final = int("".join(map(str, new_final)))

    return final

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':  
        name = request.form['name']
        name1 = request.form['name1']
        love_percentage = calculate_love_percentage(name, name1)
        return render_template('result.html', name=name, name1=name1, love_percentage=love_percentage)
    else:  
        return render_template('index.html')

import os
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

