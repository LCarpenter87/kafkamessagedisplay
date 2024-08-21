import streamlit as st
from kafka import KafkaConsumer
import os
import json
from datetime import datetime


st.header('Event Shoutout wall!')

consumer = KafkaConsumer(
    'shoutout',
    bootstrap_servers=st.secrets['bootstrap_servers'],
    sasl_mechanism='SCRAM-SHA-256',
    security_protocol='SASL_SSL',
    sasl_plain_username=st.secrets['sasl_plain_username'],
    sasl_plain_password=st.secrets['sasl_plain_password'],
    auto_offset_reset='earliest',
    group_id='consumer1',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
     
)
st.write("hello2")
try:
    for message in consumer:
        stream_message = message.value
        name = stream_message['name']
        avatar = stream_message['avatar']
        msg = stream_message['message']
        ts = datetime.now()

        dt_string = ts.strftime("%H:%M - %d/%m/%Y")
        with st.chat_message(name=name, avatar=avatar):
            st.write(msg)
            st.write(f'From {name} at {dt_string}')
except KeyboardInterrupt:
    pass 
finally:
    consumer.close()








