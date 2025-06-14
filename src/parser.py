import re
import pandas as pd

# Define regex patterns for different formats
LOG_PATTERNS = {
    "default": re.compile(r"\[(ERROR|WARNING|INFO)\].*?-\s+(.*)"),
    "apache": re.compile(r'(\d{1,3}(?:\.\d{1,3}){3}).+\] "(GET|POST) (.+?)" (\d{3})'),
    "syslog": re.compile(r'^\w{3} +\d+ \d{2}:\d{2}:\d{2} \S+ \S+\[\d+\]: (.*)$'),
    "custom": re.compile(r'ERROR::\[timestamp=(.*?)\]::(.*)')
}

def parse_log_dataframe(df, log_format="default"):
    pattern = LOG_PATTERNS.get(log_format)
    if not pattern:
        raise ValueError(f"Unsupported log format: {log_format}")

    messages = []
    levels = []

    for line in df["line"]:
        match = pattern.search(line)
        if not match:
            messages.append("UNKNOWN")
            levels.append("UNKNOWN")
            continue

        if log_format == "default":
            level, msg = match.groups()
        elif log_format == "apache":
            ip, method, resource, status = match.groups()
            level, msg = "INFO", f"{method} {resource} - Status {status}"
        elif log_format == "syslog":
            level, msg = "ERROR", match.group(1)
        elif log_format == "custom":
            ts, msg = match.groups()
            level = "ERROR"

        messages.append(msg.strip())
        levels.append(level)

    df["level"] = levels
    df["message"] = messages
    return df
