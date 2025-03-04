from src.utils import open_file
from src.views import date_operations_filtering, return_json_answer

if __name__ == "__main__":
    print(return_json_answer("2023-10-05 14:30:00"))
    # print(open_file('./data/operations.xlsx'))
    print(date_operations_filtering('20.05.2020'))