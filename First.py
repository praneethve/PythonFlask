#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('name')
    print (name)
    with open('/Users/prane/Documents/temp/Data.txt','r') as f:
        data = f.read()
        records = json.loads(data)
        for record in records:
            if record['name'] == name:
                return jsonify(record)
        return jsonify({'error': 'data not found'})

@app.route('/create', methods=['POST'])
def create_record():
    print("input")
    record = json.loads(request.data)
    print(record)
    with open('/Users/prane/Documents/temp/Data.txt', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('/Users/prane/Documents/temp/Data.txt', 'w') as f:
        var2=json.dumps(records, indent=2)
        print(var2)
        f.write(json.dumps(records, indent=2))
    return jsonify(record)

@app.route('/update', methods=['PUT'])
def update_record():
    print("in post")
    record = json.loads(request.data)
    print(record)
    new_records = []
    with open('/Users/prane/Documents/temp/Data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
    for r in records:
        if r['name'] == record['name']:
            r['email'] = record['email']
        new_records.append(r)
    with open('/Users/prane/Documents/temp/Data.txt', 'w') as f:
        var1= json.dumps(new_records, indent=2)
        print(var1)
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)
    
@app.route('/', methods=['DELETE'])
def delte_record():
    record = json.loads(request.data)
    new_records = []
    with open('/Users/prane/Documents/temp/Data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['name'] == record['name']:
                continue
            new_records.append(r)
    with open('/Users/prane/Documents/temp/Data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)

app.run(debug=True)
