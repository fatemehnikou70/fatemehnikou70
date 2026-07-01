def get_list_of_wagons(*args):
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    return (
        [each_wagons_id[2]]
        + missing_wagons
        + each_wagons_id[3:]
        + each_wagons_id[:2]
    )


def add_missing_stops(route, **stops):
    route["stops"] = list(stops.values())
    return route


def extend_route_information(route, more_route_information):
    route.update(more_route_information)
    return route


def fix_wagon_depot(wagons_rows):
    return [list(row) for row in zip(*wagons_rows)]