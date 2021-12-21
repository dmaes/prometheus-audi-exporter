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


## Acknowledgements
This exporter makes use of the HomeAssistent project https://github.com/arjenvrh/audi_connect_ha.git .
All their code does the API talking, we just translate those results to something prometheus can handle.
Without arjenvrh's project, this would have been a lot more work, so big thanks to them.
