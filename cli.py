import argparse
from prettytable import PrettyTable
from core.monitor import monitor_db

def display_requests():
    logs = monitor_db.get_requests()

    if not logs:
        print("No logs found.")
        return

    table = PrettyTable(["Timestamp", "Endpoint", "Provider", "User Email", "User ID"])
    table.align = "l"

    for log in logs:
        table.add_row([log.timestamp, log.endpoint, log.provider, log.user_email, log.user_id])

    print(table)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitor API request logs.")
    parser.add_argument("--show", action="store_true", help="Display logged API requests.")
    args = parser.parse_args()

    if args.show:
        display_requests()
