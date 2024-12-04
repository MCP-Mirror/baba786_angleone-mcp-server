from datetime import datetime
from typing import Optional, List, Dict, Any
from smartapi import SmartConnect

class MarketData:
    def __init__(self, smart_api: SmartConnect):
        self.api = smart_api

    async def get_historical_data(
        self,
        exchange: str,
        symbol_token: str,
        interval: str,
        from_date: str,
        to_date: str
    ) -> List[Dict[str, Any]]:
        try:
            data = self.api.getCandleData({
                'exchange': exchange,
                'symboltoken': symbol_token,
                'interval': interval,
                'fromdate': from_date,
                'todate': to_date
            })
            return data['data']
        except Exception as e:
            raise Exception(f'Failed to get historical data: {str(e)}')

    async def get_quote(self, exchange: str, symbol_token: str) -> Dict[str, Any]:
        try:
            data = self.api.ltpData(exchange, symbol_token)
            return data['data']
        except Exception as e:
            raise Exception(f'Failed to get quote: {str(e)}')