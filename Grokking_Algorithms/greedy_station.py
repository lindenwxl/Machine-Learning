from __future__ import print_function,division


def main():
    states_needed = set(["mt", "wa", "or", "id", "nv", "ut","ca", "az"])
    
    # You also need the list of stations that you’re choosing from.  Choose to use a hash for this:
    stations = {}
    stations["kone"] = set(["id", "nv", "ut"])
    stations["ktwo"] = set(["wa", "id", "mt"])
    stations["kthree"] = set(["or", "nv", "ca"])
    stations["kfour"] = set(["nv", "ut"])
    stations["kfive"] = set(["ca", "az"])
    
    final_stations = set()
    
    

    while states_needed:
        best_station = None
        states_covered = set()
        for station, states_for_station in station.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
                
    states_needed -= states_covered
    final_stations.add(best_station)


if __name__=="__main__":
    main()
