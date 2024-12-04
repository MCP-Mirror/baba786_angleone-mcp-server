import logging
from fastapi import FastAPI, HTTPException
from mcp import MCPServer
from .config import Config
from .angleone import AngleOneClient

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AngleOneMCPServer(MCPServer):
    def __init__(self):
        super().__init__()
        self.angleone = AngleOneClient()
        self.connected = False
    
    async def startup(self):
        """Initialize connections on startup"""
        try:
            Config.validate()
            await self.angleone.connect()
            self.connected = True
            logger.info('Successfully connected to AngleOne')
        except Exception as e:
            logger.error(f'Startup failed: {str(e)}')
            raise
    
    async def get_model_info(self):
        """Return model information"""
        return {
            'name': 'angleone-market-data',
            'version': '1.0.0',
            'description': 'Angle One market data and trading API integration',
            'capabilities': [
                'market_data',
                'order_placement',
                'portfolio_tracking'
            ]
        }
    
    async def generate(self, context):
        """Handle MCP generate requests"""
        if not self.connected:
            raise HTTPException(status_code=503, detail='Not connected to AngleOne')
        
        # Extract command and parameters from context
        command = context.get('command')
        params = context.get('parameters', {})
        
        # Handle different commands
        if command == 'get_profile':
            return await self.angleone.get_profile()
        elif command == 'get_positions':
            return await self.angleone.get_positions()
        elif command == 'place_order':
            return await self.angleone.place_order(params)
        else:
            raise HTTPException(status_code=400, detail=f'Unknown command: {command}')

def create_app():
    app = FastAPI(title='AngleOne MCP Server')
    server = AngleOneMCPServer()
    
    @app.on_event('startup')
    async def startup():
        await server.startup()
    
    app.include_router(server.router)
    return app

app = create_app()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host=Config.HOST, port=Config.PORT, reload=True)