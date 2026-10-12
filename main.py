"""Enterprise Automation & Data Processing System - entry point.

Usage:
    python main.py          interactive menu
    python main.py run      run the full pipeline once
    python main.py auto     start scheduler + dashboard
"""
import sys
import time

import api_client
import config
import dashboard
import database
import file_processor
import report_generator
from logger_setup import get_logger
from scheduler import Scheduler, run_job

log = get_logger()

MENU = """
=============================================
  ENTERPRISE AUTOMATION & DATA PROCESSING
=============================================
 1. Create sample input files
 2. Process files (multithreaded)
 3. Fetch data from API
 4. Generate report
 5. Run full pipeline once
 6. Start automation (scheduler + dashboard)
 7. Exit
"""


def pipeline():
    run_job("file_processing", file_processor.process_all)
    run_job("api_fetch", api_client.fetch_and_store)
    return run_job("report", report_generator.generate_report)


def start_automation():
    scheduler = Scheduler()
    scheduler.add_job("file_processing", file_processor.process_all, config.FILE_JOB_INTERVAL)
    scheduler.add_job("api_fetch", api_client.fetch_and_store, config.API_JOB_INTERVAL)
    scheduler.add_job("report", report_generator.generate_report, config.REPORT_JOB_INTERVAL)
    dashboard.start_dashboard()
    scheduler.start()
    print(f"\nRunning. Dashboard: http://127.0.0.1:{config.DASHBOARD_PORT}   (Ctrl+C to stop)")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping...")
        scheduler.stop()


def menu():
    while True:
        print(MENU)
        choice = input("Choice (1-7): ").strip()
        if choice == "1":
            print("Created:", ", ".join(file_processor.create_sample_files()))
        elif choice == "2":
            for r in run_job("file_processing", file_processor.process_all) or []:
                print(" ", r)
        elif choice == "3":
            print(run_job("api_fetch", api_client.fetch_and_store))
        elif choice == "4":
            print(run_job("report", report_generator.generate_report))
        elif choice == "5":
            print(pipeline())
        elif choice == "6":
            start_automation()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("! Invalid choice.")


def main():
    database.init_db()
    mode = sys.argv[1].lower() if len(sys.argv) > 1 else "menu"
    try:
        if mode == "run":
            print(pipeline())
        elif mode == "auto":
            start_automation()
        else:
            menu()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting safely.")
    except Exception:
        log.exception("Fatal error")


if __name__ == "__main__":
    main()
