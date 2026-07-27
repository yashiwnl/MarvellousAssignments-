# Duplicate File Removal Automation

## Project Description

Duplicate File Removal Automation is a Python-based automation tool that periodically scans a specified directory and its subdirectories to identify duplicate files using MD5 checksums. Duplicate copies are deleted while preserving one original file from each duplicate group.

The application generates a detailed timestamp-based log file for every execution and sends the log file as an email attachment to the specified receiver. The entire process is repeated automatically after a user-defined time interval.

---

## Features

- Recursive directory scanning
- MD5 checksum-based duplicate file detection
- Automatic duplicate file deletion
- Preserves one original file from each duplicate group
- Timestamp-based log file generation
- Periodic execution using the `schedule` module
- Email notification after every execution
- Automatic log file attachment in email
- Command-line argument support
- Help and Usage options
- Input validation
- Exception handling
- Modular programming design

---

## Requirements

### Python Version

- Python 3.10 or later

### Required Libraries

#### Built-in Libraries

- os
- sys
- time
- hashlib
- smtplib
- datetime
- email

#### External Library

- schedule

Install it using:

```bash
pip install schedule
```

### Additional Requirements

- Internet connection for sending emails
- Gmail account (or another SMTP-supported email provider)
- Gmail App Password (recommended instead of your normal password)

---

## Project Structure

```
DuplicateFileRemoval/
│
├── DuplicateFileRemoval.py    # Main application
├── Validator.py               # Input validation functions
├── Logger.py                  # Log directory and log file operations
├── FileUtils.py               # File scanning, checksum generation and duplicate removal
├── MailSender.py              # Email sending with log attachment
├── Marvellous/                # Generated log files
└── README.md
```

### Module Description

**DuplicateFileRemoval.py**

- Reads command-line arguments
- Validates user input
- Coordinates all modules
- Schedules periodic execution

**Validator.py**

- Validates directory path
- Validates time interval
- Validates receiver email address

**Logger.py**

- Creates the Marvellous log directory
- Creates timestamp-based log files
- Writes execution details to the log

**FileUtils.py**

- Recursively scans directories
- Calculates MD5 checksums
- Detects duplicate files
- Deletes duplicate copies

**MailSender.py**

- Creates email messages
- Attaches generated log file
- Sends operation report through Gmail SMTP

---

## Command-Line Arguments

| Argument | Description |
|----------|-------------|
| Directory Path | Absolute path of the directory to scan |
| Time Interval | Time interval in minutes |
| Receiver Email | Email address to receive the operation report |

---

## Execution Command

```bash
python DuplicateFileRemoval.py "E:/Data/Demo" 50 marvellousinfosystem@gmail.com
```

> **Note:** If the directory path contains spaces, enclose it in double quotes.

Example:

```bash
python DuplicateFileRemoval.py "D:/Projects/Test Folder" 10 example@gmail.com
```

---

## Help Command

```bash
python DuplicateFileRemoval.py --help
```

or

```bash
python DuplicateFileRemoval.py -h
```

Displays:

- Project description
- Required arguments
- Example command

---

## Usage Command

```bash
python DuplicateFileRemoval.py --usage
```

or

```bash
python DuplicateFileRemoval.py -u
```

Displays:

```text
python DuplicateFileRemoval.py <AbsoluteDirectoryPath> <TimeIntervalInMinutes> <ReceiverEmailAddress>
```

---

## Log File Information

All log files are stored inside the **Marvellous** directory.

Example:

```
Marvellous/
    DuplicateFileLog_27_07_2026_16_45_10.log
```

Each log file contains:

- Log generation time
- Directory scanned
- Receiver email
- Scanning start time
- Scanning completion time
- Total files scanned
- Total duplicate files found
- Total duplicate files deleted
- Duplicate file checksums
- Deleted file paths
- Email delivery status
- Errors encountered during execution

---

## Email Configuration

The application uses Gmail SMTP to send emails.

Configure:

- Sender email address
- Gmail App Password

**Recommended**

Do **not** hard-code credentials in the source code.

Instead, store them using:

- Environment variables
- Configuration file
- Secret manager

---

## Important Notes

- Deleted duplicate files may not be recoverable.
- Always test the application on a sample directory before using it on important data.
- Do not hard-code your email password or App Password.
- One original file from every duplicate group is always preserved.
- Files are considered duplicates only if their MD5 checksums are identical.

---

## Workflow

During every scheduled execution the application performs the following operations:

1. Scan the specified directory recursively.
2. Calculate the MD5 checksum of every file.
3. Detect duplicate files using checksum comparison.
4. Preserve one original copy.
5. Delete remaining duplicate copies.
6. Generate a timestamp-based log file inside the **Marvellous** directory.
7. Record all deleted files and execution statistics.
8. Send the generated log file to the receiver through email.
9. Wait for the specified interval and repeat the process automatically.

---

## Author

**Yash Satarkar**

Computer Engineering Student

Project developed as part of a Python Automation assignment.