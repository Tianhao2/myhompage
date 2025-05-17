#!/bin/bash
echo "Stopping Gunicorn service..."
sudo systemctl stop gunicorn || true
