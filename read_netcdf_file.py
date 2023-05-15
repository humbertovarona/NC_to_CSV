def read_netcdf_file(file_path):
    dataset = nc.Dataset(file_path)
    time = dataset.variables["time"][:]
    longitude = dataset.variables["lon"][:]
    latitude = dataset.variables["lat"][:]
    depth = dataset.variables["depth"][:] if 'depth' in dataset.variables else None

    variables = {}
    for var_name, variable in dataset.variables.items():
        if var_name not in ["time", "lon", "lat", "depth"]:
            variables[var_name] = variable

    return time, longitude, latitude, depth, variables
