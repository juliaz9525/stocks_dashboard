from get_data import get_data_f
from load_yaml import load_yaml_f
from transform import transform_data
from dashboard import build_dashboard

path = r"/home/julia/PycharmProjects/stocks_analytics/src/stocks.yaml"

def main(stock_path: str):
    stock_list = load_yaml_f(stock_path)
    data = get_data_f(stock_list["stocks"], stock_list["dperiod"], stock_list["dinterval"])
    dfs = transform_data(data)
    dashboard = build_dashboard(dfs["processed_data"], dfs["metrics_dfs"] )
    return dashboard

if __name__ == "__main__":
    main(path)