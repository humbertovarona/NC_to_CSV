def save_variable_to_csv(output_file, time, longitude, latitude, depth, variable_name, variable, delimiter=','):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter)

        header = ['time', 'lon', 'lat']
        if depth is not None:
            header.append('depth')
        header.append(variable_name)
        writer.writerow(header)

        for t in range(len(time)):
            for lon in range(len(longitude)):
                for lat in range(len(latitude)):
                    if depth is not None:
                        for d in range(len(depth)):
                            value = variable[t, d, lat, lon]
                            if isinstance(value, np.ma.MaskedArray):
                                value = value.item()
                            data_row = [
                                time[t],
                                longitude[lon],
                                latitude[lat],
                                depth[d],
                                value,
                            ]
                            writer.writerow(data_row)
                    else:
                        value = variable[t, lat, lon]
                        if isinstance(value, np.ma.MaskedArray):
                            value = value.item()
                        data_row = [
                            time[t],
                            longitude[lon],
                            latitude[lat],
                            value,
                        ]
                        writer.writerow(data_row)

    print(f'Saved variable "{variable_name}" to {output_file}.')
