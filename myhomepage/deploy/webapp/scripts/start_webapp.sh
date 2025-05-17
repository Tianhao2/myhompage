#!/bin/bash
set -e

echo "Restarting Gunicorn service via systemd..."

sudo systemctl daemon-reload
sudo systemctl enable gunicorn
sudo systemctl restart gunicorn

# 等待并确认服务状态
sleep 3
sudo systemctl status gunicorn --no-pager || {
  echo "Gunicorn failed to start"
  exit 1
}
