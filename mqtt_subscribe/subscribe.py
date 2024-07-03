import paho.mqtt.client as mqtt
import ssl
import json

# MQTT Configuration
mqtt_config = {
    "protocol": "websockets",
    "host": "anpr.domain.com",
    "port": 443,
    "user": "",
    "password": "",
    "topics": [
        "gulshan2/lane01/signal/1/anpr/"
    ]
}

# Callback for when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
        # Subscribing to the topics
        for topic in mqtt_config["topics"]:
            client.subscribe(topic)
            print(f"Subscribed to {topic}")
    else:
        print(f"Connection failed with code {rc}")

# Callback for when a PUBLISH message is received from the server
def on_message(client, userdata, msg):
    payload = json.loads(json.loads(msg.payload.decode())) # Decode the message payload
    if payload['partial']:
        minio_url = payload['minio_url_full_image']
        print(minio_url)




# Create MQTT client
client = mqtt.Client(transport=mqtt_config["protocol"])

# Set username and password if provided
if mqtt_config["user"]:
    client.username_pw_set(mqtt_config["user"], mqtt_config["password"])

# Set TLS configuration
client.tls_set(cert_reqs=ssl.CERT_NONE)  # You can adjust the cert_reqs based on your requirements
client.tls_insecure_set(True)  # Disable TLS server certificate verification if necessary

# Assign callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(mqtt_config["host"], mqtt_config["port"], 60)

# Start the loop to process network traffic and dispatch callbacks
client.loop_forever()
