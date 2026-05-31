from analytics import visitor_journeys


def update_journey(track_id, zone):

    if zone is None:
        return

    if track_id not in visitor_journeys:
        visitor_journeys[track_id] = []

    if (
        len(visitor_journeys[track_id]) == 0
        or visitor_journeys[track_id][-1] != zone
    ):
        visitor_journeys[track_id].append(zone)

        print(
            f"JOURNEY -> Visitor {track_id}: "
            f"{visitor_journeys[track_id]}"
        )