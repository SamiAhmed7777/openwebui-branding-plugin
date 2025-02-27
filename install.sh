#!/bin/bash
echo "Installing OpenWebUI Branding Plugin..."

# Copy plugin to OpenWebUI directory
PLUGIN_DIR="/app/backend/plugins/openwebui-branding-plugin"
mkdir -p "$PLUGIN_DIR"
cp -r branding-plugin/* "$PLUGIN_DIR"

# Install dependencies if needed
pip install -r requirements.txt

echo "Installation complete. Restart OpenWebUI to apply changes."
