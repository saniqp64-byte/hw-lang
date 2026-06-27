#!/bin/bash
chmod +x hwlang/hwl
sudo mv hwlang/hwl /bin/
cp -r hwlang ~/.config/
echo "HWLPATH=\"$HOME/.config/hwlang/hwl.py\"" | sudo tee -a /etc/environment