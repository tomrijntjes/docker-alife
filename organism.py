"""
ENCODING:

String of binary values. First character corresponds to a card of face value 1, second card has face value 2, etcetera. "0" corresponds to pile A, "1" to pile B.

Pile A: 1
Pile B: 2,3,4,5,6,7,8,9,10

encodes to "1000000000"

SELECTION ALGORITHM:

1.appscheduler initiates sequence every n seconds wall clock time
2.containers check incoming mating requests before approaching two random candidates
3.groups of three compete. The winner lives, the other two perish

RECOMBINATION:




"""

from flask import Flask,make_response,jsonify
from docker import Client
import os
import random

cli = Client(base_url='unix://var/run/docker.sock')

app = Flask(__name__)

@app.route("/")
def home():
    if random.random()>0.9:
        cli.kill(os.environ.get('GENOME'))
    return os.environ.get('GENOME')

@app.route("/fitness")
def fitness():
    pile_A,pile_B = list(),list()
    genome = os.environ.get('GENOME')
    for i in range(len(genome)):
        if genome[i] == "0":
            pile_A.append(i+1)
        elif genome[i] == "1":
            pile_B.append(i+1)
        else:
            raise ValueError
    fitness = abs(sum(pile_A)-36)+abs(multiply_list(pile_B)-360)
    return make_response(jsonify({"fitness":fitness}),200)

def multiply_list(p):
    total = 1
    for _ in p:
        total = total*_
    return total
        
        



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)