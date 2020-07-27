import paho.mqtt.publish as pub

MQTT_SERVER = "surveil-cam-0.lan"#TODO figure out how to scan for available external connections here
MQTT_TOPIC = "test_topic"

pub.single(MQTT_TOPIC,"beep bep",hostname=MQTT_SERVER)
