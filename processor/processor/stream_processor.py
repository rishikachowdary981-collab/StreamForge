from bytewax import operators as op`nfrom bytewax.dataflow import Dataflow`n`nflow = Dataflow("streamforge")
`n# Stream topology: Consume -> Filter -> Map
`ndef filter_event(event):`n    return event.get("temperature", 0) > 25
`ndef map_event(event):`n    return {`n        "device": event.get("device"),`n        "temperature": event.get("temperature")`n    }
`ndef temperature_status(temp):`n    return "HIGH" if temp > 30 else "NORMAL"
`n# Events are grouped into 5-minute windows
`ndef get_window(minute):`n    return (minute // 5) * 5
`n# Basic validation for incoming events
