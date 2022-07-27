#! /usr/bin/env python3

import asyncio
import inspect
import os
import re
import time

from audiconnect.audi_connect_account import AudiConnectAccount, AudiConnectVehicle

from aiohttp import ClientSession
from datetime import datetime as dt
from prometheus_client import start_http_server, Enum, Gauge

labels = ["vehicle"]

metrics = {
  "mileage": Gauge("audi_mileage", "Total mileage", labels),
  "range": Gauge("audi_range", "Range", labels + ["engine"]),
  "state_of_charge": Gauge("audi_state_of_charge", "Charge percentage", labels),
  "tank_level": Gauge("audi_tank_level", "Tank level", labels),
  "max_charge_current": Gauge("audi_max_charge_current", "Max charge current", labels),
  "oil_change_distance": Gauge("audi_oil_change_distance", "Oil change distance", labels),
  "oil_change_time": Gauge("audi_oil_change_time", "Oil change time", labels),
  "oil_level": Gauge("audi_oil_level", "Oil level", labels),
  "service_inspection_distance": Gauge("audi_service_inspection_distance", "Service inspection distance", labels),
  "service_inspection_time": Gauge("audi_service_inspection_time", "Service inspection time", labels),
  "any_door_open": Gauge("audi_any_door_open", "Are there open doors?", labels),
  "any_door_unlocked": Gauge("audi_any_door_unlocked", "Are there unlocked doors?", labels),
  "any_window_open": Gauge("audi_any_window_open", "Are there any open windows?", labels),
  "hood_open": Gauge("audi_hood_open", "Is the hood open?", labels),
  "parking_light": Gauge("audi_parking_light", "Is the parking light on?", labels),
  "trunk_open": Gauge("audi_trunk_open", "Is the trunk open?", labels),
  "trunk_unlocked": Gauge("audi_trunk_unlocked", "Is the trunk unlocked?", labels),
  "last_update_time": Gauge("audi_last_update_time", "Unixtime of the last update", labels),
  "plug_state": Enum("audi_plug_state", "Plug state", labels, states=["connected", "disconnected"]),
  "charging_state": Enum("audi_charging_state", "Charging state", labels, states=["off", "charging", "completed"]),
  "remaining_charging_time": Gauge("audi_remaining_charging_time", "Remaining charging time in minutes", labels),
  "climatisation_state": Enum("audi_climatisation_state", "Climatisation state", labels, states=["off", "heating", "cooling"]),
}


def set_metrics(vehicle):
  title = vehicle.title

  data_properties = ["mileage", "state_of_charge", "tank_level", "max_charge_current",
      "oil_change_distance", "oil_change_time", "oil_level", "service_inspection_distance",
      "service_inspection_time"]

  for prop in data_properties:
    if getattr(vehicle, f"{prop}_supported"):
      metrics[prop].labels(vehicle=title).set(getattr(vehicle, prop))


  range_properties = ["range", "hybrid_range", "primary_engine_range", "secondary_engine_range"]

  for prop in range_properties:
    if getattr(vehicle, f"{prop}_supported"):
      engine = "total" if prop == "range" else prop.split('_')[0]
      metrics["range"].labels(vehicle=title, engine=engine).set(getattr(vehicle, prop))



  bool_properties = ["any_door_open", "any_door_unlocked", "any_window_open", "hood_open",
      "parking_light", "trunk_open", "trunk_unlocked"]

  for prop in bool_properties:
    if getattr(vehicle, f"{prop}_supported"):
      metrics[prop].labels(vehicle=title).set(int(getattr(vehicle, prop)))


  enum_properties = ["plug_state", "charging_state", "climatisation_state"]
  for prop in enum_properties:
    if getattr(vehicle, f"{prop}_supported"):
      metrics[prop].labels(vehicle=title).state(getattr(vehicle, prop))


  if vehicle.last_update_time_supported:
    last_update_time = dt.strptime(vehicle.last_update_time, '%Y-%m-%dT%H:%M:%S')
    metrics["last_update_time"].labels(vehicle=title).set(last_update_time.timestamp())


  if vehicle.remaining_charging_time_supported:
    if vehicle.remaining_charging_time == 'n/a':
      metrics["remaining_charging_time"].labels(vehicle=title).set(0)
    else:
      hour_minutes = [ int(i) for i in vehicle.remaining_charging_time.split(':') ]
      minutes = hour_minutes[0] * 60 + hour_minutes[1]
      metrics["remaining_charging_time"].labels(vehicle=title).set(minutes)



async def run_metrics_loop(user, password, spin, country, interval):
  async with ClientSession() as session:
    account = AudiConnectAccount(session, user, password, country, spin)
    while True:
      await account.update(None)
      vehicles = account._vehicles
      for vehicle in vehicles:
        set_metrics(vehicle)
      time.sleep(interval)


if __name__ == "__main__":
  user = os.getenv("AUDI_USER")
  password = os.getenv("AUDI_PASSWORD")
  spin = os.getenv("AUDI_SPIN")
  country = os.getenv("AUDI_COUNTRY")

  port = int(os.getenv("EXPORTER_PORT", "9086"))
  interval = int(os.getenv("EXPORTER_INTERVAL", "900"))

  start_http_server(port)

  metrics_loop = run_metrics_loop(user, password, spin, country, interval)
  asyncio.get_event_loop().run_until_complete(metrics_loop)

