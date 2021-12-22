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
| `mileage` | Gauge | Total mileage |
| `range` | Gauge | Total available range |
| `state_of_charge` | Gauge | Charge percentage |
| `tank_level` | Gauge | Tank level |
| `max_charge_current` | Gauge | Max charge current |
| `oil_change_distance` | Gauge | Recommended distance left before oil change |
| `oil_change_time` | Gauge | Recommended oil change time |
| `oil_level` | Gauge | Oil level |
| `service_inspection_distance` | Gauge | Recommended distance left before service inspection |
| `service_inspection_time` | Gauge | Recommended service inspection time |
| `any_door_open` | Gauge | Are there open doors? |
| `any_door_unlocked` | Gauge | Are there unlocked doors? |
| `any_window_open` | Gauge | Are there any open windows? |
| `hood_open` | Gauge | Is the hood open? |
| `parking_light` | Gauge | Is the parking light on? |
| `trunk_open` | Gauge | Is the trunk open? |
| `trunk_unlocked` | Gauge | Is the trunk unlocked? |
| `last_update_time` | Gauge | Unixtime of the last update |
| `plug_state` | Enum | Is the charging plug connected? |
| `charging_state` | Enum | Is the car currently charging? |
| `remaining_charging_time` | Gauge | Remaining charging time in minutes |
| `climatisation_state` | Enum | Is climatisation currently active? |


## Acknowledgements
This exporter makes use of the HomeAssistent project https://github.com/arjenvrh/audi_connect_ha.git .
All their code does the API talking, we just translate those results to something prometheus can handle.
Without arjenvrh's project, this would have been a lot more work, so big thanks to them.
