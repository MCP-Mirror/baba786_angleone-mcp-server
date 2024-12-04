# Angle One MCP Server

An MCP (Model Context Protocol) server implementation integrated with Angle One APIs for financial data processing and analysis.

## Overview

This project implements an MCP server that provides financial data and analysis capabilities using Angle One's trading APIs. It follows the Model Context Protocol specification to provide a standardized interface for accessing financial market data and executing trading operations.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/baba786/angleone-mcp-server.git
   cd angleone-mcp-server
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file with your Angle One API credentials:
   ```
   ANGLEONE_API_KEY=your_api_key
   ANGLEONE_CLIENT_ID=your_client_id
   ANGLEONE_PASSWORD=your_password
   ANGLEONE_TOKEN=your_token
   ```

## Usage

1. Start the server:
   ```bash
   python src/main.py
   ```

2. The server will be available at `http://localhost:8000`

## Features

- MCP-compliant API endpoints
- Integration with Angle One trading platform
- Real-time market data access
- Order placement and management
- Portfolio tracking

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License