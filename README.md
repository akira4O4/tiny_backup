# Tiny Backup

---

## Intro
A Simple Tiny file backup program

---

## Install
```bash
git clone https://github.com/akira4O4/tiny_backup.git
pip install -r requirements.txt
```

## Config.yaml

```yaml
interval: 1 # Backup interval minutes
input: your\game\save
output: your\backup\output

loguru:
  rotation: "1 day"
  retention: "7 days"
  compression: "zip"
```

## Run
### Linux
```bash
sudo chmod +x run.sh
./run.sh
```

### Windows
```bash
./run.bat
```
