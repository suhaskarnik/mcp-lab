A simple MCP server offering two tools:

- a dice roller, essentially an RNG that generates numbers from 1-4
- a "macrodata refiner", which just takes a number and generates the next 5 numbers

These tools are intentionally simple. The objective is to demonstrate a minimal MCP server that can be accessed by a client

The following commands can be used to run the server and client

```bash
uv run server
uv run client
```

To run the client, the env var `GEMINI_API_KEY` should be set 


