# PacketView 📡

A lightweight local network and system information tool built in Python.

## Current features

- Local hostname and IP information
- Basic operating-system and Python information
- Network interface listing
- Basic connectivity check
- Simple terminal interface

## Requirements

- Python 3
- Linux/macOS/Windows

The current version uses only Python's standard library.

## Run

```bash
python3 packetview.py
```

## Chromebook tutorial 💻

PacketView can run on a Chromebook through ChromeOS's **Linux development environment**. Google documents this as the Linux environment used for development and command-line tools. citeturn0search0

### 1. Enable Linux

Open **Settings → About ChromeOS → Developers → Linux development environment → Set up** and follow the setup steps. A Terminal app will be available when setup finishes. citeturn0search0

### 2. Install Python

Open the Linux Terminal and run:

```bash
sudo apt update
sudo apt install python3
```

Check that Python works:

```bash
python3 --version
```

### 3. Download PacketView

On GitHub, open the **PacketView** repository, select **Code → Download ZIP**, and extract the ZIP file.

If the extracted folder is in ChromeOS **Downloads**, you may need to share the Downloads folder with Linux before the Terminal can access it. ChromeOS makes shared folders available to Linux under `/mnt/chromeos/MyFiles/`. citeturn0search0turn0search2

An alternative is to move the extracted `PacketView-main` folder into **Linux files** in the ChromeOS Files app.

### 4. Open the project

In Terminal, change into the extracted folder. For example:

```bash
cd PacketView-main
```

If you moved it into your Linux home directory with the name `PacketView`, use:

```bash
cd PacketView
```

### 5. Start PacketView

Run:

```bash
python3 packetview.py
```

You should see the PacketView menu.

### Troubleshooting

**`cd: PacketView: No such file or directory`**

The folder is probably still in ChromeOS Downloads, or it has a different name such as `PacketView-main`. Open the Files app and check the exact folder name and location.

**`python3: command not found`**

Install Python with:

```bash
sudo apt update
sudo apt install python3
```

**The ZIP won't run directly**

Extract the ZIP first. PacketView runs from the extracted project folder, not from the compressed `.zip` file.

## Roadmap

- [ ] Better interface detection
- [ ] Local device discovery
- [ ] Connection statistics
- [ ] Exportable reports
- [ ] Cleaner terminal UI
- [x] Chromebook/Linux support guide
