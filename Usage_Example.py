file_path = '~/OceanData/3hr.nc'
output_folder = '~/OceanData/'
delimiter = ';'

time, longitude, latitude, depth, variables = read_netcdf_file(file_path)
#print(variables)

for variable_name, variable in variables.items():
    output_file = f'{output_folder}/{variable_name}.csv'
    save_variable_to_csv(output_file, time, longitude, latitude, depth, variable_name, variable, delimiter)
