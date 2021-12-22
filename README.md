# Prometheus Audi Exporter

This Prometheus exporter exports metrics that it fetches from the MyAudi API.

## Usage
* Checkout submodules
* Install dependencies from `requirements.txt`
* Run `./audi_exporter.py` with environment variables `AUDI_USER`, `AUDI_PASSWORD`, `AUDI_SPIN` and `AUDI_COUNTRY`
* Get metrics from `http://localhost:9086/metrics`

### Configuration
The following environment variables can be used to configure the exporter:

| Variable            | Required             | What?                              |
|---------------------|----------------------|------------------------------------|
| `AUDI_USER`         | yes                  | Username of your MyAudi account    |
| `AUDI_PASSWORD`     | yes                  | Password of your MyAudi account    |
| `AUDI_SPIN`         | yes                  | SPIN of your MyAudi account        |
| `AUDI_COUNTRY`      | yes                  | Country you are located in         |
| `EXPORTER_PORT`     | no (default: `9086`) | Port for the exporter to listen on |
| `EXPORTER_INTERVAL` | no (default: `900`)  | API polling interval in seconds    |

### Available metrics

| Name | Type | Description |
|------|------|-------------|
| `audi_mileage` | Gauge | Total mileage |
| `audi_range` | Gauge | Total available range |
| `audi_state_of_charge` | Gauge | Charge percentage |
| `audi_tank_level` | Gauge | Tank level |
| `audi_max_charge_current` | Gauge | Max charge current |
| `audi_oil_change_distance` | Gauge | Recommended distance left before oil change |
| `audi_oil_change_time` | Gauge | Recommended oil change time |
| `audi_oil_level` | Gauge | Oil level |
| `audi_service_inspection_distance` | Gauge | Recommended distance left before service inspection |
| `audi_service_inspection_time` | Gauge | Recommended service inspection time |
| `audi_any_door_open` | Gauge | Are there open doors? |
| `audi_any_door_unlocked` | Gauge | Are there unlocked doors? |
| `audi_any_window_open` | Gauge | Are there any open windows? |
| `audi_hood_open` | Gauge | Is the hood open? |
| `audi_parking_light` | Gauge | Is the parking light on? |
| `audi_trunk_open` | Gauge | Is the trunk open? |
| `audi_trunk_unlocked` | Gauge | Is the trunk unlocked? |
| `audi_last_update_time` | Gauge | Unixtime of the last update |
| `audi_plug_state` | Enum | Is the charging plug connected? |
| `audi_charging_state` | Enum | Is the car currently charging? |
| `audi_remaining_charging_time` | Gauge | Remaining charging time in minutes |
| `audi_climatisation_state` | Enum | Is climatisation currently active? |


## Acknowledgements
This exporter makes use of the HomeAssistent project https://github.com/arjenvrh/audi_connect_ha.git .
All their code does the API talking, we just translate those results to something prometheus can handle.
Without arjenvrh's project, this would have been a lot more work, so big thanks to them.
