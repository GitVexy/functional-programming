from enum import Enum


class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4


def get_csv_status(status, data: list):
    match (status):
        case CSVExportStatus.PENDING:
            return pending(data)
        case CSVExportStatus.PROCESSING:
            return processing(data)
        case CSVExportStatus.SUCCESS:
            return success(data)
        case CSVExportStatus.FAILURE:
            return failure(data)
        case _:
            raise Exception("Unknown export status")

def pending(data: list, fail_state = False) -> tuple:
    local_data = data.copy()
    for lst in local_data:
        for i in range(len(lst)):
            lst[i] = str(lst[i])
    
    if fail_state: return local_data
    
    return "Pending...", local_data


def processing(data: list, fail_state = False) -> tuple:
    local_data = data.copy()
    output = ""
    for lst in local_data:
        for item in lst:
            output += f"{item},"
        output = output.rstrip(",")
        output += "\n"
    output = output.rstrip("\n")
    
    if fail_state: return output
    
    return "Processing...", output

def success(data: str) -> tuple:
    return "Success!", data


def failure(data: list) -> tuple:
    print(data)
    return "Unknown error, retrying...", processing(pending(data, fail_state=True), fail_state=True)


