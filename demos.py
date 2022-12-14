"""Functional Demonstration (see README.md)"""

import asyncio
from src.mvgapi import MvgApi, TransportType


def demo_basic() -> None:
    """Basic Usage"""
    station = MvgApi.station('Universität, München')
    if station:
        mvgapi = MvgApi(station['id'])
        departures = mvgapi.departures()
        print(station, departures)


def demo_filter() -> None:
    """Filters"""
    station = MvgApi.station('Universität, München')
    if station:
        mvgapi = MvgApi(station['id'])
        departures = mvgapi.departures(
            limit=3,
            offset=5,
            transport_types=[TransportType.UBAHN])
        print(station, departures)


async def demo_async() -> None:
    """Advanced Usage: Asynchronous Methods"""
    station = await MvgApi.station_async('Universität, München')
    if station:
        departures = MvgApi.departures_async(station['id'])
        print(station, await departures)

if __name__ == "__main__":

    demo_basic()
    demo_filter()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(demo_async())
