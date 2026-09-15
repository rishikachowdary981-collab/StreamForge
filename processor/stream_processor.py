from bytewax import operators as op
from bytewax.dataflow import Dataflow
import json

flow = Dataflow("stream_topology")


# 1. Receive events
events = op.input("input", flow, "input-events")


# 2. Filter events
def filter_events(event):
    return event.get("temperature", 0) > 25


filtered = op.filter("filter_temperature", events, filter_events)


# 3. Map events
def process_event(event):
    return {
        "device": event.get("device"),
        "temperature": event.get("temperature"),
        "status": "HIGH" if event.get("temperature", 0) > 30 else "NORMAL"
    }


processed = op.map("process_temperature", filtered, process_event)


# 4. Print result
op.inspect("output", processed)

from bytewax import operators as op
from bytewax.dataflow import Dataflow
import json

flow = Dataflow("stream_topology")


# 1. Receive events
events = op.input("input", flow, "input-events")


# 2. Filter events
def filter_events(event):
    return event.get("temperature", 0) > 25


filtered = op.filter("filter_temperature", events, filter_events)


# 3. Map events
def process_event(event):
    return {
        "device": event.get("device"),
        "temperature": event.get("temperature"),
        "status": "HIGH" if event.get("temperature", 0) > 30 else "NORMAL"
    }


processed = op.map("process_temperature", filtered, process_event)


# 4. Print result
op.inspect("output", processed)