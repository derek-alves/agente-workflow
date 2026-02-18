import os
import shutil
import datetime
import sys

def archive_reports(days_threshold=7):
    reports_dir = ".claude/reports"
    archive_dir = os.path.join(reports_dir, "archive")
    registry_path = os.path.join(reports_dir, "_registry.md")
    
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    print(f"Archiving reports older than {days_threshold} days...")
    
    # Logic to parse registry and move files would go here
    # For now, just a placeholder message
    print("Archive script executed successfully (dry-run).")

if __name__ == "__main__":
    days = 7
    if len(sys.argv) > 1:
        try:
            days = int(sys.argv[1])
        except ValueError:
            pass
    archive_reports(days)
