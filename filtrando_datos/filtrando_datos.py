from data import DATA
def run():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    #Reto
    all_python_devs_reto = list(map(lambda worker : worker['name'], list(filter(lambda worker : worker['language'] == 'python', DATA))))
    all_platzi_workers_reto = list(map(lambda worker : worker['name'], list(filter(lambda worker : worker['organization'] == 'Platzi', DATA))))

    adults = list(filter(lambda worker : worker["age"] >= 18 , DATA))
    adults = list(map(lambda worker : worker["name"], adults))
    old_people = list(map(lambda worker : {**worker, **{"old" : worker["age"] > 70}}, DATA))
    #Reto
    adults_reto = [worker['name'] for worker in DATA if worker['age'] >= 18]
    old_people_reto = [{**worker, **{"old" : worker["age"] > 70}} for worker in DATA]
    
    for worker in adults:
        print(worker)
if __name__ == '__main__':
    run()