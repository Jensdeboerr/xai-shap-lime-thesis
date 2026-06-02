import cdsapi

dataset = "reanalysis-era5-single-levels-timeseries"

request = {
    "variable": [
        "2m_dewpoint_temperature",
        "mean_sea_level_pressure",
        "surface_pressure",
        "2m_temperature",
        "total_precipitation",
        "10m_u_component_of_wind",
        "10m_v_component_of_wind",
        "total_cloud_cover",
    ],
    "location": {
        "longitude": 5.25,
        "latitude": 52.00,
    },  # this is the location for De Bilt (the Netherlands)
    "date": ["2010-01-01/2025-01-01"],
    "data_format": "netcdf",
}

client = cdsapi.Client()

client.retrieve(dataset, request).download("data/raw/era5_debilt_2010_2025_basic.nc")

print("download done")
