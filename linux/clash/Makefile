.PHONY: all download-clash install-clash download-config download-system_call install clean 

all: download-clash download-config download-geoip download-system_call install clean
	@echo "Installation complete!"

download-clash:
	@echo "Downloading Clash binary..."
	@wget https://github.com/Dreamacro/clash/releases/download/v1.14.0/clash-linux-amd64-v1.14.0.gz

download-config:
	@echo "Downloading Clash configuration..."
	@wget -O config.yaml --user-agent 'clash' "<Your Token Here>"

download-geoip:
	@echo "Downloading GeoIP Database..."
	@wget -O Country.mmdb https://github.com/Hackl0us/GeoIP2-CN/raw/release/Country.mmdb

download-system_call:
	@echo "Downloading Clash systemd service..."
	@echo "# /etc/systemd/system/clash.service" > clash.service
	@echo "[Unit]" >> clash.service
	@echo "Description=Clash daemon, A rule-based proxy in Go." >> clash.service
	@echo "After=network.target" >> clash.service
	@echo >> clash.service
	@echo "[Service]" >> clash.service
	@echo "Type=simple" >> clash.service
	@echo "Restart=always" >> clash.service
	@echo "ExecStart=/usr/local/bin/clash -d /etc/clash" >> clash.service
	@echo >> clash.service
	@echo "[Install]" >> clash.service
	@echo "WantedBy=multi-user.target" >> clash.service
	@echo "Clash systemd service configuration written to clash.service"
	
install:
	@echo "Creating Clash configuration directory..."
	@sudo mkdir -p /etc/clash
	@echo "Copying Clash configuration to /etc/clash..."
	@sudo cp config.yaml /etc/clash/
	@echo "Decompressing Clash binary..."
	@gzip -d clash-linux-amd64-v1.14.0.gz
	@echo "Making Clash binary executable..."
	@chmod +x clash-linux-amd64-v1.14.0
	@echo "Moving Clash binary to /usr/local/bin..."
	@sudo mv clash-linux-amd64-v1.14.0 /usr/local/bin/clash
	
	@echo "Moving Country.mmdb to /etc/clash"
	@sudo cp Country.mmdb /etc/clash/

	@echo "Creating system call..."
	@sudo cp clash.service /etc/systemd/system
	@sudo systemctl enable clash
	@sudo systemctl start clash.service
	@sudo systemctl status clash.service

clean:
	@echo "Cleaning up temporary files..."
	@rm -f clash-linux-amd64-v1.14.0.gz config.yaml Country.mmdb
