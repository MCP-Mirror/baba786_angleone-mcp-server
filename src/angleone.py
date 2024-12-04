from smartapi import SmartConnect
from .config import Config

class AngleOneClient:
    def __init__(self):
        self.api = SmartConnect(api_key=Config.API_KEY)
        self.session = None
    
    async def connect(self):
        """Initialize connection with AngleOne"""
        try:
            data = self.api.generateSession(Config.CLIENT_ID, Config.PASSWORD, Config.TOKEN)
            self.session = data['data']['jwtToken']
            return True
        except Exception as e:
            raise ConnectionError(f'Failed to connect to AngleOne: {str(e)}')
    
    async def get_profile(self):
        """Get user profile information"""
        try:
            return self.api.getProfile(self.session)['data']
        except Exception as e:
            raise Exception(f'Failed to get profile: {str(e)}')
    
    async def get_positions(self):
        """Get current positions"""
        try:
            return self.api.position()['data']
        except Exception as e:
            raise Exception(f'Failed to get positions: {str(e)}')
    
    async def place_order(self, order_params):
        """Place a new order"""
        try:
            return self.api.placeOrder(order_params)
        except Exception as e:
            raise Exception(f'Failed to place order: {str(e)}')
