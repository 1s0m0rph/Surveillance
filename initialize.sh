sudo apt-get install -y mosquitto mosquitto-clients
#other installs here

#pip
pip3 install --user -U paho-mqtt

#subscribers
mosquitto_sub -h localhost -v -t test_topic &
