#!/bin/bash
echo "Stopping nginx..."
systemctl stop nginx || true
sudo rm -f /etc/nginx/nginx.conf
