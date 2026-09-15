import faust

app = faust.App(
    "temperature-stream",
    broker="kafka://localhost:9092"
)

input_topic = app.topic("temperature-input")
output_topic = app.topic("temperature-output")


@app.agent(input_topic)
async def process_temperature(stream):
    async for event in stream:
        temperature = event.get("temperature", 0)

        # Filter
        if temperature > 0:

            # Map
            result = {
                "city": event.get("city"),
                "temperature": temperature,
                "status": "positive"
            }

            await output_topic.send(value=result)