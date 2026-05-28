from get_data import get_data_f
from load_yaml import load_yaml_f
from transform import transform_data
from dashboard import build_dashboard
from pathlib import Path

path = Path.home() / "PycharmProjects" / "stocks_analytics" / "src" / "stocks.yaml"

def main(stock_path: Path):
    stock_list = load_yaml_f(stock_path)
    data = get_data_f(stock_list["stocks"], stock_list["dperiod"], stock_list["dinterval"])
    dfs = transform_data(data)
    dashboard = build_dashboard(dfs["processed_data"], dfs["metrics_dfs"] )
    return dashboard

if __name__ == "__main__":
    main(path)