def tuples_to_dict(results, columns):
    parsed_results = [dict(zip(columns, row)) for row in results]
    return parsed_results