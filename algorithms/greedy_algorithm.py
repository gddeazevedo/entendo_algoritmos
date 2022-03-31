from typing import Set, Dict


states_needed: Set[str] = set(
    ["mt", "wa", "or", "id", "nv", "ut", "ca", "az"]
) # conjunto de estados

stations: Dict[str, Set[str]] = {}
stations["kum"] = set(["id", "nv", "ut"])
stations["kdois"] = set(["wa", "id", "mt"])
stations["ktres"] = set(["or", "nv", "ca"])
stations["kquatro"] = set(["nv", "ut"])
stations["kcinco"] = set(["ca", "az"])

final_stations: Set[str] = set()


while states_needed:
    best_station: str = None
    states_covered: Set[str] = set()

    for station, statates_for_station in stations.items():
        covered: Set[str] = states_needed & statates_for_station # intersecção de conjuntos

        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)


print(final_stations)
